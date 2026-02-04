## Generating the parser code *(already done, in parser/)*

Using ANTLR4 (v4.13.2) to parse grammars. See https://github.com/antlr/antlr4/blob/master/doc/getting-started.md for details. Run `pip install antlr4-tools` to get `antlr4` and `anltr4-parse` executables. Example command: `antlr4-parse parser/CMOD.g4 compilationUnit -gui testing/noImports.cmod`

CMOD.g4 grammar inspired by https://github.com/antlr/grammars-v4/blob/master/c/C.g4 (though heavily edited afterwards). Ran `antlr4 -Dlanguage=Python3 parser/CMOD.g4` to generate parser code (you can add `-visitor -listener` flags for extra capabilities).

## Running the code

Adapted the steps from https://github.com/antlr/antlr4/blob/master/doc/python-target.md to generate output. Run `pip install -r requirements.txt` to get needed libraries, then `python3 Driver.py -r testing testing/noImports.cmod` to run on example code.

## Documentation

The concepts behind this prototype are discussed in `../proposals/stitched_modules.md`
