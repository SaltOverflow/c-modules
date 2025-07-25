<!--
V1 was rambly; in V2 we take a top-down conceptual view to try and reorient around shared concepts. I think it's a good reference for me, with notable annotations of further ideas to look into.
It lacks proper examples, so it's hard for others to understand, so V3 will be more walkthrough-esque.

What do we want
Grouping related symbols
Control over symbol visibility
Initialization order
Still feels like C
-->

# Modules proposal (v2, top-down conceptual)

## What do we want

Let’s analyze modules from a top-down view. What do we want in a C module?
1. **Grouping related symbols**: At the least, you want some way to group related symbols, because otherwise large programs have too many symbols to keep track of (symbols meaning things like types, functions and variables)
    1. **Control over symbol visibility**: Right now, all symbols are either static or extern, so you easily end up with lots of symbol clashes
2. **Initialization order**: Some things need to be set up before main(), and sometimes they need to happen in a certain order
3. **Still feels like C**: Using modules shouldn’t require rewriting entire codebases or force adopting a different paradigm

## Grouping related symbols

Grouping related symbols can be done in many ways: namespaces, files, static libraries, dynamic libraries, runtime lookup. Since Cforall is designed to work with existing C build processes (preprocess, compile, link using make) and needs to avoid requiring large-scale rewrites of existing C codebases, we use namespaces. Like C++ namespaces, this works by prefixing all symbols within a module. Unlike C++ namespaces, these modules do not need to be explicitly managed in the code. Simply declare at the top of a .c file that you’re working with a module, and the module system will handle applying the prefix to the rest of the file. Note this light form of encapsulation allows a developer to dive deep into the system and resolve symbol names in the assembly if necessary.

[[DECISION: Giving names to module prefixes, or using filenames? Note this is mostly an implementation detail]]
[[TODO: I haven’t decided if and how I would want to handle nested modules]]

import std as std;
with std;

std.cout;
std.algorithm.filter(…);

cout;
filter(); // error, not available for forall matching

[[TAXONOMY: See first sentence]]
[[DESIGN: Implementation inspiration from C++ namespaces, syntax inspiration from C++20 modules]]

## Control over symbol visibility

