# Adding modules to C: why do we need modules?

*This is part of a series where I present my Masters research, in a format that is more approachable than the structured layout of a thesis.*

C is a peculiar language in that it's the backbone of most of the world's code, but it's a pain to develop in because it lacks many modern language features. As such, developers tend to avoid working in C unless they have to. In this work, I aim to address what I consider to be the largest problem with C: its lack of modules.

## What does a module system provide?

To understand why C's lack of modules is such a problem, we first need to define what features a module system provides. There are two main features: the ability to share symbol references across files (interfile scope) and preventing symbol names which are defined in different modules from interfering with each other (name isolation). In other words: in its simplest form, it manages symbol references across a codebase.

This may not sound like much, but when you scale up to a codebase with millions of lines of code, how you manage symbol references has a huge impact on what kinds of analysis, optimizations and guarantees you can rely on. Suppose you wanted to see if making a function inline would improve performance. With the right module system, this could be as simple as adding one inline keyword and recompiling.

## How does C fall short?

How does C fit into all this? C has header files and symbol declarations, which works like an ad-hoc version of modules where you write declarations and header files to manually add the links that a module system should be doing for you. This design decision likely comes from an era when computer memory was scarce, so a compiler could not parse multiple source files simultaneously.

So in terms of the two main features (interfile scope and name isolation), C requires developers to manually manage interfile scope and does not provide any name isolation. The additional header files essentially double the number of files in a codebase while also introducing potential dependencies on the order of `#include` statements. As an example:

```
// a.h
#pragma once
struct S foo();

// b.h
#pragma once
struct S { int i, j; };

// a.c
#include "b.h"
#include "a.h"
...
```

If the order of `#include` statements changes, a compilation error is thrown. It can be argued that the developer should notice that `a.h` needs to have `#include "b.h"`, but implicit dependencies on `#include` order happen frequently in practice, which indicates a deficiency in the language.

## Module design: cyclic vs acyclic modules

In addition to the two main features of a module system (interfile scope and name isolation), we introduce another constraint: **.c/.h files have an equivalent modular representation** (or as much as possible). In other words, every reasonably written .c/.h file pair should be representable as a module file, and every module file should be representable with .c and .h files. Not only would this make the module system familiar to C developers, it also opens the possibility of automating the migration process, which would greatly accelerate adoption.

This constraint motivates the requirement for cyclic modules (ie. whether cyclic imports are allowed) To provide an example:

```
// Node.c
struct Edge;
struct Node {
  struct Edge **edges;
};

// Edge.c
struct Node;
struct Edge {
  struct Node *nodes[2];
};
```

We want each .h/.c file to be equivalent to a module file, which would put Node and Edge into separate modules. This means that each module needs to import each other, so we need to support cyclic modules.

It's worth mentioning that there are existing implementations of C modules, both in academic papers and open source. A notable example is C++20 modules. However, they all seem to use acyclic modules. While this is easier to implement and makes analysis easier (especially initialization order), it is challenging to refactor existing C codebases to the acyclic module format, which likely contributes to its poor rate of adoption.

### Making cyclic modules work

To make cyclic modules work, we need to extract a module interface (which can be as simple as a list of top-level symbol names) without consulting other files or the symbol table. We then combine the module interfaces of the imports together to create a rough symbol table, which is used to figure out context-sensitive issues (ie. whether a symbol is a type or not).

The extraction of top-level symbol names should be possible, because expressions are not allowed at top-level in C. For example, `A *b;` is always a variable definition at top-level. In fact, if "implicit int return type" is not supported, the first identifier of a top-level statement can be assumed to be a type name (excluding special names like `static_assert`).

## Other challenges with C modules

There are additional challenges to consider when building modules for C, which come from the unique position that C is in: a systems programming language with a lot of legacy code.

### Systems programming

Systems programming is characterized by needing precise control over how code is run. One example is unboxed types: If I have `struct S { int i; struct S1 s1; } s;`, then the compiler needs to know the definition of `struct S1` in order to use `s`. Another example is inline functions: If I have `inline int foo() { return 5; }`, I expect that `-O2` will elide the function call. What this means is that our module system often needs to expose the definitions of symbols to the compiler, despite other languages not needing to.

To elaborate on this, consider Java and Go. Both languages use boxed types and virtual method tables to avoid exposing implementation details (Cue the fundamental theorem of software engineering: "any problem in computer science can be solved with another level of indirection"). Go takes this one step further and only has acyclic modules, which is possible because the Node/Edge example above can be refactored into NodeInterface/EdgeInterface.

Due to the requirements of systems programming, we cannot rely on indirection unless the developer explicitly asks for it. That being said, we can still limit the logical scope of symbols, even if we need to expose information to the compiler. In the example above, if a module imports `struct S` but not `struct S1`, writing `struct S1 ss;` should be disallowed, even though the compiler is technically given the definition of `struct S1`.

### Migrating legacy code

There exists so much C code already in production systems that I would argue that most work in C nowadays is in maintaining existing systems rather than building new projects. As such, a key consideration with our module system is how an existing C codebase would migrate to use modules.

As such, we need to handle interactions between modules, .c/.h files and assembly. We also want to consider intermediate migration states and automated migration tools.

Let's consider modules calling into .c/.h or assembly. If we have name isolation for modules, that means we add the module name to the suffix of symbol names (reusing the ABI of C++20 modules). However, we don't want the module suffix to be added to these `#include` header files. To handle this, we can reuse the "global module fragment" design from C++20 modules, which sets aside some area of the module file for this purpose.

Having .c/.h call into modules involves importing said module, so the compiler may have to call into the module system to do some work. As for assembly calling into modules, we would want a way to disable name isolation (eg. `extern "C"`).

Now consider an intermediate migration state where we want to export some symbols, but only to a subset of modules? We could do it like friend classes, but we can get more control using something I call "tagged exports": `export(special) struct S *expose_runtime();` is not imported with `import M;`, but it is with `import M(special);` (I haven't seen this done before, so I'm claiming this as my idea for now). We could also provide an annotation that allows us to break name isolation (eg. `[[module(M)]] struct S *expose_runtime();`), which could be useful for debugging purposes.

We've created a pretty full-featured module system at this point, but a migration is still unlikely to be done on a codebase in the maintenance phase of its life. We need to consider tools that automate a significant portion of the migration work. Think of a tool that would automatically convert a header file into a module interface. Or a tool to generate a header file from modules, for backwards compatibility. Or the holy grail: fully automated migration to modules for an entire C codebase. I believe all of this can be done, if only we spent more time on these problems.

## To be continued

This establishes what functionality we want our modules to have, as well as a reasonable understanding that this is feasible. To recap: we want our module system to handle interfile scope and name isolation, and do so in a way that makes the module representation very close to what we would otherwise write using .c/.h files. This leads us to require supporting cyclic modules. Furthermore, the systems programming paradigm and migration considerations means that we need to carefully consider scoping rules and interactions between modules and native code.

In the next article, we will take a closer look at a more concrete proposal, which will dive deeper into the details of implementation. Furthermore, I will show an actual implemention that provides much of the functionality we're after.
