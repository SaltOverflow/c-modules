from ..scope_resolution import symbolTable as st
from ..scope_resolution.process import GraphNode, GraphInfo, DepType


def generate_module_text(module_name: str, module_data: dict, module_graph: dict[GraphNode, GraphInfo]) -> list[str]:
    """Performs a post-order traversal of module_graph, starting from module_name's own
    definitions, to produce a flat, dependency-ordered list of C text fragments.
    ```
        module_data: dict[module_name: str, interface: <generate_module_interface>]
        module_graph: dict[GraphNode, GraphInfo], the merged dependency graphs (via
            generate_dependency_graph) of module_name and everything it could transitively
            depend on (its own imports, their imports, etc.)
        returns: list[text: str], such that '\\n'.join(output) produces valid, dependency-ordered C code
    ```
    """
    output = []
    visiting = set()  # set[GraphNode], nodes currently on the DFS stack (used to detect cycles)
    visited = set()  # set[GraphNode], nodes whose text (and dependencies) have already been emitted

    def visit(originalNode: GraphNode):
        queryNode = originalNode._replace(symbolType=st.getQuerySymbolType(originalNode.symbolType))
        if originalNode in visited:
            return
        if originalNode in visiting:
            # Let it keep going
            print(f"// ERROR: cyclic dependency detected at {originalNode} (stack: {list(visiting)})")
            output.append(f"// ERROR: cyclic dependency detected at {originalNode}")
            return
        if queryNode not in module_graph:
            # Let it keep going
            print(f"// ERROR: {queryNode=} (from {originalNode=}) not found in module_graph")
            output.append(f"// ERROR: {queryNode=} (from {originalNode=}) not found in module_graph")
            return

        visiting.add(originalNode)
        text, dependencies, extra_text = module_graph[queryNode]
        for dependency in dependencies:
            visit(dependency)
        if text is not None:
            output.append(text)
        if extra_text is not None:
            output.append(extra_text)
        visiting.discard(originalNode)
        visited.add(originalNode)

    interface = module_data[module_name]
    for name, is_exported, symbolType, _ in interface['definitions']:
        visit(GraphNode(module_name, name, symbolType, DepType.DEFINITION))

    return output
