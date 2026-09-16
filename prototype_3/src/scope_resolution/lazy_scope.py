from ..interface_generation.ListenerExtractSymbolDefinitions import QuerySymbolType
from ..interface_generation.interface_generation import ModuleInterface
from .scope_resolution import GraphNode, GraphInfo, generate_dependency_graph

lazyLoad: bool = False

def getGraphInfo(queryNode: GraphNode[QuerySymbolType], module_graph: dict[GraphNode[QuerySymbolType], GraphInfo], module_data: dict[str, ModuleInterface]) -> GraphInfo:
    if queryNode not in module_graph:
        if lazyLoad:
            lazyScopeResolution(queryNode.module_name, module_graph, module_data)
    assert queryNode in module_graph, f"Missing graph information for {queryNode=}"
    return module_graph[queryNode]

def lazyScopeResolution(module_name: str, module_graph: dict[GraphNode[QuerySymbolType], GraphInfo], module_data: dict[str, ModuleInterface]) -> None:
    graph = generate_dependency_graph(module_name, module_data)
    module_graph.update(graph)
