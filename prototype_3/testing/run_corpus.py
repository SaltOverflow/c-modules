# Run `python3 testing/run_corpus.py` while in venv
# Can also do `python3 testing/run_corpus.py --files testing/defineInsideFunction.cmod`

import glob, os, argparse

import src.logging as logging
from src.scope_resolution import symbolTable as st
from src.interface_generation.interface_generation import generate_module_interface, ModuleInterface
from src.interface_generation.ListenerExtractSymbolDefinitions import SymbolType

from antlr4 import InputStream, CommonTokenStream
from src.scope_resolution.parser.CMODFullLexer import CMODFullLexer
from src.scope_resolution.parser.CMODFullParser import CMODFullParser

parser = argparse.ArgumentParser()
parser.add_argument('--files', nargs='+', help='List of .cmod file names')
args = parser.parse_args()

cmod_files = sorted(glob.glob('testing/*.cmod'))
cmod_files = [f for f in cmod_files if 'justC' not in os.path.basename(f) and 'invalid' not in os.path.basename(f)]
if args.files is not None:
    cmod_files = args.files

module_data: dict[str, tuple[str, ModuleInterface, str]] = {}  # dict[module_name: str, (text: str, ModuleInterface, file_name: str)]
for f in cmod_files:
    text = open(f).read()
    interface = generate_module_interface(text)
    module_data[interface.module] = (text, interface, f)
if logging.errorCount > 0:
    print(f"{logging.errorCount} errors after generating interfaces!")

print('Discovered modules:', list(module_data.keys()))
print()

for module_name, (text, interface, fname) in module_data.items():
    st.reset()
    st.addToFileSymbolTable(module_name, interface.definitions, exported_only=False)
    for imported_name in interface.imports:
        if imported_name not in module_data:
            logging.error(f'{module_name} imports unknown module {imported_name}')
            continue
        _, imported_interface, _ = module_data[imported_name]
        st.addToFileSymbolTable(imported_name, imported_interface.definitions, exported_only=True)

    lexer = CMODFullLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = CMODFullParser(stream)
    tree = parser.compilationUnit()
    if parser.getNumberOfSyntaxErrors() > 0:
        logging.error(f"syntax errors running CMODFull on {text!r}")
    st.sanityCheck()
    print(f'{fname} (module {module_name}): errors so far={logging.errorCount}')

print()
print('TOTAL ERRORS:', logging.errorCount)
