<!--
The initial designs. This was done after solving some of the implementation issues, but the newer versions refine these ideas better.
The language comparison section is still useful as a reference, though.

Behaviour of proposed modules (difficult to read)
Proposal
Language comparison
By example (+ segue to next version)
-->

# Modules proposal (v1, ideas)

## Behaviour of proposed modules (difficult to read)

Behaviour of `module`:
* Must be the first statement of a .cfa file. Using this means the file is a module, and can be imported.
* Modules cannot be used with `#include`. Similarly, non-modules cannot be used with `import`.
* `ordered module` means this module cannot transitively depend on itself. Using this allows the use of `init`, `fini`, `export inline`, and mitigates initialization order fiasco.
Within the module system, module “book” is transformed into the regular C form, with a few differences:
* While #include can potentially cause an ordering dependency, separate imports do not share state.
    * The goal is that adjacent `import` statements can be reordered without affecting program semantics.
* `stdio` and `string` may need to be included in the header, because they may define type information that is important to `struct Book`
    * They would be considered private to the importer of `book`, so encapsulation is preserved.
    * An optimization could be done to avoid searching those modules, since char and int are already defined in the current file.
Here is the behaviour for `export`:
* `export import` makes [incomplete thought]
    * This is fine for type and function declarations, since defining the same symbol twice is an error.
    * Macros cannot be exported in circular macros because of an ordering issue (see below). Note that [C11, 6.10.3 Macro replacement](http://port70.net/~nsz/c/c11/n1570.html#6.10.3p2) considers it a constraint violation (ie. undefined behaviour) if two macros are defined with different values.
Note this step happens after the preprocessor, as it is possible a developer wants to use the code-generation capabilities of macros.

## Proposal

Modules mean that header files no longer need to be written by the user, yet modules should behave very similarly to .c/.h configurations (ie. they require minimal code rewriting to transition to using modules). This means that our modules need to handle transitive and circular dependencies, multiple interfaces, and different levels of visibility need to be handled (we defer the issue of macros to a separate discussion). At the same time, we would like to improve compilation times, provide better lexical scoping of symbols, and provide a mechanism for ordering initialization and destruction functions.

Cforall modules achieve this functionality by behaving similarly to Rust modules - each module behaves like a namespace. In order to allow circular dependencies, we need an early compiler pass that splits the module into an interface and implementation file. Since C is a systems programming language that allows things to be created directly on the stack, both caller and callee of a function need to know type information (even though it’s only for the compiler, not for the user). The way we get around this without requiring C programmers to change their code structure entirely is: transitive imports are done, but if not export imported, everything is private (ie. not visible to the programmer unless they import it separately). Exported structs have their definitions exposed, while exported functions are only declared. If it turns out the transitive imports loop back to the original file (eg. the Nodes/Edges example), it’s treated as importing the struct declaration.

Those are circular modules, designed for easy transition for C programmers used to the .c/.h format. Now let’s consider ordered modules, which are needed for module initialization/destructor functions and inline functions. Instead of `module;` , we use `ordered module;` to denote these. If we try to import such a module, we will look inside some cache for the compiled file (say, .cforall_cache folder) - if it doesn’t exist we need to compile it first. If a cycle is found, an appropriate error diagnostic is emitted. We can use the depth of the ordered module import tree to determine initialization order (eg. ordered modules without dependencies use .init_array.10, depth 1 use .init_array.20, etc.). We introduce a new keyword for initialization and destruction, `init { … }` and `fini { … }` , which are essentially functions that run before main() (what about different syntax? Should this run before or after global variable initialization? Go allows multiple `func init() { … }` , which run after variable initialization https://go.dev/ref/spec#Package_initialization ). If .init_array.x has the same value, ties are broken by the order in which files are presented to the linker (left-to-right). Since Go doesn’t have circular modules, it stands to reason: can we also change any Cforall project to only use circular modules? There are two structures in Cforall I can think of that have problems - mutually recursive functions (functions that rely on each other) and forward type declarations (types that rely on each other, but only through pointers). Both can be solved with a slight “break” of ordering: `peek` keyword, which allows looking at function declarations and type definitions, but does not do transitive imports. A type’s layout in memory cannot be composed of another type, eventually ending up back at itself, because it would have infinite size (assuming that type sizes are static - if they’re not then you’re going outside the ABI). If your type is a class that has a method that recurses with another class’ method, you might be in a bit of a pickle - you’ll have to split the methods out of the class definition, be able to inspect the class type without the method information, or defer the need for such information until after parsing lexically visible information. However, C does not have methods (or if we plan on adding them, they might exist outside the definition), so I don’t need to worry about this.

Now consider a special class of modules that run before any other module. These could be modules that override standard libc behaviour, such as thread management or garbage collection (how could one find a list of compiler-provided functions, like malloc?) . These are specified in the module containing `main()` , labelled `preinit { import thread; import gc; }` . Listing modules inside the `preinit` block cause them to run in order, before any other ordered module initializers (in the example, if thread somehow imports gc, then gc will actually run first). A module initializer should not run twice (what if it’s called from a dynamic library? Perhaps all initializers have a check to make sure they don’t get called twice) . Dynamic libraries cannot be listed in the `preinit` block, in order to avoid triggering ld.so before the initializers have run (I don’t know if this is a problem, just being cautious. Maybe I’ll add another keyword `dynamic;` inside `preinit` block, after which you can import dynamic libraries). Or maybe there should be a stricter restriction on what can be put in the `preinit` block…

And now for module functors. One issue with encapsulating header behaviour is that there are some headers that depend on macros defined before it. After looking at OCaml functors, it turns out that this design pattern can be used to solve this problem. Use something like the syntax `import arch with { THING { … } ANOTHER_THING { … } }` and `module functor arch(THING, ANOTHER_THING)` (not the clearest about this syntax…) . In the compiler implementation, different invocations of different module functors are cached as separate.

But just to put a wrinkle into this encapsulation of macros - when you compile a project, you may also globally set a number of macros to be passed to every file. If you change this, you only want to recompile what you changed. Which means we need some way to determine which modules actually used which macros, as well as their dependencies.

[Since the module system essentially touches everything about running a whole program, there’s so many more ideas to try: allowing alternative compilation strategies, such as Rust crates, templated forall, test mocking, static vs dynamic libraries (+ how does this affect preinit?) , distributed builds]

## Language comparison

Let’s compare how other languages differ in implementation of their modules. But before we take a look, a foreword: the term “module” often refers to different constructs in different languages, which are often not analogous with each other. The definition of a “module” refers to a group of related entities, which can technically be applied to any recursive construct in structured programming (eg. for loop). However, in practice we refer to modules as a method of organizing large groups of functionality, around the scale of source files. As such, module systems often need to consider the coordination of aspects of the codebase that are external to the responsibility of the compiler, such as linking, observability, build systems and versioning. With this in mind, let’s take a look at different languages.

* C++
    * C++20 modules behave more like separate libraries, requiring support from the build system. The implementation can be split into separate files, though it is not required: the interface file can also contain all of the implementation. The issue of not having headers is resolved by requiring the module to be compiled prior to any other file importing it, thus disallowing circular dependencies. This makes them more suitable for the bundling of libraries (eg. the C++ STL) and high-level codebase organization than a more granular organization of a codebase.
    * C++ namespaces offer a more granular organization of a codebase, and can be thought of as prepending the name of the namespace onto any symbol defined inside it. This allows multiple definitions of the same symbol to exist, as long as they are defined in different namespaces. There is no restriction on which files can define which namespaces, though in practice namespaces are roughly correlated with the filesystem of the codebase.
    * As of 2025, C++20 modules are not fully supported in any major compiler or build system. This is because implementing this feature requires systematic changes to the compiler and build system, as well as significant rewrites to any codebase wishing to leverage this feature. Library versioning is not handled in the language spec, instead relying on build systems and management of include paths when calling the compiler. (another completely random thought, no good place to put it: technically you don’t need forward declarations, it would just make debugging horrible).
* Rust
    * Rust modules do not require interface files, yet can be cyclic. This is possible because the Rust compiler compiles crates, rather than individual files. This allows the compiler to see all modules at once, thereby removing the need for interface files. Rust modules follow the codebase’s filesystem, though you can create submodules within files. Rust modules can be seen as analogous to C++ namespaces.
    * Rust crates are the units of compilation, which is generally composed of multiple Rust modules and files. This means that an entire crate needs to be recompiled even if only one file is touched. This is somewhat mitigated by incremental compilation, though there is a fundamental tradeoff at play here. Rust crates can be seen as analogous to C++20 modules.
    * Rust packages can hold multiple crates, often representing a full Rust project. Here, the overall structure of a Rust program is defined, such as the locations of the Rust crates, as well as the versions of the external libraries in use. Rust packages can be seen as analogous to C++ build systems, such as CMake.
* Go
    * Go packages are like Rust crates - no circular dependencies allowed. All files in a package can see each others’ definitions, and other packages can import to see the exported symbols. This shows that production languages don’t always need to have a circular module equivalent. To break circular dependencies, you can separate the implementation from the type by creating an interface and performing dependency injection (worth noting this adds a level of indirection through the v-table, so this may not be entirely viable in C).
    * Go modules are like Rust packages, collections of Go packages, and each module has a go.mod file describing dependencies with other modules. This also includes functionality such as versioning. Like go packages, they do not allow circular dependencies.
* Java
    * Java packages function similarly to C++ namespaces, in that they are a way of organizing related classes and interfaces. This follows the codebase’s file system (it might not be enforced by the compiler? Nonetheless, it is standard practice). I don’t believe you can define subpackages within a file (it’s one top-level class/interface per file)?
    * Java modules function similarly to C++20 modules, providing strong encapsulation but disallowing circular dependencies. They were introduced in Java 9.
    * pom.xml files and Maven can be thought of as whole program builders, providing functionality like versioning.
* Scala
    * Scala packages seem to be the same as Java packages, circular dependencies seem to be allowed. Apparently you can treat Scala packages like first-class citizens, similar to Ocaml? Dunno, this comparison list is getting too long anyways.
* Ocaml
    * Ocaml modules are typed, allowing multiple modules to satisfy the same signature. Like Rust modules, they follow the file system, but submodules can be defined within a file (note that Ocaml modules are defined with the `struct` keyword, though they are not C structures). The signature and module can be in separate files, and if the signature is not specified, everything in the module is considered public (need to verify this?). The power of Ocaml modules comes from their use in functors, allowing for functionality similar to C++ templates. This does mean that Ocaml modules are acyclic, though this is handled using a build dependency tool such as Dune.
    * (There is a bit of discourse I wish to expand upon [though isn’t directly related to modules technically since functors are mostly restricted to functional paradigms] concerning how every language needs to have some meta-programming or higher-order capability. C has macros, Cforall has forall, C++ has templates, Rust has macros, Go has generics, Java has generics, Python is interpreted so it has structural typing [also can modify itself]. Perhaps this relates to a checklist of things I find in any general purpose [if it’s domain-specific like Lua or Futhark some may not be necessary] programming language - version management (package manager), library building (ordered modules), namespaces (cyclic modules), structures (user defined types), type constructors (templates), metaprogramming (macros), functions. Then there’s functionality such as memory management, thread management, a standard library.)
* Python
    * Python modules are files, follow the file system, and you cannot create submodules within files. There are no interface files - instead, imports are performed by executing the target module. Circular dependencies are runtime errors, as the interpreter is trapped in an infinite cycle of imports. One solution is to import within a function call, though using imports in this manner is poor practice and can always be resolved by refactoring (proof?).

## By example (+ segue to next version)

Regular C:
```main.c
#include “book.h”
int main() {
	struct Book myBook;
	createBook(&myBook, "The Great Gatsby", "F. Scott Fitzgerald", 1925);
	displayBook(&myBook);
	return 0;
}
```
```book.h
#pragma once
struct Book { char title[100]; char author[100]; int year; };
void createBook(struct Book *book, const char *title, const char *author, int year);
void displayBook(const struct Book *book);
```
```book.c
#include <stdio.h>
#include <string.h>
#include “book.h”
void createBook(struct Book *book, const char *title, const char *author, int year) { /* … */ }
void displayBook(const struct Book *book) { /* … */ }
```

Now in CFA:
```main.cfa
import “book”;
int main() {
	struct Book myBook;
	createBook(&myBook, "The Great Gatsby", "F. Scott Fitzgerald", 1925);
	displayBook(&myBook);
	return 0;
}
```
```book.cfa
module;
import <stdio>;
import <string>;
export struct Book { char title[100]; char author[100]; int year; };
export void createBook(struct Book *book, const char *title, const char *author, int year) { /* … */ }
export void displayBook(const struct Book *book) { /* … */ }
```

I’m getting stuck with this idea of circular modules, it’s hard to make sense of it. Perhaps let’s start with .h/.c and allow forward decls and make timestamps and only acyclic modules, then expand from there. Peter wants me to consider looking at the benefits/feasibility of generating headers (+ maintaining correctness) and multipass compiler (- forward decls).