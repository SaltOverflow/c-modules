# Run `python3 testing/run_interfaceGeneration.py` while in venv
# Can also do `python3 testing/run_interfaceGeneration.py --files testing/defineInsideFunction.cmod`

import glob, os, argparse

import src.logging as logging
from src.interface_generation.interface_generation import generate_module_interface, ModuleInterface

parser = argparse.ArgumentParser()
parser.add_argument('--files', nargs='+', help='List of .cmod files to generate interfaces for')
args = parser.parse_args()

if args.files is not None:
    cmod_files = args.files
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # so the glob is relative to this script's directory
    cmod_files = sorted(glob.glob('*.cmod'))
    cmod_files = [f for f in cmod_files if 'justC' not in os.path.basename(f) and 'invalid' not in os.path.basename(f)]

module_data: dict[str, ModuleInterface] = {}
for f in cmod_files:
    text = open(f).read()
    interface = generate_module_interface(text)
    module_data[interface.module] = interface

for k, v in module_data.items():
    print(v)
print()
print('TOTAL ERRORS:', logging.errorCount)
