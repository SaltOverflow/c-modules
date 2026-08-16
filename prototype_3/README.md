# A cyclic module system for C99

Building upon the concepts described in [my ONPLS 2026 presentation](https://docs.google.com/presentation/d/10CdEMUHpR9FgXT7NRg_zzKULKEtGaaZ1YX_n6-uuW5o/edit?slide=id.p#slide=id.p), we extend the module system prototype to *almost all* of C99 (minus trigraphs and K&R syntax).

The module system takes in preprocessed code and outputs C code, to be passed along to a C compiler like GCC. Modules can cyclically import each other, as long as symbols don't depend on their own definitions. A module file starts with `module <identifier>;` , followed by zero or more `import <identifier>;` , followed by zero or more symbol definitions (which may have `export` in front of them). Note that forward declarations like function prototypes are disallowed, as all symbols within a file are already visible to each other.

The grand vision is to turn this into a true drop-in replacement for header files. This approach can also be applied to other languages in the C family, such as C++ or Cforall. *Note: This is a work in progress. If you want to be able to import header files, that will come in a later iteration.*

## Getting started

* Creating the venv (following instructions in https://stackoverflow.com/a/50194143 ):
    * Run `python -m venv .venv` in the directory this README is found.
    * On Linux, run `. .venv/bin/activate` (`deactivate` exits the venv).
    * Run `pip install -e .` (uses `pyproject.toml` to install `src/` as a module).
* Generating the parser code (see https://github.com/antlr/antlr4/blob/master/doc/getting-started.md for details):
    * Run `pip install antlr4-tools` (gets `antlr4` and `antlr4-parse` executables).
        * Example command: `antlr4-parse -v 4.13.2 src/interface_generation/parser/CMODInterface.g4 compilationUnit -gui testing/basic.cmod` .
    * Run `antlr4 -v 4.13.2 -Dlanguage=Python3 src/interface_generation/parser/CMODInterface.g4 -listener` (if you installed `antlr4` directly, remove the `-v 4.13.2` argument).
* Running the code (adapted steps from https://github.com/antlr/antlr4/blob/master/doc/python-target.md ):
    * Run `pip install -r requirements.txt` .
    * Example command: `python3 src/Driver.py -r testing testing/basic.cmod` .

Adapted the steps from https://github.com/antlr/antlr4/blob/master/doc/python-target.md to generate output. Run `pip install -r requirements.txt` to get needed libraries, then `python3 src/Driver.py -r testing testing/basic.cmod` to run on example code.