Control over symbol visibility gets closer to the core of why C translation units (C files after preprocessing), while having aspects of modules, isn’t generally considered a module. A programming language component, be it a for loop, type, function, struct, needs to have a well-defined set of semantics, ie. things you can do with it. A struct that can only be used if some arbitrary set of functions are called isn’t well-defined. However, this is pretty much how C translation units work, declaring functions that need to be resolved later by the linker. We argue that C translation units, with the right restrictions on use, can be considered a module. In our specification, within a module, all declarations are scoped to only symbols within the module. Accessing other modules would be done with an import mechanism, which behave the same way regardless of position in the file (unlike #include, which is textual inclusion). This allows giving modules well-defined semantics.

Taking some inspiration from C++20 modules, the main format of modules is a single file, rather than a .c/.h pair. This makes it easier to generate multiple versions of interfaces can be generated for different use-cases, since the responsibility is offloaded to the compiler to generate the headers. For example, the export mechanism can provide an optional tag, which means that only those that import the module while passing that specific tag will have that function in scope.

module thingy;
export(only_for_friend) int foo() { /*…*/ }
export int bar() { /*…*/ }

import thingy(only_for_friend);

int thingy$$foo() { /*…*/ }
int thingy$$bar() { /*…*/ }

int thingy$$bar();

#import “barheader.h”
int thingy$$foo();

#import “fooheader.h”

To account for special use-cases, and to ensure an easier transition to using modules, all module configurations should have an equivalent representation using only .c/.h files. This is a crucial step in ensuring not only well-defined semantics, but widespread adoption by newcomers. Another way we make modules even more flexible to migrate towards is by allowing modules to be defined across multiple translation units. These files would be “module parts,” with a single module file acting as the general interface of the module (similar to C++20 modules’ interface / implementation split). Note that a single interface module is necessary to enforce certain aspects of ordering and encapsulation.

module part asdf;
int foo() {}

module part asdf;
int bar() {}

module asdf;
export foo();
export bar();

[[Q: how would headers be changed?]]

As an example of problems that can be encountered when migrating existing codebases: the Make build system relies on timestamps, so generating header files can cause issues. To avoid this, the compiler will need to check if the generated header file is different before overwriting. Where generated header files are stored could be controlled using a command line parameter, perhaps defaulted to something like `.cforall_cache/generated_headers/<path to file>`.

*As an aside, many modern programming languages have a configuration file for listing external dependencies and versioning. While managing this is outside the scope of this project (requiring careful thought as to how it allows incremental development with existing build systems, or to replace them), having a configuration file could allow us to pass parameters to the compiler without resorting to managing command line arguments.*

[[DISCUSS: Tagged exports supplement the public interface, while prelude export is standalone]]
[[TODO: Discussion on module parts, migration importance]]
[[DECISION: Default generated header placement]]

## Initialization order

Initialization order can be achieved by having some modules be acyclic (call these “ordered modules”). These modules would be allowed to have an init and fini block, and their ordering comes from the ordered modules they import. For example, ordered modules that don’t import any ordered modules could have order `10`, and those that do would have order `10 + highest order module it imports`. The init block cannot (or should not, producing a silence-able error) use symbols from non-ordered modules, in order to prevent initialization order errors. A preinit block can also be defined for any execution module (ie. the one with the main() function), which is used to allow certain modules to run prior to any of the other init blocks. This is useful in certain cases, such as overriding the standard library memory allocator.

Ordered modules restrict codebase design, which may be undesirable for most use-cases. As such, most modules are “cyclic modules”, being allowed to mutually import each other. This is in line with the standard .c/.h structure in existing C codebases. However, this presents a problem: if modules are defined in a single file, we cannot export the interface without first importing modules, which is not possible due to an import cycle. Resolving this fundamental problem requires generating a header before entering such an import cycle. This can be done by augmenting one of the modules in an import cycle with a “prelude” section. The prelude section would export any necessary symbols, and would be fully defined before importing any modules that would cause an import cycle. Any importing modules that would otherwise complete an import cycle would import the prelude instead, thus breaking the cycle. The declarations within the prelude could then be checked for existence by fully processing the module and confirming the exported symbols do in fact have implementations.

module qwer;
import tyui;
import asdf(prelude); // prelude is a special keyword here
export void foo(); // this is actually asdf$$foo()
export void bar() {}

module asdf;
export prelude {
	void foo();
}
import qwer;
export foobar();
export foo() {bar();}

*To highlight the issues of not allowing cyclic dependencies: C++20 modules act like libraries, which affects the build / link process. While it is an idealized system, it requires fundamentally altering the codebase and build process. This may be the reason that in 2025, there is still no major C++ compiler that fully supports C++20 modules. Instead, we would prefer if it were possible to continue using the same build system as before, while providing the option to transition to a “library format” as the language and codebase evolves. This also comes back to the Cforall motto: “describe not prescribe,” meaning that a language feature should not force a certain way of doing things.*

[[DISCUSS: How would overwriting standard library implementations actually work? eg. thread local layout]]
[[NOTE: The post-prelude check needs to find the actual implementation, or it may simply find the original exported prelude symbol]]

[[THINK: How hard would it be to automatically refactor a C project to use modules? What about how it maps to a C++ or C++20 modules project? Perhaps we can try doing by hand on an existing codebase]]

## Still feels like C

Still feels like C, as highlighted above, turns out to be a fairly tight restriction. Instead of the conventional wisdom of stricter encapsulation, our modules use namespace prefixing. This is because we do not wish to force a change in the build process and we want to give the developer a deeper understanding of the internals of modules. Due to our careful design, C modules need only minor changes to existing files in a codebase, allowing .h/.c and module part representations if necessary. Crucially, we will be able to support cyclic modules, so existing codebases need not require rearchitecting. Note that significant work in the compiler will need to be done in order to support these features, especially in updating the existing error diagnostics to aid in developer understanding.

One very unfortunate reality of the C workflow is that modules cannot export macros. This is because the preprocessor runs before the compiler, and an ethos of Cforall is to avoid requiring changes to a workflow (at least, without really good reason). If macros are needed, preprocessor directives like #include would need to be used. A potential alternative could be to use a directive like `#pragma include`, but this would likely cause problems with cyclic modules. Instead of this, we will try and provide enough powerful language features that the use of C macros is rare.

[[TODO: Haven’t discussed how the modules could help define static libraries, dynamic libraries, different build models, despite having a simplistic design]]
[[NOTE: Necessary work on error diagnostics needed]]

[[IDEA: constexpr, special macro-like variables that have guaranteed inlining, interactions with thread local]]
[[IDEA: Other language ideas, such as implicit method generation from standard function overloading, automatic v-table generation like Rust, …]]
