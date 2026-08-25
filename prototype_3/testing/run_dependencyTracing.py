import glob, os
from src.interface_generation.process import generate_module_interface
from src.scope_resolution.process import generate_dependency_graph
from src.dependency_tracing.process import generate_module_text

cmod_files = sorted(glob.glob('testing/*.cmod'))
cmod_files = [f for f in cmod_files if 'justC' not in os.path.basename(f) and 'invalid' not in os.path.basename(f)]

module_data = {}
for f in cmod_files:
    text = open(f).read()
    module_data[generate_module_interface(text)['module']] = generate_module_interface(text)

module_graph = {}
for module_name in module_data:
    module_graph.update(generate_dependency_graph(module_name, module_data))

for module_name in module_data:
    output = generate_module_text(module_name, module_data, module_graph)
    errors = [line for line in output if line.startswith('// ERROR')]
    print(f'{module_name}: {len(output)} lines, {len(errors)} errors')
