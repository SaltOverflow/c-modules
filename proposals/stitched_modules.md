# Stitched modules

## Background context

C doesn't have modules -- instead, C relies on the programmer (+ preprocessor) to insert the references to any symbols that are defined in other files. This is because the C compiler only processes one translation unit from top to bottom, so you have to give it everything, and in the correct order.

So our C module system simply analyzes other modules and extracts any imported information to give to the compiler, right? Yes, but it's a bit tricky because C is a systems programming language, which means we care a lot about how our code is compiled. An object-oriented approach hides a class' implementation behind a pointer and a vtable (also a pointer), so importers can use a class without even knowing its size. This doesn't work for C because it has unboxed types, so we need to expose information to the compiler.

### A previous attempt

A previous attempt at C modules used "type stubs", meaning that each exported type would generate a "stub" type with only size and alignment information. Any function that returned the exported type would return the "stub" type instead, so importers wouldn't need to know any implementation details unless they imported the actual type (which would use type-punning to convert between the two). This approach unfortunately doesn't work in C because type-punning breaks strict aliasing rules, and the C spec allows small structs to be unpacked when used as arguments into functions. Additionally, extracting size and alignment information can require analyzing the entire codebase -- if we have to do all that to make just unboxed types work, perhaps there are better options.

### Other languages

Let's take a look at some other systems programming languages to see how they do it. C and C++ use header files, as described above. C++20 modules need to be compiled before they can be imported, which makes them acyclic. Rust compiles an entire crate all at once, so modules are essentially namespaces, and modules can import freely within a crate. Zig modules are implicitly structs, and are used by assigning the import to a name.

C and C++ header files lead to a lot of manual module management, where the programmer has to ensure the .h and its corresponding .c file stay in sync. It should be possible to condense this workflow into a single file without any practical loss of functionality. C++20 modules are acyclic, forcing any mutually recursive structures into the same module -- this doesn't work with the granularity of .c/.h files, which frequently share declarations with each other. Rust modules rely on whole-crate compilation, which clashes with the C philosophy of separate compilation. Zig modules share many similarities with this prototype, and present some interesting avenues for further development. As such, we will discuss Zig modules after presenting the prototype.

## The prototype

The code for processing modules is in `Driver.py`, using the grammar in `CMOD.g4`. You can run it on files in `testing/` by following the `README.md`. We will now analyze what `Driver.py` is doing.

`module_data` extracts top-level symbols from the input code, producing a type and variable symbol table (minus the imported symbols). Note that, while parsing C into an AST is context-sensitive (eg. `(a)*b` is a cast or a multiplication, depending on if `a` is a type), it is unambiguous outside of expressions. This means we can extract top-level symbol information from C files, and leave the rest for a later pass (here it is extracted into `used_names_*`, but it can be done right after the `module_input` step).

Next, `module_input` combines the top-level symbols of a module with any imported symbols (which we can do because we have `module_data`) to produce the complete type and variable symbol table. Once this is done, you can parse the remaining expressions in the C file, which would produce a complete AST with the correct symbol references.

Finally, `module_output` performs symbol renaming (so symbols are linked to the correct module), as well as performing a topological ordering (so needed symbols are defined before they are used). The symbol renaming uses a simple namespacing strategy, prepending the file path of the module (when read from the project root directory) to the name (see `full_name()`). The topological ordering takes into consideration whether a definition or declaration is needed, and is able to handle circular file imports. Note that this process allows types to depend on variables out-of-the-box, so inline functions can be supported without significant changes to the algorithm (mutually recursive inline functions may need to be handled by a special case).

The code should be reasonably straightforward to understand, and is fairly robust. The one caveat is that overloading is not supported -- if a function and a variable have the same name, the code will pick one and silently overwrite the other.

### An example

Let's do a quick example to showcase the power of this algorithm:

```
// a.cmod       // b.cmod
module;         module;
import b;       import a;
struct s1 {
    type s2;    struct s2 {
};
struct s3 {         type s3;
                };
    type *s4;   struct s4 {
};                  type s3;
                };
```

This example has many dependencies from a to b, and vice versa. However, the module system can process this into:

```
// a.cmod (processed)
struct b$$s4;
struct a$$s3 {
    type *b$$s4;
};
struct b$$s2 {
    type a$$s3;
};
struct a$$s1 {
    type b$$s2;
};
```

