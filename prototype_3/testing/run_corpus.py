# Run `python3 testing/run_corpus.py` while in venv
# Can also do `python3 testing/run_corpus.py --files testing/defineInsideFunction.cmod`

import sys, glob, os, argparse

from src.scope_resolution import symbolTable as st
from src.interface_generation.process import generate_module_interface
from src.interface_generation.ListenerExtractSymbolDefinitions import SymbolType

from antlr4 import *
from src.scope_resolution.parser.CMODFullLexer import CMODFullLexer
from src.scope_resolution.parser.CMODFullParser import CMODFullParser

parser = argparse.ArgumentParser()
parser.add_argument('--files', nargs='+', help='List of .cmod file names')
args = parser.parse_args()

cmod_files = sorted(glob.glob('testing/*.cmod'))
cmod_files = [f for f in cmod_files if 'justC' not in os.path.basename(f) and 'invalid' not in os.path.basename(f)]
if args.files is not None:
    cmod_files = args.files

# Build module_name -> (text, interface) map for all files upfront
module_data = {}
for f in cmod_files:
    text = open(f).read()
    interface = generate_module_interface(text)
    module_data[interface['module']] = (text, interface, f)

print('Discovered modules:', list(module_data.keys()))
print()

total_errors = 0
for module_name, (text, interface, fname) in module_data.items():
    st.reset()
    st.addToFileSymbolTable(module_name, interface['definitions'], exported_only=False)
    for imported_name in interface['imports']:
        if imported_name not in module_data:
            print(f'// WARNING: {module_name} imports unknown module {imported_name}')
            continue
        _, imported_interface, _ = module_data[imported_name]
        st.addToFileSymbolTable(imported_name, imported_interface['definitions'], exported_only=True)

    lexer = CMODFullLexer(InputStream(text))
    tokens = lexer.getAllTokens()
    lexer.reset()
    stream = CommonTokenStream(lexer)
    parser = CMODFullParser(stream)
    tree = parser.compilationUnit()
    n = parser.getNumberOfSyntaxErrors()
    total_errors += n
    st.sanityCheck(tokens)
    print(f'{fname} (module {module_name}): errors={n}')

print()
print('TOTAL ERRORS:', total_errors)