# Run `python3 testing/run_dependencyTracing_lazy.py` while in venv
# Can also do `python3 testing/run_dependencyTracing_lazy.py --modules a`

import glob, os, argparse
from pprint import pprint
import src.logging as logging
from src.interface_generation.interface_generation import ModuleInterface
from src.interface_generation import lazy_interface
from src.scope_resolution.scope_resolution import GraphNode, QuerySymbolType, GraphInfo
from src.scope_resolution import lazy_scope
from src.dependency_tracing.dependency_tracing import generate_module_text

parser = argparse.ArgumentParser()
parser.add_argument('--modules', nargs='+', help='List of modules to display dependency trace on')
args = parser.parse_args()

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # so the glob is relative to this script's directory
cmod_files = sorted(glob.glob('*.cmod'))
cmod_files = [f for f in cmod_files if 'justC' not in os.path.basename(f) and 'invalid' not in os.path.basename(f)]
module_names = [os.path.splitext(os.path.basename(f))[0] for f in cmod_files]

module_data: dict[str, ModuleInterface] = {}
module_graph: dict[GraphNode[QuerySymbolType], GraphInfo] = {}
lazy_interface.lazyLoad = True
lazy_interface.project_root = '.'
lazy_scope.lazyLoad = True

if args.modules:
    for module_name in args.modules:
        output = generate_module_text(module_name, module_data, module_graph)
        pprint(output)
        print(f'{module_name}: errors so far={logging.errorCount}')
else:
    for module_name in module_names:
        output = generate_module_text(module_name, module_data, module_graph)
        print(f'{module_name}: {len(output)} entries, errors so far={logging.errorCount}')
