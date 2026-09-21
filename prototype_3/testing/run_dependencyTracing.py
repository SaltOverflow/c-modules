# Run `python3 testing/run_dependencyTracing.py` while in venv
# Can also do `python3 testing/run_dependencyTracing.py --modules a`

import glob, os, argparse
from pprint import pprint
import src.logging as logging
from src.interface_generation.interface_generation import generate_module_interface, ModuleInterface
from src.scope_resolution.scope_resolution import generate_dependency_graph, GraphNode, QuerySymbolType, GraphInfo
from src.dependency_tracing.dependency_tracing import generate_module_text

parser = argparse.ArgumentParser()
parser.add_argument('--modules', nargs='+', help='List of modules to display dependency trace on')
args = parser.parse_args()

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # so the glob is relative to this script's directory
cmod_files = sorted(glob.glob('*.cmod'))
cmod_files = [f for f in cmod_files if 'justC' not in os.path.basename(f) and 'invalid' not in os.path.basename(f)]
if args.modules:
    cmod_files.extend(f'{m}.cmod' for m in args.modules)  # duplicates are wastful, but idempotent

module_data: dict[str, ModuleInterface] = {}
for f in cmod_files:
    text = open(f).read()
    interface = generate_module_interface(text)
    module_data[interface.module] = interface

module_graph: dict[GraphNode[QuerySymbolType], GraphInfo] = {}
for module_name in module_data:
    graph = generate_dependency_graph(module_name, module_data)
    if args.modules and module_name in args.modules:
        for k, v in graph.items():
            print(f"{k}: {v}")
    module_graph.update(graph)
print('errors after building dependency graphs:', logging.errorCount)

if args.modules:
    for module_name in args.modules:
        output = generate_module_text(module_name, module_data, module_graph)
        pprint(output)
        print(f'{module_name}: errors so far={logging.errorCount}')
else:
    for module_name in module_data:
        output = generate_module_text(module_name, module_data, module_graph)
        print(f'{module_name}: {len(output)} entries, errors so far={logging.errorCount}')