### Design choices

There are a number of design choices in this prototype, as well as ideas that I had in mind when creating this prototype, which are not critical to the functionality of this algorithm.

* Imports follow the file system: Just like `#include`, we resolve modules by following the file system. Other languages have users specify module names, but for now it seemed unnecessarily complex.
    * As such, the module declaration at the top of a module file (`module;`) does not take a name argument (this declaration would be used to distinguish a regular C file from a C module file).
    * As seen in `testing/`, files with the same name as a folder exist outside of it (ie. `yesImports/` and `yesImports.cmod`). This is in line with Rust, which initially used `mod.rs` for folder-like files before using this strategy.
* Symbol names are prefixed with the file path of the module, as read from the project root folder.
* Imports automatically expand into module scope: The alternative is to have imports like `import "graph/node" as N;`. Doing so would require prefixing any symbols from "graph/node.cmod" (eg. `N.struct_1`). The prototype took the other approach to keep the language less verbose.
    * The prototype ignores name clashes, but a full module system should give the ability to disambiguate. One idea is to use the module name (eg. `"../graph".struct_2`)
* We use `import` and `export` keywords to control module visibility.
* This isn't demonstrated in the grammar, but follows from the work in my previous attempt at modules (type stubs). The idea is that struct definitions are not visible unless imported. For example, if a module imports `struct struct_3 {struct struct_4 field_1;};` but does not import `struct struct_4`, it can access `field_1` but it cannot access any fields of `field_1`. This would work similarly to how, if `field_1` were a pointer, you don't have access to the struct.

### Comparison with Zig

Zig has separate compilation, cicular modules and no header files! This is what my module system is trying to do, so it's really worth taking a close look:
* `@import` is like treating the file as a struct. You assign to a name and use it.
    * This neatly unifies language concepts -- Zig's main feature is compile-time logic (`comptime`), and `@import` behaves like any other compile-time function.
* Compile-time functions (`@import` works like one) are memoized, so importing twice leads to references to the same object (avoiding double-definitions).
    * This may explain why they use module names instead of file paths; file paths change depending on the current directory, which messes with memoization.
* The Zig compiler waits until a struct/function is used before analyzing its definition/declaration.
    * This "lazy evalution" differs from my prototype, which performs "eager evaluation" of imports. The prototype does this partly because it's simpler to implement, but also because I need `module_input` in order to resolve parsing ambiguities.
    * Using functions means analyzing function declarations, not their definition. If you want inline functions or constants, those are likely handled by the `comptime` feature. Cforall doesn't have such a feature and requires backwards compatibility with C, so we can't make this assumption. Thankfully, the prototype can be adapted to work for cases such as inline functions.
