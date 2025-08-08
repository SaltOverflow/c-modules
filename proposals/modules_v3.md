<!--
Motivation and goal section are really good imo. The rest of it spiraled out of control, because I started writing simple example section without seeing the end (it's all interconnected). Disliked the export syntax for generating headers, but maybe this can be solved by strong module theory in v4. Ordered modules is also messy and should probably be considered only after figuring out the other stuff (the static init double-write case is interesting but kind of degenerate).

Motivation
Goal
Strategy
Simple example (acyclic, non-transitive, using .c/.h files)
Generating headers
Handling circular modules
Ordered modules
Nested modules
-->

# Modules proposal (v3, walkthrough)

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

*note: this section was written after the rest of the document*

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

**There are two general types of modules: cyclic and complete**, which vary in whether their imported modules need to be fully defined first. Cyclic modules work like namespaces, being referenceable before they’re compiled/interpreted. Complete modules create a topological ordering of definitions, with examples such as Ocaml modules, Go packages, or Python modules. We will revisit complete modules when discussing initialization order, but cyclic modules best represent C translation units (declarations are incomplete references that need to be resolved later by the linker).

With that in mind, let’s try bundling a, b, c into separate namespaces:

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

These modules work similarly to C++ namespaces, except that #include automatically opens the namespace into the current namespace. Namespaces work by prepending the namespace name to the front of any defined symbols (eg. `module a { void abba(); }` becomes `void a$$abba();` ). Using namespaces to implement our modules allows us to avoid changing the build system (eg. Makefile), as linker symbol resolution can continue working the same way. We do need some mechanism to ensure two modules use the same name, though.

A couple problems with this iteration:
* Having to type `module a { /* all definitions in file */ }` is tedious and error-prone (need to remember what’s inside/outside brackets).
* If modules are essentially namespaces, where’s the “access control” (ie. stopping other modules from peering into the current one) ?

For the first point, we can use a single declaration at the top of the .c file, and have the compiler assume all remaining declarations / definitions are part of the module. Headers are more problematic: the preprocessor handles #include , and the compiler sees the contents of the header *as if it was always a part of the original file*. So full brackets are still needed for headers, though we could use a #pragma (eg. `#pragma module a` is equivalent to `module a { /* rest of file */ }` ).

For the second point, we can put a check right before calling the linker to ensure module names do not clash. An option to avoid the module naming problem is by having the module name be the file path. This could be taken relative to where the compiler is called from, or based off of a configuration file. Considerations would need to be made for different codebase structures (eg. `src/headers/path/to/a.h` is the header file for `src/path/to/a.c` ). At the current stage of compiler development, I feel like this could lead to issues with module extensibility (eg. header only modules, modules that span multiple translation units, nested modules, renaming modules), so I’ll get back to this idea when discussing how to nest modules.

```
// a.h
#pragma module a
void abba();
// a.c
module a;  // #pragma module a could also work here
void abba() {}

// b.h
#pragma module b
void bass();
// b.c
module b;
#include “a.h”
void bass() { abba(); abba(); abba(); }

//  c.h
#pragma module c
void cash();
// c.c
module c;
void cash() {}
void cs() {}

// main.c
#include “b.h”
#include “c.h”
int main() { bass(); cash(); }
```

There’s actually a bug in `b.c` : `#include` is just textual inclusion, so the compiler would see `module b { module a { void abba(); } }` . Some solutions:
* Treat nested modules as actually top-level (causes problems when adding nested modules in the future)
* Move the `module b;` declaration after the #include (unintuitive)
* Add an import keyword (a few caveats to consider)

There’s also another issue to consider: When importing, do we really want to automatically open the namespace? What if you want to keep it closed? The third point is the only one that adequately handles this. Let’s see how:

When importing a module header, we can do this:
```
import {
	#include “a.h”
};
```
We can also put multiple of them in an import block:
```nc
import {
	#include “b.h”
	#include “c.h”
};
```
By default the modules are not expanded into the current scope (otherwise it causes problems with nested modules). If we want to expand into the current scope, we “dereference”:
```
import *{
	#include “b.h”
	#include “c.h”
};
```
This would be equivalent to:
```
import {
	#include “b.h”
	#include “c.h”
};
with b;
with c;
```
If you don’t have macros defined, you can skip the brackets (macros are evaluated before the compiler runs, exporting them causes many ordering issues):
```
import “a.h”;
import *”b.h”, “c.h”;  // Note this doesn’t expand module c into the current scope
```
Imports can also rename the imported module in the current scope (could be useful when importing a non-module header):
```
import “a.h” as aa;  // aa.abba();
import {
	#include “a.h”
} as aaa;  // aaa.a.abba();
import *{
	#include “a.h”
} as aaaa;  // aaaa.abba();
import {
	#include “b.h”
	#include “c.h”
} as abc;  // abc.b.bass(); abc.c.cash(); abc.c.cs();
```

Now we can update the example:
```
// a.h
#pragma module a
void abba();
// a.c
module a;  // #pragma module a could also work here
void abba() {}

// b.h
#pragma module b
void bass();
// b.c
module b;
import *“a.h”;
void bass() { abba(); abba(); abba(); }

//  c.h
#pragma module c
void cash();
// c.c
module c;
void cash() {}
void cs() {}

// main.c
import *“b.h”;
import *“c.h”;
int main() { bass(); cash(); }
```
Compare with the original code:
```
// a.h
void abba();
// a.c
void abba() {}

// b.h
void bass();
// b.c
#include “a.h”
void bass() { abba(); abba(); abba(); }

//  c.h
void cash();
// c.c
void cash() {}
void cs() {}

// main.c
#include “b.h”
#include “c.h”
int main() { bass(); cash(); }
```
Pretty good!

[[
After finishing writing this version, I found that there are issues with exporting another module under the current module (ie. `export import`). In the example below, it looks like there are 5 different versions of module a, even though they're the same. Even if we implement these "copies of module a" as virtual modules (they actually point to the real module a), it'd be confusing to have `struct d.b.a.S value = d.b.get_value();` and `struct d.c.a.S value = d.b.get_value();` mean the same thing.
```
module a {
	struct S {};
}

module b {
	module a {
		struct S {};
	}
	struct S get_value();
}

module c {
	module a {
		struct S {};
	}
	void use_S(struct S);
}

module d {
	module b {
		module a {
			struct S {};
		}
		struct S get_value();
	}
	module c {
		module a {
			struct S {};
		}
		void use_S(struct S);
	}
	void do_something() {
		
		use_S(get_value());	}
}
```
C translation units are singletons rather than instances, so C modules should be too. As such, I now believe the first strategy for interpreting modules is the better one: Treat nested modules as actually top-level.
]]

## Generating headers

Let’s take this to the next level. The header files are somewhat redundant, and most modern languages do away with them. By letting the compiler handle generating headers, we’ll also be able to generate multiple headers for a single file, thereby improving encapsulation. Let’s take the previous example and make it work:

```
// a.c
module a;
export void abba() {}

// b.c
module b;
import *“a”;
export void bass() { abba(); abba(); abba(); }

// c.c
module c;
export void cash() {}
void cs() {}

// main.c
import *“b”;
import *“c”;
int main() { bass(); cash(); }
```

The `.h` suffix on import file names has been removed for brevity here, since the generated header is stored somewhere else, possibly in precompiled form. The generated headers can be output directly into the working directory, or stored somewhere else (eg. using a command line parameter).

Here is a list of the different ways to export:
```
// functions
export void f() {}  // void f();
export inline void ff() {}  // inline void ff() {}
export f;  // void f();
export *f;  // error: cannot export definition of non-inline function f
export ff;  // void ff();
export *ff;  // inline void ff() {}

// types
export struct S {};  // struct S {};
export struct S;  // struct S;
export typedef Integer int;  // typedef Integer int;
export S;  // struct S;
export *S;  // struct S {};
export Integer;  // error: cannot export declaration of typedef, needs to be definition
export *Integer;  // typedef Integer int;

// variables
export int a = 4;  // int a;
export a;  // int a;
export *a;  // error: variable declarations are exported, not definitions

// forall
export forall {…}  // forall {…}
mallocs: forall {…}
export mallocs;  // error: cannot export declaration of a forall, needs to be definition
export *mallocs;  // forall {…}

// imports
export import “a”;  // exports all definitions/declarations that are exported in a, as if it were a nested module
export import *“b”;  // exports all definitions/declarations that are exported in b, as if they were defined within the module
import “c” as cc;
export cc;  // exports all definitions/declarations that are exported in c, as if it were a nested module defined as cc
export *cc;  // exports all definitions/declarations that are exported in c, as if they were defined within the module
```
So function definitions are exported as declarations, unless they are inline. Types are generally exported as definitions, variables declarations, forall definitions. There is also syntax for exporting definitions or declarations, though note that it must be done after the symbol’s definition.

**I’ll admit I’m not very satisfied with this specification of single-file modules**. Not only because having to know declaration vs definition is tedious, but also because module exporting doesn’t really even follow it (`export cc;` would be “declare an empty module called cc” under the rigorous specification).

Another challenge is the fact that C uses unboxed types. If we `export Card getCard(Person *);` , even if the programmer doesn’t need to see the details, the compiler needs the definition of `Card` and the declaration of `Person` . Also, in the definition of `Card` , there can be other structs that need to be exported too, and so on. Here we have a decision on whether the developer should explicitly export the full chain of definitions/declarations, or the compiler can automatically export those details. And if they are automatically exported, are they always visible to the importer (eg. if a type is used only within the definition of an inline function) ? This may require adding a private/protected mechanism, of which there is no analogue in C (complicating the “every module has a .c/.h equivalent”).

There is also something else to talk about: having the compiler generate headers allows us to generate different headers for different importers. Suppose you have a module with some functions that are only meant to be called by a few special modules:
```
// mod.c
module mod;
void not_for_others() {…}
export void for_everyone() {…}
export(special) void for_special_modules() {…}
```
This ends up being equivalent to:
```
// mod.h
#pragma module mod
void for_everyone();
// mod__special.h
#pragma module mod
import “mod.h”;
void for_special_modules();
// mod.c
module mod;
void not_for_others() {…}
void for_everyone() {…}
void for_special_modules() {…}
```
And importers can use the special version with `import “mod”(special);` .

This helps provide an alternative to friend modules. Note that the special interface includes public interface, in order to cut down on complexity.

## Handling circular modules

One aspect of linking C translation units is that multiple translation units can reference each other. To use the classic example:

```
// node.h
struct Edge;
struct Node {
	Edge **edges;
};
// edge.h
struct Node;
struct Edge {
	Node **nodes;
};

// graph.h
#include “node.h”
#include “edge.h”
void displayGraph(Node*);
void displayGraph(Edge*);
// graph.c
#include “graph.h”
void displayGraph(Node* nodes) {…}
void displayGraph(Edge* edges) {…}
```

Here, node.h is referencing something in edge.h, and vice versa. But we can’t have modules peering into the internals of each other! As such, a modular specification could be:

```
// node__prelude.h
#pragma module node
struct Node;
// node.h
#pragma module node
import “edge”(prelude);
struct Node {
	Edge **edges;
};
// edge__prelude.h
#pragma module edge
struct Edge;
// edge.h
#pragma module edge
import “node”(prelude);
struct Edge {
	Node **nodes;
};

// graph.h
#pragma module graph
import “node”, “edge”;
void displayGraph(Node*);
void displayGraph(Edge*);
// graph.c
module graph;
import “graph”;
void displayGraph(Node* nodes) {…}
void displayGraph(Edge* edges) {…}
```

Now, how would one represent this with single-file modules?

```
// node.c
module node;
import “edge”;
export struct Node {
	Edge **edges;
};
// edge.c
module edge;
import “node”;
export struct Edge {
	Node **nodes;
};
// graph.c
module graph;
import “node”, “edge”;
void displayGraph(Edge*);  // needed because mutually recursive
export void displayGraph(Node* nodes) {…}
export void displayGraph(Edge* edges) {…}
```

There’s a problem here: In order to generate the header for node.c, we need to analyze node.c, which requires generating the header for edge.c, which ends up circling back to node.c . In this case, it’s relatively straightforward to see what’s going on, but in the general case, it can require complex fix-point analysis which is inefficient and hard to debug (if it is even possible to do). To break this loop, what we’d want is to have some way to generate a header before entering this circular dependency of imports. Let’s see how that changes things:

```
// node.c
module node;
export(prelude) final {
	struct Node;
}
import “edge”(prelude);
export struct Node {
	Edge **edges;
};
// edge.c
module edge;
export(prelude) final {
	struct Edge;
}
import “node”;
export struct Edge {
	Node **nodes;
};
// graph.c
module graph;
import “node”, “edge”;
void displayGraph(Edge*);  // needed because mutually recursive
export void displayGraph(Node* nodes) {…}
export void displayGraph(Edge* edges) {…}
```

What export final does is immediately generate a header from the contents of the block, instead of waiting until the end to produce the final header. This has some special semantics, in that this generated header does not include the public interface. In essence, it works like a “header file within the module file”, with the caveat that anything defined within it is visible to the rest of the file.

## Ordered modules

Some modules have initialization and destructor functions, which may need to run before other initializers. These modules would work like this:

```
// a.c
ordered module a;
int foo();  // need to forward declare because definitions are not hoisted (maybe they could?)
init {
	export int a = foo();
}
fini {
	a = 10;
}
int foo() {…}
// b.c
ordered module b;
import “a”;
init {
	export int b = a.a;
}
fini {
	b = a.a;  // note this runs before a.c’s fini
}
```

The ordering of the blocks comes from the ordered modules they import. For example, ordered modules that don’t import any ordered modules could have order `10`, and those that do would have order `10 + highest order module it imports`. The init block cannot (or should not, producing a silence-able error) use symbols from non-ordered modules, in order to prevent initialization order errors.

~~A preinit block can also be defined for any execution module (ie. the one with the main() function), which is used to allow certain modules to run prior to any of the other init blocks. This is useful in certain cases, such as overriding the standard library memory allocator.~~ *I’m unsure how I’d want to set this up, I feel like preinit modules are a completely separate entity that should not be attached to something like an “execution module”.*

## Nested modules

Some aspects of nested modules have already kind of been discussed in the previous discussions, but we’ll take a closer look here. Let’s consider the Cforall equivalent of std.algorithm. You could specify the module using `module std.algorithm;` , but with the current setup, if `module std;` does `export import “std/algorithm”;` , that would actually be exporting `std.std.algorithm` . Perhaps we only grab the last module name out of the chain, but then why specify `module std.algorithm;` instead of `module algorithm;` ?

A reason for specifying `module std.algorithm;` instead of `module algorithm;` is because it’s used as the namespace prefix, so we can’t conflict during linking. Let’s revisit the idea of using the filepath as the prefix instead. If a module exports a symbol that was defined by a different module, then any importers see it as if it came from that module. So the namespace prefix that the linker sees is not actually related to the logical imports in the language - it’s only there to make sure you don’t have symbol name clashes.

If you use the filename prefix as the namespace prefix of the module, then modules can have the same name without any issues. It doesn’t mean they can interchange with each other (C programs can be tightly interlinked because you avoid boxing), but it means you avoid name clash issues.

And just as an extra note: you could have modules that span multiple files. Each file keeps the .c/.h split, except at the top you say `module part “abc/foo”;` , then in abc/foo.c you have `module foo;` , which serves as the single interface file for aspects such as ordered modules. In this setup, you can import a module part instead of going to the main interface file - it just grabs the header file.

*Anyways, there's enough problems with this design that I think we can try again with more insight. Onto iteration v4.*
