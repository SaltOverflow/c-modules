# Run `python3 testing/run_scopeResolution.py` while in venv

import glob, os
import src.logging as logging
from src.interface_generation.interface_generation import generate_module_interface, ModuleInterface
from src.scope_resolution.scope_resolution import generate_dependency_graph

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # so the glob is relative to this script's directory
cmod_files = sorted(glob.glob('*.cmod'))
cmod_files = [f for f in cmod_files if 'justC' not in os.path.basename(f) and 'invalid' not in os.path.basename(f)]

module_data: dict[str, ModuleInterface] = {}
for f in cmod_files:
    text = open(f).read()
    interface = generate_module_interface(text)
    module_data[interface.module] = interface

for module_name in module_data:
    graph = generate_dependency_graph(module_name, module_data)
    for k, v in graph.items():
        print(f"{k}: {v}")
    print(f'{module_name}: {len(graph)} nodes, {logging.errorCount} errors so far')
