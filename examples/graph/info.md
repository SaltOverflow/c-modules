Features:
* Struct, function (no inline), variables
    * The only definition we need to handle exporting here is struct. typedef, traits, forall, inline functions, we'll look into those later
    * Also no `export import` (ie. modules that export other module's contents automatically)
* int, int*, const int
    * No extra built-in types considered here
* No `#include`
    * No manual control over headers demonstrated in example, everything handled in `module`, `import`, `export`
* No forward decls
    * All definitions within modules, with declarations automatically hoisted to the top
    * Note: this requires top-level declarations to be context-free

Stylistic choices:
* `module;` doesn't specify a namespace (prefix with file path)
* folder files like `graph.cfa` are outside their folders (simplifies the import file discovery algorithm)
* `import` uses no quotes/angle brackets (unlike `#include`)
* `import` automatically opens the namespace (keeping it closed can be tricky with transitive dependencies)
* `stdio` and other standard C libraries have `import` versions
* `main.cfa` is not a module (avoid module namespacing interfering with `main()` symbol discovery)

Step-by-step:
* `0_initial` is the code that is written by the developer
    * Note how modules seem to have circular dependencies (eg. `graph/node.c` imports `graph/edge.c` and vice versa)
    * Top-level declarations within modules can also be declared out-of-order (eg. using `a` before `const int a = 4;`)
* `1_size_analysis` describes a mechanism for figuring out sizes and alignments of types
    * There could also be an attribute system for indicating a desired size and alignment for a given type (not shown here)
* `2_tstub` generates the type stub headers
    * These allow importers to avoid unnecessary dependencies to other modules
    * eg. if module `A` imports `B`, and `B` imports `C`, then a change to a function in `C` should not cause `A` to recompile
* `3_export` generates the headers that are imported
    * Type stubs are used in the functions, variables, type definitions
    * The actual type comes with an implicit zero-cost conversion between it and its type stub
    * Also note an expansion of the constant `max_edges_per_node` in `graph/node__export.h`
* `4_impl` generates the implementations
    * Insert conversions whenever fields of a type are accessed (read or write, though constructors are tricky)
        * Note that type-punning (eg. `(*(struct S*)&a)`) may not be safe due to [strict aliasing](https://cellperformance.beyond3d.com/articles/2006/06/understanding-strict-aliasing.html) and size/alignment rules not being enforced by the spec
        * I also don't think I caught every cast (it's enough to compile)
    * We also move constants and type definitions not already in `__export.h` to the top, as well as adding function declarations
        * This is what allows top-level declarations to be out-of-order
* `5_tweaking` alters the library imports to make it compile
    * ie. `#include <stdio.h>` instead of `#include <stdio__export.h>`

Advanced considerations:
* No private fields, though opaque types can be made
* Hoisting occuring at top-level, what about within functions?
* How does update logic work?
* No module interface logic here (ie. strong module split)
* How much of compilation is centrally controlled (ie. by a file that keeps track of the entire project's dependencies)?
    * `__tstub.h` changes every time a new type is added, but a central file can check if importing files actually need recompilation
* Extra details: How to perform a unity build? Static/dynamic library generation and management?
* Aside: Uniform function call syntax
