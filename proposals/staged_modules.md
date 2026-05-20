# Staged modules

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

## What's going on here?

### User perspective:

The module system runs after the preprocessor and before symbol resolution.

To be a module, `module <identifier>;` must be the first declaration.

`import <identifier>;` must be before all symbol definitions.

If it is used, `export` must be the first keyword of a symbol definition.

Only symbol definitions are allowed at top-level in modules, as all top-level symbols within a module are visible to each other.

Exports make symbols visible to importers. Inline functions cannot be exported (moved to a future extension).

*Some of these restrictions can be modified through future extensions (see Language extensions).*

### Stage 1:

Stage 1 gathers useful information from a single module file. To support cyclic imports (M and M1 import each other), this stage cannot rely on other files.

We lack a symbol table at this stage, so we can only parse context-free information. However, we can extract top-level names.

Some export metadata (eg. is symbol exported or not) is recorded, but most information (eg. `const`, field names) can be left to a later stage.

*In order to parse the file without a symbol table, the first name of a function/global definition is treated as a type.*

*This means we disallow implicit int return types (they have been disallowed since C99). Note expression statements are disallowed at top-level.*

### Stage 2:

Stage 2 gathers useful information from a module file and its direct imports. We gather import information from stage 1.

Here, we determine which symbols are in scope (ie. build a symbol table).

This stage lacks the ability to inspect symbol definitions, so expressions (eg. `x.y.z`) are left for stage 3 to resolve.

Types are not fully resolvable due to array sizes, `decltype` and templates. The names of types can be resolved in C, but can be done in stage 3 instead.

*Note: `auto` and `typeof` are not allowed at top-level in C23.*

### Stage 3:

Stage 3 can look up symbol definitions by following imports recursively (ie. can access the transitive import closure). We use information from stage 2.

Here, we can resolve the rest of the AST by loading symbol definitions as needed (eg. S1 needs the definition of S, but only needs declaration of S2).

If a cycle is detected while loading symbol definitions, we have a type of infinite size or an unresolvable ambiguity &mdash; produce an error diagnostic.

To reduce file IO, modules are lazily loaded in as symbol definitions are needed &mdash; S1 doesn't need the definition of S2, so M2 isn't loaded in.

To do this efficiently, expression parsing code would call lookup functions to go from name to symbol candidates.

*The stitched modules approach is to output code that would be reparsed in the original compiler, which is simpler to implement.*

*However, if the module system does not parse expressions, it has to make a conservative guess on reachable symbol definitions, which is less efficient.*

## Language extensions

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
* declaration diagnostics: If a user writes `struct S1;` in a module file, provide a diagnostic instead of erroring out.
* dependency files: similar to preprocessors, have the module system output a list of files it has analyzed.
* ordering initializers: `import ordered M;` would mean M is initialized before this module.
* escape hatches: There may be cases where the user needs to circumvent the module system. Let them.
* generating header files: Provide a way to generate .h files from a module file so plain C can use libraries written with modules.
* migration tools: By handling circular imports, we can support much of what .c/.h files do. So build an automatic migration tool.
* code analysis tools: Modules make the link between symbol names explicit, so we can perform more complex analyses and refactorings.

## Notes

### Stage 3 does a lot of duplicated work

For example, S1 needs the definition of S in all 3 modules. Another example is if we had inline functions.

This information could be cached. We would need to consider how to handle staleness, dependency tracking, race conditions and duplicate symbol definitions.

### Stage 2 vs stage 3

Consider a codebase as a graph (DAG), where nodes are the symbols and directed edges are dependencies (either "needs definition" or "needs declaration").

Stage 2 builds the symbol table, which is used to determine these edges. Stage 3 resolves the graph by following the edges as necessary.

### What build optimizations does this enable?

Each file within a stage can be processed in parallel.

If recompiling earlier stages generates new information that importers don't use, we can skip recompiling importers.

This fine-grained analysis could be accomplished by hashing symbol definitions, similar to Rust incremental compilation.

### Extracting top-level names

Extracting top-level names can have multiple edge cases. For example, the following is valid in gcc and clang:

```
struct Outer {
    int i;
    struct Inner {
        int j;
    } k;
};

struct Inner i;
```

Since C is not formally specified, it is infeasible to catch all cases (we aim to eventually produce a "semi-formalism" of the module system, however).

Rather than trying to cover all cases, it is more practical to work towards a use-case &mdash; migrating existing C code to this module system.

In that light, the edge case demonstrated above is a lesser priority, as it is used infrequently and is relatively easy to manually fix.

Handling cases such as `export struct S { int i; } s;` (exports S and s) are more important in comparison, as this pattern is fairly common.

### To reparse or not to reparse

While Zig demonstrates that all 3 stages can be performed in a single pass, this likely requires rewriting large parts of the compiler.

Instead, we can implement stages 1 and 2 as producing JSON objects, and have stages 2 and 3 reparse the module files instead of caching the tokens.
The outputs of previous stages can be passed via the command line for simplicity.

We can consider optimizing this at a later point, and measure speedups. But at this stage, getting functionality is more important than execution speed.

### Reusing existing code

Taking the idea of reparsing files even further, we can take the stitched modules approach &mdash; output code to be reparsed in the original compiler.
This means the module system does not parse expressions.

The naive approach of treating an expression like a black-box would force us to load all visible symbols, since we wouldn't know which symbols it uses.
This is highly likely to result in a lot of false cycles, which would severly hamper functionality.

A better approach is to extract a set of identifiers from the token stream of the expression, since an expression only uses symbols that it specifies.

### Dependency tracking

In a large codebase, only a few files change between compilations. We would like to avoid recompiling the codebase every time.

The C preprocessor can output a dependency file (.d) that lists the files that have been inspected, which is later used to determine when to recompile.
Similarly, each stage of the module system can also output a dependency file.

Like Zig, we can go further by using hashes instead of just timestamps, and track dependencies at the granularity of top-level symbols instead of files.

At this stage of implementation, we defer this work until later.

### Comparison with Zig

Zig is a systems language with cyclic imports. It performs all 3 stages in a single pass by lazily analyzing information.

Building a module resolves expressions (stage 3), which needs a symbol table (stage 2), which means extracting information from imports (stage 1).
If an expression needs a symbol definition from an import, then to parse the symbol definition you need its symbol table. Keep going until resolved.

Since all symbols get resolved, a library or executable file can be generated directly without having to call the linker afterwards.
This shows that having a module system allows a language to subsume responsibilities which would otherwise need to be delegated to a separate build system.

Object files and intermediate representation are stored in a cache. Incremental compilation patches binaries with top-level declaration granularity.
Zig's build system also uses a DAG of steps that run concurrently, and track compilation inputs (eg. compiler options) to get deterministic builds.

While this would be useful, creating a build system is a huge engineering effort and outside the scope of this proposal.
This proposal is concerned with adding language features that a module system would use, which may be leveraged by a build system in the future.

*To highlight the challenge of creating a build system, many of Zig's features (eg. incremental compilation) are still considered experimental.*
*Rust has spent almost a decade refining its incremental compilation architecture.*

*A quick note about Rust: it also has a module and build system. A crate is considered one translation unit, which is aggressively optimized.*
*This hampers incremental compilation. By contrast, Zig compiles multiple object files for a project, so it can do some form of separate compilation.*
