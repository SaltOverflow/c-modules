import argparse
import os
import sys

from src import logging
from src.interface_generation.interface_generation import ModuleInterface
from src.interface_generation import lazy_interface
from src.scope_resolution.scope_resolution import GraphNode, GraphInfo, QuerySymbolType
from src.scope_resolution import lazy_scope
from src.dependency_tracing.dependency_tracing import generate_module_text


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='the .cmod file to compile; imported modules are looked up '
                                           'in the same folder as this file')
    parser.add_argument('--eager', action='store_true',
                         help='eagerly resolve the transitive import closure of modules, '
                              'which does more work than needed, but simplifies the debug trace')
    return parser.parse_args()


def generate_code_eager(entry_module_name: str, project_root: str) -> list[str]:
    lazy_interface.project_root = project_root
    module_data: dict[str, ModuleInterface] = {}
    to_load = [entry_module_name]
    while to_load:
        module_name = to_load.pop()
        if module_name in module_data:
            continue
        lazy_interface.lazyInterfaceGeneration(module_name, module_data)
        interface = module_data[module_name]
        to_load.extend(interface.imports)
    
    module_graph: dict[GraphNode[QuerySymbolType], GraphInfo] = {}
    for module_name in module_data:
        lazy_scope.lazyScopeResolution(module_name, module_graph, module_data)

    return generate_module_text(entry_module_name, module_data, module_graph)


def generate_code_lazy(entry_module_name: str, project_root: str) -> list[str]:
    module_data: dict[str, ModuleInterface] = {}
    module_graph: dict[GraphNode[QuerySymbolType], GraphInfo] = {}
    lazy_interface.lazyLoad = True
    lazy_interface.project_root = project_root
    lazy_scope.lazyLoad = True
    return generate_module_text(entry_module_name, module_data, module_graph)


def generate_code(input_file: str, eager: bool) -> str:
    project_root, filename = os.path.split(input_file)
    dot_index = filename.rfind('.')
    if dot_index < 0 or filename[dot_index:] != '.cmod':
        raise RuntimeError("input_file must use .cmod suffix")
    entry_module_name = filename[:dot_index]
    if eager:
        output = generate_code_eager(entry_module_name, project_root)
    else:
        output = generate_code_lazy(entry_module_name, project_root)
    return '\n'.join(output)


def main():
    args = parse_args()
    code = generate_code(args.input_file, args.eager)
    print(code)
    if logging.errorCount > 0:
        print(f"// {logging.errorCount} error(s) encountered during compilation", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
