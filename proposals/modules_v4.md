<!--
WIP
-->

# Modules proposal (v4, walkthrough with strong modules)

## Motivation

Let's walk through the design process of making a C module system.

First things first: **Why do we need modules?** From a theoretical standpoint, it's superfluous - a module system restricts your creative freedom because it makes you think that organizing code and organizing data is different, even though they use the same concepts. However, in practical scenarios it's useful to have a module system because we care about building things fast, reliably, and spread across multiple teams with varying skill levels. **We want modules because it helps us focus on only the parts of the program we're working on.**

But **isn't a C translation unit a module?** *(a c translation unit is a `.c` file after preprocessing)* It has `static` and `extern`, but there isn't a good way to analyze which symbols are used where in the program. A symbol defined in `foo.c` can be declared in `foo.h`, but there's nothing preventing an arbitrary file from declaring it too. Calling a C translation unit a module is like saying a struct is well-defined, even if it can only be used if some arbitrary set of functions is called. We don't consider it a module because its `extern` contents bleed out into the rest of the program - you can't easily analyze which modules use its contents because all of them can. **We argue that C translation units, with some access control, can be considered a module.**

## Goal

Let's first clarify what we're trying to achieve with our modules. The term "module" is as abused as "polymorphism" in programming languages, which makes it challenging to determine what we're working towards with a module system for C. Let's start:

* **Make C translation units into modules** (needs some access control on `extern`)
* **Generate headers** (so .h files are not necessary, though they can still be used)
* **Each feature is incremental** (each part of the module system requires minimal changes to existing C code - features should feel like optional, simple syntactic sugar)

Put simply, we want to require minimal changes (source code, makefile, programmer thought process, compiler implementation), while building something similar to Rust modules. There are other aspects of modules that we'll want to cover - modules defined across multiple files, modules nested within a file, module friendship - which have their various solutions, but we'll get to them after working with these main 3 goals.

## Strategy

From [this article](https://thunderseethe.dev/posts/whats-in-a-module/) (more specifically, [Backpack in Haskell](https://plv.mpi-sws.org/backpack/)), we are introduced to this concept of **weak and strong modules**. A weak module is tied to its dependencies, meaning that swapping out a dependent module for another requires recompilation. Contrast this with a strong module, where we can provide the dependent modules after the module has been compiled. *[[note this doesn't deal with initialization orders, that's separate]]*

For our purposes, the difference is thus: **weak modules are dependent on other modules, while strong modules are dependent on module interfaces.** Given that header files can act as a module interface, and we are intending to generate headers, this works in our favour. Let's see how:
* A module is a collection of definitions. We want to restrict the module interface to only the key details that an importer should know. There are 3 kinds of definitions in C to consider: variables, functions, types.
    * Variables and functions export their declarations. Types need to export their definitions, so importers can access their fields.
    * Variables and functions can use types not defined in their module. To avoid needing to expose other modules' contents (which creates unwanted transitive dependencies), the importer will receive a "shell" of that type - name, parent module, size, alignment. This allows callers of imported functions to allocate the appropriate space on the stack. If field information is necessary the importing module would also import the module containing the type.
* First, a module needs to be scanned at the top-level to extract the "shells" of its types. To calculate the sizes, this can require recursively searching through all imports. To handle circular imports, this may require partial parsing and fixpoint analysis, which requires top-level declarations to use a context-free grammar. At the end of this pass, a **type declaration header** is produced for the module, which contains a "shell" for every type it defines. *[[unsure, also typedecls may need to have a separate header than structs]]*
* Second, the module is parsed to collect all exported symbols, called the **export header**. If a symbol uses a type that isn't part of the module, the appropriate type declaration header is exported too. *[[doesn't the typedecl header potentially create too many unnecessary dependencies?]]* At the same time, we can also collect all top-level declarations, which can be used in the next phase to avoid needing forward declarations within modules.
* Third, the module can generate its **implementation file**, which imports any necessary headers, forward declares all top-level declarations, then all definitions in the module (can skip those already defined in export header). Alternatively, we can go straight to compiling the object file.
* Once headers are generated, they are not meant to change frequently. This way, when a module is updated, we can recompile it using the generated headers, without needing to check the actual modules. If we wish to update the headers, we invoke a command to do so, repeating the first and second steps (skipping modules that have not changed).
* To keep track of which modules are connected to which, we can have a central module file which controls which modules are bound to which headers (ie. module interfaces). This would essentially function similar to a Makefile, but aware of the fine-grained details of symbol exports. *[[this can get very complex, dealing with details such as static/dynamic libraries, distributed builds, unity/release builds, and interfacing with codegen such as parser generators]]*

