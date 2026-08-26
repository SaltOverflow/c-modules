import glob, os
from pprint import pprint
from src.interface_generation.interface_generation import generate_module_interface
from src.scope_resolution.scope_resolution import generate_dependency_graph

cmod_files = sorted(glob.glob('testing/*.cmod'))
cmod_files = [f for f in cmod_files if 'justC' not in os.path.basename(f) and 'invalid' not in os.path.basename(f)]

module_data = {}
for f in cmod_files:
    text = open(f).read()
    interface = generate_module_interface(text)
    module_data[interface['module']] = interface

for module_name in module_data:
    graph = generate_dependency_graph(module_name, module_data)
    for k, v in graph.items():
        k_print = k.module_name, k.name, k.symbolType.name, k.depType.name
        v_print = [(x.module_name, x.name, x.symbolType.name, x.depType.name) for x in v.dependencies]
        print(f"{k_print} -> {v_print}")
    print(f'{module_name}: {len(graph)} nodes')
