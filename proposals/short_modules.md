# C modules

We want to implement these abilities:
* Implementing C modules
* Wrap existing C libraries into modules
* Migrate C files into modules

## Implementing C modules

* Core principles (guides what we can do)
* Algorithm
* Future features
* Alternative approaches

More details can be found in `modules_v5.md` - this doc is meant to only have the bare essentials.

### Core principles

* .c/.h files have an equivalent modular representation (can be converted in both ways, so retains developer patterns)
* The modular representation has each symbol definition control its visibility (if some information needs to be leaked, minimize it)
* Import order does not matter (enables precompiled header optimizations)
* Avoid symbol name clashes between modules
* Module system handles fetching symbols (`import` handles details such as boxed/unboxed types, regular/inline functions)

### Algorithm

Module format:
* Assume modules only supports some builtin types, `struct`, pointers, functions, globals (no macros, include, const, arrays, forward declarations)
* Introduce keywords: `module` (a module has `module;` as first statement), `import` (like `#include`, use `import "sys/wait";`), `export` (first qualifier of a type, function, global)

Module requirements:
* Every module file can be parsed to extract top-level symbols and struct fields, without context-sensitive grammar problems (needed in order to examine what other modules export)
* There is a mechanism to go from import statement to a module
* ~~Every module has a unique and consistent identifier (used to prefix top-level symbols, to avoid name clashes)~~ (ignore for now)

Algorithm steps (given a single module file):
* Extract list of imported modules
* For each imported module:
    * Extract and output any exported `struct` definitions, function and global declarations (output in file order)
    * These may use imported types too, so extract list of imported modules:
        * Analyze and output any matching types (these are output above the imported module). Choose between type declarations and definitions
        * If we need a type definition, we keep recursing. Check for loops (revisiting the same module is ok, but revisitng the same type definition is not)
* This may result in duplicate type definitions, so deduplicate by keeping the first output
* Remove `export` keywords from the module file, then output
* The output is fed into a C compiler

# Scratch space

The algorithm is essentially broken up into a partial parse (parse module by itself, get list of defns, uses, imports), followed by a combining phase (for each module, unresolved uses make us scan all imports), followed by a dedup phase (removing duplicate definitions before sending to C compiler).

Context-sensitivity can make analyzing uses challenging (whether an identifier is a type or a variable can influence the code structure). Some examples include: angle brackets <>, dot operator ., dereference operator (a)*b, parentheses after identifiers int().

Context-sensitivity could be handled by not having the module system get the uses. Instead, use the rest of the compiler to disambiguate uses.
