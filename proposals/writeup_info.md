# Adding modules to C

Unlike more modern programming languages, C lacks a proper module system to control visibility across files. Instead, C relies on the programmer managing declarations in header files. This directly hinders its useability.

This is partly because C is very old, so it carries forward many design decisions that were made back when computer memory was scarce. For example, the C compiler only parses one translation unit (.c file after preprocessing), and symbols must be defined before their first use. Computers and software tools have evolved since then, so it stands to reason that the language should adapt too.

It's worth mentioning that there already exist many implementations of C modules, both in academic papers and open source. C++20 notably introduced modules into the standard. So why is it C code is still written without module support?

In my opinion, it's because developers rarely actively develop in C these days. The decision to write in C has more to do with pre-existing code already being written in C, because the language lacks support for many features that developers use to accelerate their workflow. In other words, people try to avoid spending time writing in C.

So if we want good adoption of a new feature such as a module system in C, it must slot into existing codebases without needing significant manual intervention. We can summarize this in a principle: **.c/.h files have an equivalent modular representation**. In other words, every *reasonably written* .c/.h file pair should be representable as a module file, and every module file should be representable with .c and .h files. This would make the module system familiar to the C developerbase. Additionally, this formulation opens the possibility of automating the migration process, which would greatly accelerate adoption.

Existing implementations of C modules, which includes C++20 modules, do not satisfy this principle. Take this example:

```
// Node.h
struct Edge;
struct Node { struct Edge **edges; };

// Edge.h
struct Node;
struct Edge { struct Node *nodes[2]; };
```

Both Node and Edge reference each other. If they exist in separate modules, the module system would need to support circular imports. Out of all C module implementations I have looked at, none of them allow this. As such, this common pattern needs to be manually resolved when attempting to migrate to using modules. In practice, this is rarely done, leaving most C code in a perpetually dilapidated state.

We can do better. Let's take a look at how it can be done.

## Our module system

Since our module system is under active development, there are a number of restrictions imposed on this iteration that may change later on. Here's what we're targeting at the moment:

Our module system runs after the preprocessor and before symbol resolution. To be a module, `module <identifier>;` must be the first declaration. Then `import <identifier>;` must be before all symbol definitions. Note that only symbol definitions are allowed at top-level in modules, as all top-level symbols within a module are visible to each other. If it is used, `export` must be the first keyword of a symbol definition. Exports make symbols visible to importers.

In addition, we restrict the kinds of symbols we can define. For example, we disallow defining a struct and a global in the same statement (eg. `struct S { int i; } s;`) and don't support inline functions. These restrictions are a result of a lack of development time, rather than a fundamental restriction of the module system. Later iterations are expected to relax these constraints.

### By example

<table>
    <tr>
        <td>
            <b>Example code:</b><br>
        </td>
        <td>
<pre>
module M;
import M1;
export struct S1 s[N];
export struct S { int i; };
struct S1 *f() {
    return (struct S1 *) s;
}
</pre>
        </td>
        <td>
<pre>
module M1;
import M;
import M2;
export struct S1 {
    struct S arrS[2];
    struct S2 *s2;
};
export const int N = 5;
</pre>
        </td>
        <td>
<pre>
module M2;
import M1;
export struct S2 {
    int i;
    struct S1 s1;
};
</pre>
    </tr>
    <tr>
        <td>
            <b>Stage 1:</b><br>
            &emsp;  Top-level names<br>
            &emsp;  (file only)<br>
        </td>
        <td>
<pre>
Module name:          M
Imports:              M1
Type definitions:     S
Variable definitions: s, f
(Note: f is not exported)
</pre>
        </td>
        <td>
<pre>
M1
M, M2
S1
N

</pre>
        </td>
        <td>
<pre>
M2
M1
S2


</pre>
        </td>
    </tr>
    <tr>
        <td>
            <b>Stage 2:</b><br>
            &emsp;  Scope resolution<br>
            &emsp;  (file + imports)<br>
        </td>
        <td>
<pre>
M  -> S, s, f
M1 -> S1, N
--------
Types: S, S1
Variables: s, f, N
</pre>
        </td>
        <td>
<pre>
M1 -> S1, N
M  -> S, s
M2 -> S2
--------
Types: S, S1, S2
Variables: s, f, N
</pre>
        </td>
        <td>
<pre>
M2 -> S2
M1 -> S1, N
--------
Types: S1, S2
Variables: N
</pre>
        </td>
    </tr>
    <tr>
        <td>
            Stage 3:<br>
            &emsp;  Symbol resolution<br>
            &emsp;  and resolving transitive dependencies<br>
            &emsp;  (file + transitive import closure)<br>
        </td>
        <td>
<pre>
"needs definition" graph:
    S  <-\
/-> S1 --/
|-> N
\-- s
    f
</pre>
        </td>
        <td>
<pre>
    S  <-\
    S1 --/
    N
</pre>
        </td>
        <td>
<pre>
    S  <-\
