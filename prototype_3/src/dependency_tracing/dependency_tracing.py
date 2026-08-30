from .. import logging
from ..interface_generation.ListenerExtractSymbolDefinitions import SymbolType, QuerySymbolType
from ..interface_generation.interface_generation import ModuleInterface
from ..scope_resolution.scope_resolution import GraphNode, GraphInfo, DepType


def generate_module_text(module_name: str, module_data: dict[str, ModuleInterface], module_graph: dict[GraphNode[QuerySymbolType], GraphInfo]) -> list[str]:
    """Performs a post-order traversal of module_graph, starting from module_name's own
    definitions, to produce a flat, dependency-ordered list of C text fragments.
    ```
        module_data: dict[module_name: str, ModuleInterface]
        module_graph: dict[GraphNode[QuerySymbolType], GraphInfo], the merged dependency graphs (via
            generate_dependency_graph) of module_name and everything it could transitively
            depend on (its own imports, their imports, etc.)
        returns: list[text: str], such that '\\n'.join(output) produces valid, dependency-ordered C code
    ```
    """
    output: list[str] = []
    visiting: set[GraphNode[SymbolType]] = set()  # nodes currently on the DFS stack (used to detect cycles)
    visiting_stack: list[GraphNode[SymbolType]] = []  # same as visiting, but list form (so we can grab the last element)
    visited: set[GraphNode[SymbolType]] = set()  # nodes whose text (and dependencies) have already been emitted
    late_symbol_definitions: list[GraphNode[SymbolType]] = []  # inline functions need to provide their definitions
    late_type_definitions: list[GraphNode[SymbolType]] = []

    def visit(originalNode: GraphNode[SymbolType]):
        nonlocal late_symbol_definitions, late_type_definitions
        queryNode: GraphNode[QuerySymbolType] = GraphNode(originalNode.module_name, originalNode.name,
                                                          originalNode.symbolType.toQuerySymbolType(), originalNode.depType)
        if originalNode in visited:
            return
        if originalNode in visiting:
            logging.error(f"cyclic dependency detected at {originalNode} (stack: {list(visiting)})")
            output.append(f"// ERROR: cyclic dependency detected at {originalNode}")
            return
        assert queryNode in module_graph, f"{queryNode=} (from {originalNode=}) not found in module_graph"

        visiting.add(originalNode); visiting_stack.append(originalNode)
        text, dependencies, module_specific_text = module_graph[queryNode]
        for dependency in dependencies:
            visit(dependency)
        if text is not None:
            if originalNode.depType == DepType.DECLARATION and originalNode._replace(depType=DepType.DEFINITION) in visited:
                pass  # avoid redundant declarations (harmless but adds clutter)
            elif (originalNode.symbolType == SymbolType.TYPEDEF and
                  originalNode._replace(depType=DepType.DEFINITION 
                                        if originalNode.depType == DepType.DECLARATION
                                        else DepType.DECLARATION) in visited):
                pass  # duplicate typedef definitions are technically not C99 compliant (6.7p3), even if compilers support it
            else:
                output.append(text)
        visiting.discard(originalNode); visiting_stack.pop()
        visited.add(originalNode)
    
        if originalNode.depType == DepType.DECLARATION and module_graph[queryNode._replace(depType=DepType.DEFINITION)].module_specific_text is not None:
            # if inline function declaration, put its definition in the queue
            late_symbol_definitions.append(originalNode._replace(depType=DepType.DEFINITION))
        if originalNode.depType == DepType.DECLARATION and originalNode.symbolType.isType():
            # if type declaration, put its definition in the queue
            late_type_definitions.append(originalNode._replace(depType=DepType.DEFINITION))
        if module_specific_text is not None and len(visiting_stack) == 0:
            # inline function has to actually emit the symbol
            output.append(module_specific_text)
        if len(visiting_stack) == 0:
            # emit inline function definitions
            lsd = late_symbol_definitions
            late_symbol_definitions = []
            for dependency in lsd:
                visit(dependency)
        if len(visiting_stack) == 0 or not visiting_stack[-1].symbolType.isType():
            # emit type definitions (must be before nontype in case it is used)
            ltd = late_type_definitions
            late_type_definitions = []
            for dependency in ltd:
                visit(dependency)

    interface = module_data[module_name]
    for name, is_exported, symbolType, _ in interface.definitions:
        visit(GraphNode(module_name, name, symbolType, DepType.DEFINITION))

    return output