* Zig has the philosophy of making things explicit: no implicit constructors/destructors, passing allocators into functions, etc. There is also no private struct fields (the idea being that when you're working low-level, you may need access to the internals). I think Cforall takes a different approach, using more powerful abstractions (potentially influenced by C++); however, I think Zig has a lot of merit in wanting to make things visible and tweakable by the programmer, and we could benefit from taking some of these ideas.

### Ideas for future direction

So with this insight, combined with the design choices section, what direction would I like to take this?
* I still like the idea of resolving modules by following the file system. The fact that `import "std/array";` works similarly to `#include "std/array.h"` is really nice in my opinion.
    * That being said, my current grammar also allows writing `import std/array;` , which I think is a mistake. The unquoted version should be reserved for if/when we support named modules, which would look like `module file_reader;` and `import file_reader;`
* Unlike Zig, Cforall still needs to compile down to C code, so prefixing symbol names with the module name is still the most reasonable solution I can come up with that still works with existing C linkers.
* I'm inspired by the way Zig assigns imports to a symbol, so I'd like to try having imports require the `as` keyword (eg. `import "graph/node" as N;`). If the programmer wants the import to be expanded into scope, they can use `with N;` or `import "graph/node" as *;`. This also resolves any nasty disambiguation syntax such as `"../graph".struct_2`.
    * One of the struggles with this was that `import "graph/node" as N; import "graph/node" as M;` (in practice, this could happen through "diamond imports") would mean `N.struct_1` and `M.struct_1` need to refer to the same struct, without double-definition problems. With the concept of memoization, this turns out to be implementable.
    * I concede that `N.struct_1` and `M.struct_1` isn't the nicest thing to deal with. Rust would write `"../graph".struct_2` as `super::graph.struct_2`, but I would like to stick with import names looking the same as `#include`. As a consolation, the meaning is not ambiguous, and this is arguably an edge case.
    * This does increase the verbosity of the language, but it's arguably worth it for the increased readability. Note that Python, a language touted for its ease of use, works in a similar manner. Additionally, this renaming can be automated, so migrating existing systems shouldn't be a problem.
* We use `import/export`, similar to C++20 modules. Rust uses `use/pub`, Zig uses `@import/pub`. For now, I don't see a need to change, and it's fairly simple to update in the future.
* I'm quite conflicted on the idea that struct definitions (therefore its fields) should not be visible unless imported. While restricting field access is common in other languages, no language does it in the way I'm envisoning.
    * By example: if I import `struct struct_5 foo() {...}` but I don't import `struct_5`, I should be able to use `foo()` (which would include assigning to a variable) but I can't access the fields of the return value. You only get the functionality that you import.
    * The implementation problem: In C, in order to create a variable you need to specify its type. So you'll have to provide some way to expose the name `struct_5` to the importer. If you do that, why can't you give me the fields too?
    * The useability problem: The ability to access the fields of a returned value can be seen as necessary in order to properly use a function (eg. function returns named tuple). So you're forcing the programmer to do extra import/export management for not much practical gain. Additionally, this isn't very "C-like", because in regular C you would need to provide the struct definition here.
    * You can think of this concept as "opaque types, but from the importer's side". The function itself does nothing to hide the fact it's using `struct_5`, but the importer cannot use `struct_5` because it didn't import it. Pretty much all other languages (eg. Scala, Swift) put the opaque type on the exporter's side. In comparison, my system seems unnecessarily pedantic. If we want to consider restricting field access, public/private fields also provide better granularity (we might be able to leverage "tagged exports", described below).
        * It's also worth asking if hiding struct information is the right thing. Zig chooses not to have private fields, taking the philosophy that low-level often needs to reach into the internals of a struct in order to produce composable abstraction layers. Something I'm interested in knowing is: if I have a variable whose type has a field with a pointer to some other struct, can I access the other struct's fields? If you can, then it would be consistent between pointer and non-pointer fields.
    * Ultimately, it might be best to abandon this idea, as it is pedantic for not enough practical benefit. Just let the programmer access the struct in the same way it's written in the function declaration.
        * As an aside, trait information in Cforall might also be unnecessarily pedantic. Having to import a forall, trait, struct, and certain methods in order to make use of some polymorphic function seems a bit overkill (though I might be missing something).
* Modules often need to expose different interfaces to different modules. For example, a thread module may need to expose more information to a garbage collection module than a regular module. The object-oriented technique of having "friend classes" is an all-or-nothing approach; it's not great because it lacks granularity. Instead, we can tag certain exports: the thread module uses `export(details) struct internals {...};` while the garbage collection module uses `import thread(+, details);` (the `+` referring to also wanting regular exports).
    * I've never seen this in the wild before, but a quick search shows that Perl has some form of this in the form of `%EXPORT_TAGS`. I like my method of putting it directly on the symbol definition instead of a big array at the bottom of the file, though.

## Future work

* The current request is to generate headers from analyzing .c files. My general steps would be to:
    * parse C code, extract necessary symbols (like `module_data` step).
    * *(start with a simpler model, without inline functions or constants)*
    * figure out what other code it's referencing (use `#include` to figure out where to look, like `module_input` step).
    * Heavily cyclic symbol references requires breaking a single header into multiple parts. To start, we can assume modules are not cyclic and put an `#include` in the header when symbols from other files are used. Then we can see where the cycles are happening and prioritize those first.
    * *tbh I'm not sure why you'd want to go back to using headers when the information is all gathered already -- you could just merge this logic into the compilation step. I think it's more for people who don't want to change anything about their code (use it more like a tool rather than changing their compiler). Perhaps it's a "gateway drug" to the full module system. It also could function as a "source of truth" for what the full module system should be doing.*
* I want to take a closer look at Zig, actually run some code to validate my theories. Also look at some other "low-level languages".
* Flesh out how the full C module system would work.
    * I'd also need to look into implementing migration tooling (likely will be able to reuse functionality from previous steps)
* Write thesis.
* Graduate.