/-> S1 --/
\-- S2
</pre>
    </tr>
</table>

In stage 1, we partially parse the file to collect the names of top-level symbols. Since a symbol table has not yet been generated, we assume the first name a function/global definition is a type, and we skip the parsing of context-sensitive areas such as expressions and function bodies.

Stage 2 then gathers these top-level symbols into a symbol table, which determines what symbols are in scope.

Finally, stage 3 begins the parsing of context-sensitive areas, recursively resolving symbol definitions as needed. As an example, while parsing struct S2, it is found that struct S1 is needed. Then while parsing struct S1, it is found that struct S is needed. In addition, a forward declaration of struct S2 is needed. This results in the following code:

```
struct S { int i; };
struct S2;
struct S1 {
    struct S arrS[2];
    struct S2 *s2;
};
struct S2 {
    int i;
    struct S1 s1;
};
```

### Relationship to the principle

As mentioned earlier, we want .c/.h files to have an equivalent modular representation, and vice versa.

* The modular representation has each symbol definition control its visibility.
    * eg. a function cannot be used in other modules unless the function is exported and its parent module is imported.

In addition, we would also like our module system to have some other properties:

* Import order does not matter.
    * ie. `import M; import M1;` produces the same code as `import M1; import M;`.
* Avoid symbol name clashes between modules.
    * eg. module M and M1 can both define `void foo()` without causing a linker error.
* Module system abstracts the process of fetching symbols.
    * ie. `import` handles details such as boxed/unboxed types, regular/inline functions.

In truth, not all of these requirements can be satisfied completely, due to fundamental limitations or limited development time. In the cases where we cannot support certain features, we should provide "escape hatches" so users can fall back to the legacy C way.


### The algorithm

Explanation of the code.

### Module system extensions

There are a number of limitations with the proposed module system, which can be resolved with extensions:

* global module fragment: Taking inspiration from C++20 modules, this allows us to use header files within our modules.
* export import: This allows us to avoid having to write out every import, by having one import expand into multiple imports.
* module namespacing: We can follow the same ABI as C++20 modules (ie. `name@module`). This helps us avoid linker symbol clashes.
* export inline functions: Allow inline functions to be exported, which would expose the definition of the function to the importer.
* import as module_name: Makes it so we qualify names as `module_name.S` for more control.
* tagged exports: Some modules may need more implementation details than others. `export(tag)` means `import M(tag);` gets it.
* relaxed import placement: import statements could be placed within function definitions.
* alternative module names: What if we imported using the file path, similar to `#include` ?
* constexpr: While not a module-specific feature, having this reduces our reliance on preprocessor directives.
* const int array suffixes: A simpler version of constexpr, handling `const int value = 3; char s[value];` so you use `#define` less often.
* declaration diagnostics: If a user writes `struct S1;` in a module file, provide a diagnostic instead of erroring out.
* dependency files: similar to preprocessors, have the module system output a list of files it has analyzed.
* ordering initializers: `import ordered M;` would mean M is initialized before this module.
* escape hatches: There may be cases where the user needs to circumvent the module system. Let them.
* generating header files: Provide a way to generate .h files from a module file so plain C can use libraries written with modules.
* migration tools: By handling circular imports, we can support much of what .c/.h files do. So build an automatic migration tool.
* code analysis tools: Modules make the link between symbol names explicit, so we can perform more complex analyses and refactorings.

## Module systems in other languages

Note that systems programming languages have special requirements, needing to expose information to the compiler in order to handle features such as unboxed types.

For inspiration, we look at 3 module systems that are implemented within the constraints of the systems programming paradigm: C++20 modules, Rust and Zig.

C++20 modules are of particular interest because C++ is an extension of C, so we could use its approach when implementing C's modules. Indeed, our module system will borrow much of the sytax of C++20 modules. However, C++20 modules' architecture disallows cyclic imports, which makes it challenging to migrate existing code to use this feature.*

*Expand on how C++20 modules works; how its system simplifies iniitalization order, symbol clash and import performance; and how it causes problems with existing systems and codebases.

Rust has crates and modules. A crate can be thought of as a library, and dependencies between crates are acyclic. A crate contains many modules, which behave like C++ namespaces. Rust compiles an entire crate at once, which resolves the problem of unboxed types due to having all modules loaded into the compiler. However this approach clashes with the C philosophy of separate compilation, so we don't take this approach.*

*Talk about incremental compilation, how its query based system works, how its taken 10 years to set up.

Zig's module system is particularily interesting because it allows both separate compilation and circular imports. As such, our module implementation takes significant inspiration from Zig. When a file is compiled in Zig, it is first partially analyzed to determine which symbols are available. Then, symbol definitions are fully analyzed on an as-needed basis. For example, the symbol definition for `S` is only fully analyzed if, say, it is used in a function definition that we need to resolve.*

*Zig's whole system is fascinating and worth looking closer into. It uses comptime to handle many advanced features. Imports are essentially a comptime function and structs.
