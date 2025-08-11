<!--
I fleshed out some problems with strong module theory after working through some examples and writing some code, and got a better idea of how to actually implement my vision. The cynic in me says that I've simply solved many hard problems by slapping "compile-time reflection" on it (which is by no means a simple thing to engineer), but it does solve a number of glaring issues with my previous attempts. Additionally, it takes many concepts from other programming languages, so the strategy seems at least reasonable.
Now, the biggest hole in my proposal is that I do not address the issue of initialization order (I'm kind of putting this one off, because I think I can handle this separately). Additionally, I still need to present "walkthrough examples" and present a formalism.

Motivation
Goal
Strategy (high-level)
Strategy (implementation details)
    Handling unboxed types
    C macros are not exportable
    Import ordering does not matter
    Forward declarations are unnecessary
    Explicit transitive dependencies
    Exporting inline functions
    Generating multiple module interfaces
    Modules use `import` instead of `#include`
    Forall polymorphism
Walkthrough
    Symbols of a module
    How importing modules use symbols
Formalism
    Layout of the codebase
    Individual module information
    Resolving names of exported declarations
    Providing additional information for importers
    Resolving names for compilation
-->

# Modules proposal (v4, strong modules)

## Motivation

Let's walk through the design process of making a C module system.

First things first: **Why do we need modules?** From a theoretical standpoint, it's superfluous - a module system restricts your creative freedom because it makes you think that organizing code and organizing data is different, even though they use the same concepts. However, in practical scenarios it's useful to have a module system because we care about building things fast, reliably, and spread across multiple teams with varying skill levels. **We want modules because it helps us focus on only the parts of the program we're working on.**

But **isn't a C translation unit a module?** *(a c translation unit is a `.c` file after preprocessing)* It has `static` and `extern`, but there isn't a good way to analyze which symbols are used where in the program. A symbol defined in `foo.c` can be declared in `foo.h`, but that symbol can also be declared in `unrelated.c`. Calling a C translation unit a module is like saying a struct is well-defined, even if it can only be used if some arbitrary set of functions is called. We don't consider it a module because it doesn't provide a way to control which modules depend on its contents. **We argue that C translation units, with some access control, can be considered a module.**

## Goal

Let's first clarify what we're trying to achieve with our modules. The term "module" is as abused as "polymorphism" in programming languages, which makes it challenging to determine what we're working towards with a module system for C. Let's start:

* **Make C translation units into modules** (needs some access control on `extern`)
* **Generate module interfaces** (so .h files are not necessary)
* **Each feature is incremental** (each part of the module system requires minimal changes to existing C code - features should feel optional, functioning more like syntactic sugar)

Put simply, we want to require minimal changes to the existing C workflow (source code, makefile, programmer thought process, compiler implementation) while providing something similar to Rust modules. There are other aspects of modules that we'll want to cover - initialization order, modules defined across multiple files, modules nested within a file, module friendship - which have their various solutions, but we'll get to them after working with these main 3 goals.

## Strategy (high-level)

From [this article](https://thunderseethe.dev/posts/whats-in-a-module/) (more specifically, [Backpack in Haskell](https://plv.mpi-sws.org/backpack/)), we are introduced to this concept of **weak and strong modules**. A weak module is tied to its dependencies, meaning that swapping out a dependent module for another requires recompilation. Contrast this with a strong module, where we can provide the dependent modules after the module has been compiled.

For our purposes, the difference is thus: **weak modules are dependent on other modules, while strong modules are dependent on module interfaces.** In order to achieve this, we need modules to control what is exported to other modules, which includes limiting transitive dependencies between modules. This will allow modules to only expose what they own, allowing us to avoid depending on module details. By having modules generate their interfaces, we can separate the parts of C that force modules to be "weak" into the interface generation step, so that the compilation step can work with "strong" modules.

From a logical perspective, modules can only export symbols that they own, and only use symbols that they import. Some concessions need to be made to support the complexities surrounding unboxed types, but this is limited to what is absolutely necessary. Note that C macros cannot be exported, since they run before module processing. The order of imports does not affect compilation - they can be reordered without changing module behaviour. In fact, forward declarations are unnecessary in these modules - we scan all top-level declarations while determining what to export, so the symbols are already in memory by the time we resolve definitions. Explicit transitive dependencies can be created with the use of `export import` - from the perspective of the importing module, it has the same behaviour as if the exported module were imported separately. To support inline functions, we introduce the distinction between a module being visible to the compiler (in order to expand function definitions) and being visible to an importing module. Since we can generate our own module interfaces, we can generate multiple interfaces, which helps solve the module friendship problem. Modules are imported using `import` instead of `#include`, and a translation unit need not be a module to import modules. The forall keyword is an addition from Cforall to support polymorphism, with polymorphic functions using vtables and a single implementation. This has a straightforward implementation in modules (the module that owns the polymorphic function holds the implementation), though if we wish to support specialization for polymorphic functions (ie. multiple implementations), the module system would need to be updated to support this. More details in the next section.

## Strategy (implementation details)

A module is a collection of symbol definitions, which it can export to other modules. It may also import other modules' symbols, which it uses to define its symbols. There are 3 kinds of symbols in C to consider: variables, functions and types.

```
               --------------------------------------
               | module B;                          |
      imports  | import A;                          |  exports
A::a --------> | export int b = a;                  | --------> B::b
A::aa          | export struct aa foobar();         |           B::foobar (+ A::aa?)
               | export struct bb {struct aa foo;}; |           B::bb (+ A::aa?)
               --------------------------------------
```

### Handling unboxed types

Above, we note a problem: whereas functions and variables can export only their symbol declarations, we need the definitions of types in order to use them fully. Languages that use boxed types (eg. Java, Go) do not have this restriction, since the caller only needs to reserve space for a pointer (eg. when calling `B.foobar`). In contrast, C and other systems programming languages (eg. C++, Rust) require handling unboxed types, since it demands control over pointer indirection (also, there may not be a heap available to support boxed types). This means we need to know the definitions of types in order to use them, even if it's just to allocate enough space on the stack. In Rust, this is done by compiling an entire crate at a time; in C/C++, this is done by including transitive dependencies in headers.

We make the following insight: **if we have an oracle that tells us the size and alignment of any type, we can use unboxed types without needing to expose type definitions.** For example, a caller of `B.foobar` need only know that the structure returned has size 32 bytes, aligned to 8 bytes, in order to use it. For type safety, the caller should also know the type returned is `A.aa`, but the caller does not need to know the inner fields of `A.aa`. This means, if `B` does not change, any module that uses `B` does not need to be recompiled unless `A.aa` exceeds its size or alignment allocations. The extra condition that any module that uses `B` needs to be recompiled if `A.aa` exceeding its size or alignment allocations does break the "strong module guarantee" (since `A` is not re-exported, it would ideally not be considered a dependency), but the scope of this has been limited to only what is absolutely necessary to support unboxed types. If the module that uses `B` wants to access the inner fields of `A.aa`, it needs to import `A`.

How do we actually implement this "oracle"? After analyzing the alternatives, option 2 feels the most "natural", despite its inherent complexity.
1. We can perform whole-program analysis to analyze all type-related information, similar to how Rust does it. This allows for maximum expressiveness since this gives us full visibility into the entire program, and can rely on the analyzer to automatically resolve circularly dependent modules (eg. module `A` imports module `B`, which in turn imports module `A`, but in a way that is still resolvable). However, this breaks the principle of separate compilation by accessing the entire program, and raises questions such as "what gets reanalyzed if `A` changes?"
2. We can also extract type information into a separate generated module interface. This aligns closer to the principle of separate compilation, though it still requires special analysis to resolve circularly dependent modules (eg. module `A` imports module `B`, which in turn imports module `A`, but in a way that is still resolvable. In order to avoid a circular import error, this requires only importing the symbols from `B` that `A` needs). A criticism is that this does not really resolve the transitive dependency issue; in a certain sense, it's offloading the problem to a compile-time reflection mechanism. This level of compile-time reflection is also non-trivial, poentially requiring significant re-engineering and validation of an existing C compiler in order to implement. Despite these concerns, this strategy seems to align best with general intuition when analyzing an existing codebase.

### C macros are not exportable

**C preprocessing runs first, then the module system generates module interfaces for exporting symbols, then the translation unit is compiled using the generated module interfaces.** The module system runs after preprocessing because we may want to use C macros to generate export definitions. However, this means the module system cannot export C macros, because they have already been evaluated at that point.

Supporing C macro exports may be possible if we made the preprocessor module-aware. This could be done by augmenting the C preprocessor to check for a `module;` statement or having all module-related statements be `#pragma` directives instead. However, this overcomplicates the preprocessor, making it both hard to develop and demonstrate how to use it. Additionally, certain functionalities such as compile-time reflection are not compatible with the "one pass" nature of the C preprocessor. Put simply, the set of functionalities we wish to support with our module system is complex enough that it warrants being a separate system.

As it currently stands, one can achieve "exported macros" by simply putting them in a header file, then using `#include`. It could also be argued that the trait system in Cforall makes this kind of metaprogramming unnecessary for most use-cases. That being said, this proposal permits future extensions which provide some form of metaprogramming that executes after the module system. Some ideas for inspiration include: string mixins from D, procedural macros from Rust, and staged functions from Zig.

### Import ordering does not matter

A key problem with `#include` is that textual inclusion is order-dependent - including `a.h` before `b.h` may result in different behaviour than `b.h` before `a.h`. Not only does this cause confusion among developers, it also affects compilation speed - while headers can be precompiled, they must always account for the possibility of a C macro completely changing the meaning of the header file.

The fact that each import is independent from each other assures developers that reformatting the import list will not break functionality. Additionally, since modules can only export symbols that they own (with the caveat on types), it is clear to the developer what a module is getting from another.

Since the module system runs after the C preprocessor (and requires a certain formatting of the file), the generated module interfaces can be optimized for maximum compiler efficiency. The potential gains are significant: when the standard library became available to import in C++23 (ie. `import std;`), the time to compile a "Hello World" program essentially halved. This significant reduction in build times likely translates to faster iterations and more productive developers.

As a point for future development, the generated module interfaces can also be analyzed by a language server in order to provide accurate suggestions to the developer. This may be augmented with AI in order to provide robust code-generation capabilities.

### Forward declarations are unnecessary

Since we scan all top-level declarations while generating module interfaces, forward declarations are unnecessary. In fact, the module system can resolve what would otherwise be incomplete types in C. In the following example, even if we added `struct Other;` after `module;`, `struct Other details;` would still break. However, with our module system, we can resolve this.

```
module;
export struct Node {
    int id;
    struct Other details;
};
struct Other {
    int symbols[max_symbols_supported];
};
const int max_symbols_supported = 100;
```

This property of being able to "look ahead" in a file echoes some parallels with classes in object-oriented languages. In those languages, a method's definition can call a method defined later, but still within the same class definition. In fact, modules and objects share many features (eg. abstraction, encapsulation). The main difference is that a module behaves more like a singleton class (as they are actually sections of code), wheras objects can be instantiated.

### Explicit transitive dependencies

There are many cases where development of a module is broken up into parts, yet is often used together. In other cases, some modules are meant to be used in conjunction with another module's symbols.

```
// module std
module;
export import std/vector;
export import std/iostream;

// module wrapper
module;
export import std/map;
export import std/string;
export typedef map[string, string] stringmap;

// module client 
module;
import std;  // this is equivalent to import std/vector;
             //                       import std/iostream;
             //                       import std;  // superfluous in this case
import wrapper;  // this is equivalent to import std/map;
                 //                       import std/string;
                 //                       import wrapper;  // for stringmap
```

In the above case, `std` allows developers to import a common set of functionality without needing to concern themselves with the explicit naming of modules. `wrapper` handles a special case with exporting `typedef`: Since `wrapper` does not own `map` or `string`, it should export the modules that contain them if `client` expects to use the fields of `map[string, string]` (as opposed to simply knowing that `stringmap` is a `map[string, string]`).

### Exporting inline functions

Inline functions require the definition of a function to be available. Similar to the section on "handling unboxed types", we would wish to avoid unwanted transitive dependencies if possible.

```
// module inlined
module;
import supporting;
export inline int power(int a, int b) {
    int ret = 1;
    for (int i=0; i<b; ++i) ret = multiply(ret, a);
    return ret;
}
// module supporting
module;
import deeper;
export int multiply(int a, int b) {
    int ret = 0;
    for (int i=0; i<b; ++i) ret = add(ret, a);
    return ret;
}
// module deeper
module;
export int add (int a, int b) {return a + b;}
// module client
module;
export int foobar() {return power(10, 5);}
```

In this scenario, to compile `client`, the compiler needs the exported symbols of `inlined` and `supporting`. Note that the compiler does not need `deeper` because `multiply()` is not an inline function. However, `client` cannot access symbols from `supporting` unless it imports it directly.

If `inlined` has not generated its module interfaces by the time `client` is being compiled, then the presence of a single inlined function would cause all modules imported by `inlined` to need to be traversed, since the module system cannot ascertain which module contains `multiply()`. After the module interfaces are generated (and the modules have not been edited in the meantime), we can use those instead of traversing imports.

There is another optimization that can be made here: have all exported inline functions generate actual function definitions, so that if importers choose not to expand the function definition, they do not need to regenerate the function definition. It may be tricky to implement if the functionality is not already supported, though this feature is optional.

### Generating multiple module interfaces

A common problem with encapsulation is that certain modules may need certain functionalities from others that should otherwise be private. In object-oriented languages, this is accomplished by designating "friend classes", which get full access to a class' internals. However, this "all or nothing" approach lacks fine-grained control. Another alternative is to present multiple interfaces for importers to choose from, facilitated by the fact that we already generate module interfaces.

```
// module multiple
module;
export int public_function() {return 100;}
export(internal) int internal_function() {return 10;}
int private_function() {return 1;}
// module kernel
module;
import multiple(internal);  // can use public_function, internal_function
// module client
module;
import multiple;  // can use public_function
```

Here, `internal` is a user-defined tag. We could use `export(aaa)` and `import multiple(aaa)` instead. Additionally, we can attach multiple tags to an export (eg. `export(aaa, internal)`) and import with multiple tags (eg. `import multiple(aaa, internal)`). Any symbol that is exported without a tag is always imported, and a symbol that is exported with tags is imported if the import statement includes one of its tags.

Another details is that `private_function()` is technically still accessible by accessing its mangled C name directly. If we truly wanted it to be private, we could use `static`. An additional functionality that the module system could provide is to automatically append `static` to these functions.

### Modules use `import` instead of `#include`

A module is defined by having `module;` be the first statement in a source file (somewhat similar to C++20 modules). Internally, modules work like namespaces, implemented by prepending the module name in front of all declared symbols. There are multiple alternatives to determine the module name - we use option 2 for its brevity:
1. Have the user define the module names (eg. `module A;`). This is similar to how Java and C++ require specifying packages and namespaces, respectively. This gives the developer some flexibility on naming, as it is not tied to the file system. However, it raises some questions surrounding how module discovery works (if a module imports `A`, where is `A`?).
2. Have the module names be defined from a "root directory" (eg. `module;` is module `A` because it is located at `src/A.cfa`, and `src/` is defined as the root directory). This creates import paths that look similar to include paths, allowing us to align more closely with existing C programmers. When searching for an appropriate module, a search is conducted first from the current directory, then we look for an appropriate library (similar to the include path in C). A downside is that this precludes adding nested modules (ie. module definitions within a module file), though nested modules are arguably not that important.

Another design choice that was made was to have files with the same name as a folder exist outside their folder. For example, module `graph` exists at `src/graph.cfa`, while module `graph/node` exists at `src/graph/node.cfa`. The alternative is to have module `graph` at `src/graph/mod.cfa` - this may be more familiar to some developers, but this complicates module discovery (eg. if there exists a module at `src/graph.cfa` at the same time, which takes precedence? Does `graph` need to `import ../analysis` in order to import the module at `src/analysis`?). Taking insights from Rust's move from `mod.rs` to files with the same name as the folder, we opt to use the more straightforward strategy.

Since modules prepend their module name in front of all declared symbols, we use `import` instead of `#include` when importing modules (this is also necessary to support some of our compile-time reflection mechanisms, which would be challenging to implement in the preprocessor). This automatically removes the module name from the front of the symbol names. If this causes symbol clashes, they can be resolved using attributes (eg. `A::a` means "symbol `a` within module `A`").

This prepending of the module name in front of all symbols within a module can result in undesirable behaviour if we use `#include` within a module, as all of its contents will be prepended with the module name. To resolve this, we introduce extern blocks, which escape the module prefixing (eg. `extern { #include <stdio.h> }`, though with a newline after the `>`).

By having modules prepend their names to their symbols, we can add functionality to perform a "unity build", as every symbol can be disambiguated. This would allow us to balance a "development configuration" with the benefits of modularization, alongside a "release configuration" with maximum optimizations.

### Forall polymorphism

The forall keyword is an addition to Cforall to support polymorphism, with polymorphic functions using vtables and a single implementation. If a module exports a forall statement, the module owns the polymorphic function implementations, while the polymorphic function declarations are exported (if these were declared inline, the definition could be exported, similar to C++20 modules). Polymorphic types are instantiated from the caller's side, so their definitions are exported. This may present problems, but currently I am not familiar enough with Cforall to judge.

An interesting case is to consider if Cforall could be updated to perform specialization (multiple implementations for a single function) in addition to the single implementation strategy. This would be similar to Rust's `impl` vs `dyn` traits. To support this, the module system would need to be updated, as we would want the multiple implementations to exist within the module that owns the forall statement.

## Walkthrough

A module holds a collection of symbols to be exported. What we're concerned with is how the importing module can use these symbols. In order to answer this, we will analyze:
* What are the kinds of symbols and what does the importing module see?
* How does the importing module disambiguate between symbols?

Our guiding principle behind our modules is that, as much as is possible, **every symbol definition should have full control over who can see it.** This means that you cannot declare a function or struct that is defined in another module unless that module exports it and you import said module (of course, it may be accessible using `extern "C"`). We will see certain cases where types and inline functions break this abstraction somewhat, but we try to limit this "information leakage" as much as we can. A benefit of this is that our inductive proof usually only needs to reason using the previous step, as every symbol is logically isolated from each other.

### Symbols of a module

Modules in our modules are either types, functions or variables. While types can be defined in the same line as a variable (eg. `struct {int i;} name = {5};`), we will make the simplifying assumption right now that this does not happen (in the example, both `name` and the anonymous struct would be exported together).

#### Types

There are 3 kinds of types: builtins (eg. `int`), user-defined (ie. `struct`) and aliases (ie. `typedef`). We defer discussion on pointers, references and arrays until afterwards.

Built-ins are provided by the compiler to every module, so we don't need to consider them. We can simplify aliases as a `struct` with one field, which has an implicit field access.

So `struct` is really the only type we need to concern ourselves with. Based on our guiding principle, if we export a `struct` that has a `struct` field which is not itself, then it should not export any information related to that field's type. The importer will be able to access all of its fields, but the `struct` field is essentially an opaque type (if a module also wants access to that, it needs to import that `struct` too).

Unfortunately, this isn't technically possible. First, we have unboxed types (boxed types are implemented as a pointer to the actual object). This means we need to know the size and alignment of every field, so we know how large the struct is and the offsets of each field. Second, when a user initializes a variable with a field, they need to be able to write down the type name (eg. `struct Exported e; struct Field f = e.f1;`). So we need to know the size, alignment and name of a field (in the previous example, move/copy constructors may also need to be considered, but in C we simply copy bytes). A similar thing happens when returning types from functions (eg. `struct Unexported foo();`), which we will discuss later.

How do we obtain this size/alignment/name information? We use compile-time reflection to crawl import modules as needed. Note that this needs to handle circular imports, as it should only fail if we encounter a type name ambiguity (eg. we import module `A` and `B` which both export `struct S`, and we need a `struct S`) or the type has infinite size (eg. `struct A {struct B b;}; struct B {struct A a; int i;};`). This means the number of modules that need to be analyzed in order to determine the size/alignment of a `struct` is only bounded by the size of the codebase, but in practice this should not happen often.

Pointers and references are boxed values, so size/alignment information of the underlying type is not gathered. However, we still require modules to import the symbol in order to handle name disambiguation. Arrays may be parameterized by an integer whose value must be immediately available. This is key, otherwise we can end up with cases such as `struct S {struct T t[sizeof(struct U)];};`, which may require fixpoint analysis. In our case, we can simply leverage compile-time reflection in the same manner as we do with field structs.

#### Functions

Functions have the form `returnType name(parameterType, ...numberOfParameters) {...body}`. In order for importers to use this function, we need to provide the size, alignment and name of any types in its declaration. We use compile-time reflection to resolve the details (see Types section for details).

If we are exporting an inline function, from the compiler's perspective the function body is also exported. This may also use compile-time reflection in order to resolve the symbols within the function body (which is done within the context of the containing module, not the importing module).

Cforall introduces a keyword called `forall`, which can be used to create polymorphic functions. At the moment, these functions do not specialize - there is only one instance of this function, and callers need to pass a vtable alongside any polymorphic type parameters, similar to how the `dyn` trait in Rust works. This means that trait information must be provided to the importing module, which unfortunately breaks our guiding principle somewhat. Within a `forall` block we can also define polymorphic types, which can be used as the return value of a polymorphic function. In that case we need size/align/name information, and the first two are currently handled by calling a "layout function" at runtime (this could possibly be moved to happening at compile-time, but isn't at the moment). As such, we need provide the layout function to the importing module, which unfortunately breaks our guiding principle too. So polymorphic functions can be made to work with our system, but they break our guiding principles to some extent.

#### Variables

Variables have the form `variableType name = expression;`. We make the simplifying assumption that only one name is defined at a time (ie. no `int a, b, c;`). An importing module needs to provide the size, alignment and name of `variableType` in its declaration to any importing modules. We use compile-time reflection to resolve the details (see Types section for details).

If the variable is actually a polymorphic type (see Function section for details), I'm actually not sure how this works. The layout function can only be called at runtime, but you need the information in order to allocate the appropriate amount of space in the `.data` section. More analysis is needed here.

### How importing modules use symbols

The previous section notes compile-time reflection as the solution to many of our challenges with modules. Here we will explain how symbol names are resolved to the correct modules, allowing us to define how our compile-time reflection crawls through modules in order to determine the information it requires.

#### Gathering symbols

First, we scan the top-level declarations of a module, gathering a list of imported modules and top-level symbol names defined within the module.

```
// module data/graph/node
module;
import edge;
import ../minheap;
import stdlib;
const int maxEdges = 10;
export struct Node {
    int id;
    int value;
    struct Edge edges[maxEdges];
    struct MinHeap someField;
};
// Shadows imported MinHeap
struct MinHeap {int capacity; int size; int *data;};
struct MinHeap initHeap(int capacity) {
    // Assumes malloc doesn't return error code
    return {capacity, 0, (int*)malloc(sizeof(int) * capacity)};
}
void destroyHeap(struct MinHeap* h) {
    free(h->data);
    h.capacity = 0;
    h.size = 0;
}
```

We first look for the import relative to the current directory - if that fails we look at libraries. So our set of imports here are: `data/graph/edge`, `data/minheap` and `stdlib` (library module).

The top-level symbol names are: `maxEdges`, `Node`, `MinHeap`, `initHeap` and `destroyHeap`.

#### Crawling other modules

Continuing with our example, we do the same top-level analysis with the imported modules.

If `data/minheap` has `export import minheap/functions;` defined, then it is as if `data/graph/node` has `import ../minheap/functions;` defined. This can keep going - if `data/minheap/functions` has `export import`, it is also added to `data/graph/node`. After all `export import` have been resolved, we can look at the top-level declarations of every imported module in order to determine what symbols are visible to `data/graph/node`.

Now, we can bind each symbol within `data/graph/node` to the correct module. The details of how multiple symbols are disambiguated are described in the Overload resolution section.

In addition to name disambiguation, some symbols need additional information in order to be useable by importers. For example, size/alignment information of types, function bodies for inline functions, and trait information for polymorphic functions. This information is obtained by performing the above steps, but on the importing module instead of `data/graph/node`.

This recursive task raises the problem of circular imports: What if we recurse back to `data/graph/node` (or any module that creates a cycle)? As long as we are analyzing different symbols inside the circularly imported module, this should not pose a problem. This leaves us with handling the problem where we circle back to the same symbol. For size/alignment analysis, coming back to the same type means that said type contains itself, which for our purposes is not resolvable/infinite size. If an inline function calls other inline functions that mutually recurse with itself, we can either produce a forward declaration of the function within the underlying C implementation (Cforall compiles down to C), or make mutual recursion be a regular function call. The first option is ideal, but if this is not supported in the C spec, we can fall back to the second option. For trait information, we could emit a warning, but if a trait includes itself, that can be safely ignored (a trait is a collection of conditions, it contains itself by definition). Since we can handle all of our circular problems, our system is well-defined here.

#### Overload resolution

A key aspect about our modules is that imported symbols are used in the same way as they are defined - no namespacing needed (eg. `struct Edge` in the provided example). While this raises the potential for name collisions, we argue that with the right compiler tools and the ability to disambiguate between different modules (eg. `A::a` means "symbol `a` within module `A`"), this can be a reasonable tradeoff (unfortunately, much of the tooling here is out of scope for this proposal).

The reason behind this decision comes from 2 places: First, if we add namespacing to imports, then when we have an imported function that returns a type defined in another module, we would be forced to write the module name (the alternatives don't fare much better in terms of brevity and readability). Second, a core feature of Cforall is its advanced overloading system (eg. allowing multiple variables with the same name but different types to coexist). Adding namespaces would likely limit our ability to research and take advantage of this feature.

This means we have both symbols defined within our module and imported symbols participating in overload resolution. This requires extending our existing overload resolution algorithm to handle multiple types with the same name (currently we handle multiple functions and variables with the same name, but not types). This also requires refactoring the overload resolution algorithm to hold the full name of a symbol (symbol name + module name). Finally, if overload resolution favours two options equally, it should favour symbols defined within the given module (eg. `struct MinHeap` in the provided example). Note that this will only happen if the alternative is strictly better, otherwise it is ambiguous.

## Formalism

Taking the Walkthrough section a step further, we will provide a rough sketch of a formal argument that our module system is well-defined.

We'll first describe the layout of our module system by providing a rough description of the file structure and grammar we are working with. Then we describe what we can grab from each module file separately. By combining this information with those from other modules, we can determine which module's symbol is being referred to in each exported declaration. Note that for some symbols to be properly used by importers, additional information like size/alignment information will be necessary, which we will show is possible to obtain. Finally, with this information, we can resolve every symbol within a function body or expression, thereby completing the compilation process.

### Layout of the codebase

In order to provide a formal argument that our module system is sound, we need to first describe the format of the codebase we are trying to analyze.

The file system is set up so that imports are relative to the current directory, or found in a library. For example, a module file `data/graph.cfa` trying to access `data/graph/node.cfa` would write `import graph/node;`. If such a file doesn't exist, we will look for `graph/node` within the provided libraries (starting from the root directory of each library).

Module files have `module;` as their first statement. Import statements are written as `import filePath;`, where the file path can be escaped with double-quotes if necessary. Only top-level statements can be exported, which is done by placing `export` at the beginning (eg. `export const int i = 3;`). The available top-level statements are:
* Types: `struct` and `typedef` statements. Only one `struct` can be defined per top-level statement (eg. no `typedef struct {int i;} MyStruct;`).
* Functions: Format is `returnType name(parameterType ...numberOfParameters) {...functionBody}`.
* Variables: Format is `variableType name = initializerExpression;`. Initializer may be omitted. Only one variable can be declared per top-level statement (eg. no `int a, b;`).

The syntax of function bodies and initializer expressions can mostly remain unrestricted, as compilation is outside of the module system's purview (we provide the symbols and sufficient information on how to use them to importers). Some aspects we need to note are:
* No user-defined copy/move constructors: In order to handle `func(s.f1)` (where `void func(struct Field);`), we need to be able to create a copy of `struct Field` without knowing its fields (in the example, the importer knows `func` and the type of `s`, but does not need to know the details of `struct Field`). Having user-defined copy/move constructors can be done, but we opt to avoid it here.
* `::` operator: Sometimes we need to disambiguate which module a symbol belongs to. `struct InBothModules foo();` can either use `struct InBothModules;` from `import a;` or `import b;`. Trying to resolve this by analyzing the function body of `foo()` may be possible, but would likely be very challenging to implement. To resolve this, we can write `struct a::inBothModules foo();` instead.

### Individual module information

For every module file, we can collect the import list and the top-level symbols, without needing to consult any other files. The top-level symbols include types, functions and variables.

Top-level statements, at least the way we have it set up here, avoid any context-sensitive sections (eg. `MyType * a;` can be multiplication or a variable). This means we have no issues parsing all symbols at the top-level (function bodies and initializer expressions are context-sensitive, but we don't need to deal with them here). This means that for each module file, we can grab an import list, a type list, a function list and a (global) variable list, as well as determine which are exported.

### Resolving names of exported declarations

Now we wish to resolve every symbol in any module's top-level declaration (this does not include the function bodies or initializer expressions). In order to do this, we first collect a module's full import list, then all of its imported symbols, before finally resolving our symbols.

In order to determine a module's full import list, we first look at the individual module information of each imported module. We initially look for the imported module relative to the current directory of the module that the import statement is in - if it does not exist, it will look starting at the root directory of any provided libraries (if we can't find the module, we error out). If any imported module has `export import moduleName;` (or some other module name), then we look at those too. If we end up importing any modules we have already imported (or the module we are getting the full import list of), we can ignore those. Since there are a finite number of modules in a codebase (plus any provided libraries) and we don't analyze a module twice, this search will terminate with a full import list.

To collect all the imported symbols, we take every module in the full import list and we grab all of the top-level statements that have `export` as their first keyword. This gives us a imported type list, a imported function list and a full variable list.

Now that we have a list of imported symbols as well as the module's own, we can start resolving symbols in the top-level declarations. Since our grammar is not context-sensitive outside of function bodies and initializer expressions, there is no ambiguity determine whether a type or variable is needed. To resolve names, we first check to see if it uses the `::` operator - if so, then we look using the same strategy when looking for imported modules (if the module isn't in the full import list, we error out). Then we look in the module's own top-level symbols to see if we have a type/variable that matches the symbol's name (this means a module's symbols shadow its imported symbols). If we don't find a match, then we look in the list of imported symbols. If the list of imported symbols has more than one match, we error out due to ambiguity (it may be possible to use overload resolution here, but for now we'll prompt the user to use a `::` operator).

Something to note about this setup is that forward declarations are neither necessary nor allowed, because all visible symbols are known before attempting to resolve names.

### Providing additional information for importers

Unfortunately, in order to use some of these top-level symbols, simply resolving the names within top-level declarations (ie. not including function bodies or initializer expressions) is not enough for an importer to be able to use it. For example, if a function returns a `struct`, we need to at least know the size/ alignment of the `struct` in order to use it.

Type names are found within the definitions of other types, the return and parameters of a function, and the type of a variable. In order to fully specify a type, we must at least know the size/alignment of its fields. To use a function, we also need to know size/alignment of return and parameter types. To use a variable, the size/alignment of its type is not technically required, but to keep its semantics consistent with that of field access, we require it (eg. `struct Unimported x = s.f1; struct Unimported x1 = importedVariable;`).

For functions and variables, we first resolve the type (for types, we move to the next step). Then we look at the fields of that type and resolve those types (pointers don't need to be resolved because pointers have a defined size/alignment). We keep recursing until we resolve everything or find a cycle (if we have a cycle, we error out), and this terminates because there are a finite number of symbols. Additionally, types may be arrays, which are parameterized by an integer (if we resolve to something that is not an integer, we error out). The C spec requires that this integer's value must be constant and immediately calculable, which means `char padding[64-sizeof(int)]` is fine but not `char padding[64-sizeof(struct U)];` (this functionality can be supported and may be useful for cache-aware programming, but we will not support this for now). This means we can fully resolve everything within a well-defined type, and therefore collect its size/alignment.

While the importing module doesn't change its behaviour whether a function is inline or not, the compiler must see the function body, which means it must be included in the file sent to the compiler. In order to resolve the inline function body, then from the perspective of the module that contains the inline function, we must collect the full import list, then all of the imported symbols. If any of those imported symbols are inline functions, then we need to keep recursing. If we find a mututally recursive inline function, we would emit a forward declaration (eg. `inline float a();`). Note that the module that owns the inline function must use `extern` (eg. `extern inline float a() {return 5;}`) in order to ensure a definition is emitted. Since there are a finite number of modules, this will terminate. Note that if an imported module contains an inline function, we do not provide the function definitions of its non-inline functions - this means the compiler cannot inadvertently expand the definition of a function it is not meant to have access to.

Cforall introduces the `forall` keyword, which allows creating polymorphic functions and types. I am not completely familiar with the internal implementation of these (hence it isn't actually a part of this formalism), but I know they use a single implementation, with callers passing in a vtable for each concrete instance of a polymorphic type (similar to Rust's `dyn` trait). This means that we need to provide the traits of each polymorphic type in a polymorphic function in order for an importer to use it. This analysis follows a similar logic to the size/alignment of types, except that we're working to define a trait rather than a type. As such, if a trait mutually includes another trait, we ignore the circular reference. I am unsure if resolving traits requires resolving more than the symbol names of each type - if necessary we use the same technique as size/alignment analysis.

### Resolving names for compilation

Now that we have every top-level symbol visible to a module ready to be used, we can proceed to resolve every symbol in each function body or initializer expression. This functionality is actually the domain of the overload resolution system rather than the module system, but the module system adds additional features which need to be handled by the overload resolution system.

First, name resolution needs to be augmented to also store the containing module name. We also need to support the `::` operator, used when specifying a specific module name. This doesn't change how the overload resolution algorithm would work, but we need the containing module name in order to generate the full symbol name in the generated C code.

Additionally, we have the fact that the imports' symbols are now available to participate in overload resolution. In this formalism, our module's symbols have priority over the imports' if they are deemed equal by the overload resolver, and we error out if we have to choose between two imported types with the same name. This allows us to handle the 2 special cases that our module system introduces to the overload resolver.
