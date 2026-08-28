import glob, os, argparse
from pprint import pprint
from src.interface_generation.interface_generation import generate_module_interface, ModuleInterface
from src.scope_resolution.scope_resolution import generate_dependency_graph, GraphNode, QuerySymbolType, GraphInfo
from src.dependency_tracing.dependency_tracing import generate_module_text

parser = argparse.ArgumentParser()
parser.add_argument('--modules', nargs='+', help='List of modules to display dependency trace on')
args = parser.parse_args()

cmod_files = sorted(glob.glob('testing/*.cmod'))
cmod_files = [f for f in cmod_files if 'justC' not in os.path.basename(f) and 'invalid' not in os.path.basename(f)]

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

if args.modules:
    for module_name in args.modules:
        output = generate_module_text(module_name, module_data, module_graph)
        pprint(output)
else:
    for module_name in module_data:
        output = generate_module_text(module_name, module_data, module_graph)
        errors = [line for line in output if line.startswith('// ERROR')]
        print(f'{module_name}: {len(output)} lines, {len(errors)} errors')
