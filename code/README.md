Using ANTLR4 (v4.13.2) to parse grammars. See https://github.com/antlr/antlr4/blob/master/doc/getting-started.md for instructions on how to use.
Example command: `antlr4-parse parser/C.g4 compilationUnit -gui testing/graph.c`

C.g4 grammar taken from https://github.com/antlr/grammars-v4/blob/master/c/C.g4 (compilationUnit is the root node).

Ran `antlr4 -Dlanguage=Python3 -visitor -listener parser/C.g4` to generate parser code.

Adapted the steps from https://github.com/antlr/antlr4/blob/master/doc/python-target.md to generate output.

Run `pip install -r requirements.txt` to get needed libraries, then `python3 Driver.py -r testing testing/graph.c` to run on example code.