*[[Simplify the explanation down to: separating the weak modules part (generating headers) from the strong modules part (compilation)]]*

*[[to be continued with more concrete implementation examples]]*



## Simple example (acyclic, non-transitive, using .c/.h files)

Let’s look at some code:

```
// a.h
void abba();
// a.c
void abba() {}

// b.h
void bass();
// b.c
#include "a.h"
void bass() { abba(); abba(); abba(); }

//  c.h
void cash();
// c.c
void cash() {}
void cs() {}

// main.c
#include "b.h"
#include "c.h"
int main() { bass(); cash(); }
```

Looking at this, it looks like a, b, c work like modules. However, what if `a.h` defines `void cs();` ? What if `b.h` defines `void cash();` and `c.h` doesn't? The language allows any translation unit to pull in any symbol from anywhere, and `#include` is textual inclusion, so **the idea of `.c/.h` being a module is an illusion - it's not enforced by C.**

We want each module to have control over what it exports to others, which means we need to know which symbol belongs to which module. We'll achieve this by bundling a, b, c into separate namespaces:

```
// a.h
module a { void abba(); }
// a.c
module a { void abba() {} }

// b.h
module b { void bass(); }
// b.c
#include "a.h"
module b { void bass() { abba(); abba(); abba(); } }

//  c.h
module c { void cash(); }
// c.c
module c {
	void cash() {}
	void cs() {}
}

// main.c
#include "b.h"
#include "c.h"
int main() { bass(); cash(); }
```

A couple of things to consider/update with this iteration:
* Explicitly naming the modules or implicitly using the file path?
    * C++ namespaces and Java packages have some redundancy in that their names repeat the file path somewhat, but this can offer some flexibility in code organization
* `module a { ... }` or `module a; ...` ?
    * The first is tedious/verbose, the second applies to everything, which can lead to some unexpected semantics
    * eg. The `module b { module a { void abba(); } }` problem
* Does `#include` automatically open the namespace ?
    * Automatically opening is backwards compatible, but throws away a lot of control. If we keep it closed, there are a number of design options to choose from
    * eg. Treat like namespaces, try to encapsulate, module aliases
* How do we control modules from having the same name?
    * The most obvious way is to have a step right before the linker. Other options include static analysis, module renaming, whole program analysis

// working on rewriting this section

// I'll need to address the transitive problems somewhere
// This may have some relations to nested modules

// Cyclic is a problem when dealing with single-file modules
// Single-file modules also ask the question: how should export work?

// THEN we need to figure out 

**There are two general types of modules: cyclic and complete,** which vary in whether their imported modules need to be fully processed first.
* With cyclic modules, an imported module needs to describe how to access its symbols without needing to be fully processed itself. Some systems do a shallow parsing of a file (eg. Java classes, Rust modules), some have separate files for interface and implementation (eg. C header files). This can allow development to adopt a more flexible code structure, though aspects such as initialization order and readability can be a problem.
* With complete modules, you create a topological ordering of when modules need to be processed. This is often necessary if you want to operate on a module, like with Ocaml or Python modules. The ordering can also be useful for initialization order and readability, like with Go packages. It can be problematic for certain projects which are inherently cyclic, however.

I introduce this concept because while many aspects of C translation units are cyclic (eg. C header files, declarations), other aspects we wish to support are not (eg. inline and struct definitions need implementation details, initialization requires ordering). For now, we have a simple example, but it's worth peeking ahead at potential issues.

