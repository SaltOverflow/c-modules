## Generating the parser code

Using ANTLR4 (v4.13.2) to parse grammars. See https://github.com/antlr/antlr4/blob/master/doc/getting-started.md for details. Run `pip install antlr4-tools` to get `antlr4` and `anltr4-parse` executables. Example command: `antlr4-parse -v 4.13.2 src/parser/CMOD.g4 compilationUnit -gui testing/basic.cmod`

CMOD.g4 grammar originally taken from Annex A of C99 standard, then edited to work with modules. Ran `antlr4 -v 4.13.2 -Dlanguage=Python3 src/parser/CMOD.g4 -listener` to generate parser code (flags like `-visitor -listener` generate extra capabilities).

## Running the code

Followed steps in https://stackoverflow.com/a/50194143 to set up import directory. First create virtual env `python -m venv .venv`, then activate `. .venv/bin/activate` (this is for Linux, use `./venv/Scripts/activate` for Windows). Note that `deactivate` on Linux gets you out of the venv. Now run `pip install -e .` in this directory.

Adapted the steps from https://github.com/antlr/antlr4/blob/master/doc/python-target.md to generate output. Run `pip install -r requirements.txt` to get needed libraries, then `python3 src/Driver.py -r testing testing/basic.cmod` to run on example code.

## Documentation

The concepts behind this prototype are discussed in [my ONPLS 2026 presentation](https://docs.google.com/presentation/d/10CdEMUHpR9FgXT7NRg_zzKULKEtGaaZ1YX_n6-uuW5o/edit?slide=id.p#slide=id.p).

*The previous prototype was presented at the seminar, so we create a separate iteration for further work. This extends the grammar to almost all C99 code (ignore trigrams and K&R syntax), including expression parsing. Module namespacing is left to the next iteration, as it introduces additional language extensions.*
