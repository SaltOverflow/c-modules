import argparse
import os
import sys

from src import logging
from src.interface_generation.interface_generation import generate_module_interface, ModuleInterface
from src.scope_resolution.scope_resolution import generate_dependency_graph, GraphNode, GraphInfo, QuerySymbolType
from src.dependency_tracing.dependency_tracing import generate_module_text


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='the .cmod file to compile; imported modules are looked up '
                                            'in the same folder as this file')
    return parser.parse_args()


def load_module_data(project_root: str, entry_module_name: str) -> dict[str, ModuleInterface]:
    """Loads entry_module_name and every module it transitively imports (recursively),
    resolving each imported module name to <project_root>/<name>.cmod."""
    module_data: dict[str, ModuleInterface] = {}
    to_load = [entry_module_name]
    while to_load:
        module_name = to_load.pop()
        if module_name in module_data:
            continue
        module_path = os.path.join(project_root, module_name + '.cmod')
        if not os.path.isfile(module_path):
            logging.error(f"could not find module {module_name!r} (expected {module_path!r})")
            continue
        with open(module_path) as f:
            text = f.read()
        interface = generate_module_interface(text)
        if interface.module != module_name:
            logging.error(f"module {module_name!r} (file {module_path!r}) declares itself as {interface.module!r}")
        module_data[module_name] = interface
        to_load.extend(interface.imports)
    return module_data


def generate_code(input_file: str) -> str:
    project_root, filename = os.path.split(input_file)
    dot_index = filename.rfind('.')
    if dot_index < 0 or filename[dot_index:] != '.cmod':
        raise RuntimeError("input_file must use .cmod suffix")
    entry_module_name = filename[:dot_index]

    module_data = load_module_data(project_root, entry_module_name)

    module_graph: dict[GraphNode[QuerySymbolType], GraphInfo] = {}
    for module_name in module_data:
        module_graph.update(generate_dependency_graph(module_name, module_data))

    output = generate_module_text(entry_module_name, module_data, module_graph)
    return '\n'.join(output)


def main():
    args = parse_args()
    code = generate_code(args.input_file)
    print(code)
    if logging.errorCount > 0:
        print(f"// {logging.errorCount} error(s) encountered during compilation", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
