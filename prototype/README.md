Using ANTLR4 (v4.13.2) to parse grammars. See https://github.com/antlr/antlr4/blob/master/doc/getting-started.md for instructions on how to use.
Example command: `antlr4-parse parser/CMOD.g4 compilationUnit -gui testing/noImports.c`

CMOD.g4 grammar inspired by https://github.com/antlr/grammars-v4/blob/master/c/C.g4

Ran `antlr4 -Dlanguage=Python3 parser/CMOD.g4` to generate parser code (you can add `-visitor -listener` flags for extra capabilities).

Adapted the steps from https://github.com/antlr/antlr4/blob/master/doc/python-target.md to generate output.

Run `pip install -r requirements.txt` to get needed libraries, then `python3 Driver.py -r testing testing/noImports.c` to run on example code.

The documentation behind these modules can be found at `../proposals/stitched_modules.md`
