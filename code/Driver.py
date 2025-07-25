import argparse
from antlr4 import *
from parser.CLexer import CLexer
from parser.CParser import CParser

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="file to parse")
    parser.add_argument("-a", "--action", type=int, choices=[0], default=0, help="""
                        what action to take.
                        0 = parse and output text
                        """)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    input_stream = FileStream(args.input_file)
    lexer = CLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.compilationUnit()
    print(tree.getText())

# input_stream = FileStream('testing/just_main.c')
# lexer = CLexer(input_stream)
# tokens = lexer.getAllTokens()
# # tokens[0].text

# input_stream = FileStream('testing/just_main.c')
# lexer = CLexer(input_stream)
# stream = CommonTokenStream(lexer)
# parser = CParser(stream)
# tree = parser.compilationUnit()
# # tree.getSourceInterval()  # eg. a,b = tree.getSourceInterval() ; ''.join(i.text for i in tokens[a:b+1])
# # tree.getChildren()
# # tree.getChildCount()
# # tree.getChild()

if __name__ == '__main__':
    main()