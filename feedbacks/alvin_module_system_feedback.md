<!--
This is not my work, this is feedback from Andrew
Written in response to modules v4, back when Walkthrough and Formalism sections were not written yet
-->

Alvin Module System Feedback
============================

## Goals
"Make C translation units into modules." isn't a goal like the others, it is
more the project. But I think you are trying to say something about
visibility or linkage.

## Stratagy (high-level)
If we are generating the interfaces from the modules, then (by transitivity
of dependencies) are our modules still weak? Are regular C modules strong?

"modules can only export symbols that they own"
- Define "own" (and maybe export?)
- This is phrased like a general fact, but I think it is a goal.

For specializations of polymorphic functions, you might want to call out it
is creating new specializations in different modules that is hard. Not having
specalizations in general.

## Stratagy (implementation details)
Are there significantly different types of symbols in Cforall? ex. traits?

### Handling unboxed types
I think you can reference the existing notion of sized types in Cforall.
You will also have to consider life-time operations.

For option 2, we are doing similar things for polymorphic types already,
you will probably want to look into that.

### C macros are not exportable
"Overcomplicate" the C preprocessor? I feel I am going to need that in more
concrete terms especially considering the compleity of this proposal.

(Other arguement is fine.)

Is the main use of macros to implement polymorphic code? That's all traits
can replace. Also, we could preserve macros for later.

### Import ordering does not matter
All good features, I don't actually see how we are implementing any of this
in this section.

In paragraph 3, I think you are actually making an argument for precompiled
headers here. That being said, running the preprocessor once would give some
savings still, but probably not as much as a compiled header/symbol file.
(I am recalling some previous examples you showed that generated header files
containing text Cforall code.)

We already have language servers that can preform auto completion and aid
in code generation. How does this help them?

### Forward ceclarations are unnecessary
Sounds good. I will try and break it appart at some point.
Some ideas include nested types, recurive types and typeof silliness.

### Explicit transitive dependencies
Looks good, but is does once again make me wonder what a module owning a
symbol means. Does std own the symbols of std/vector and std/iostream to
export them?

### Exporting inline functions
I think this is all good, but the wording of things like "regenerate" does
confuse me a bit. (I think you mean keep the inline function in a precompiled
state?)

### Generating multiple module interfaces
All looks good. Nothing about the implementation yet.
And think the bit about static functions belongs in a different section.

### Modules use `import` instead of `#include`
How does this all work with libraries and system headers?

There is actually no time the module name is in front of the symbol name.

### Forall polymorphism
Note, the current implementation uses a lot of parameters, not vtables,
outside of some narrow uses with exceptions.

I have no idea how this connects to `impl` vs `dyn`. Actually generally,
don't turn to Rust quite as frequently, not because of the language itself,
but because the lab hasn't worked with it nearly as much.
