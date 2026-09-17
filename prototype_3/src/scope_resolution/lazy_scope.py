import os
import pickle
from .. import logging
from ..interface_generation.ListenerExtractSymbolDefinitions import QuerySymbolType
from ..interface_generation.interface_generation import ModuleInterface
from ..interface_generation.lazy_interface import module_mtimes
from .scope_resolution import GraphNode, GraphInfo, generate_dependency_graph

project_root: str | None = None
lazyLoad: bool = False
readCache: bool = False
storeCache: bool = False

def getGraphInfo(queryNode: GraphNode[QuerySymbolType], module_graph: dict[GraphNode[QuerySymbolType], GraphInfo], module_data: dict[str, ModuleInterface]) -> GraphInfo:
    """Get graph node, filling in the entry if needed."""
    if queryNode not in module_graph:
        if lazyLoad:
            generateGraphInfo(queryNode.module_name, module_graph, module_data)
    assert queryNode in module_graph, f"Missing graph information for {queryNode=}"
    return module_graph[queryNode]

def generateGraphInfo(module_name: str, module_graph: dict[GraphNode[QuerySymbolType], GraphInfo], module_data: dict[str, ModuleInterface]) -> None:
    """Fill in missing scope resolution entries in module_graph. Uses file caches to avoid extra processing."""
    if readCache:
        assert project_root is not None, "project_root must be set in order to use caches"
        cache_path = os.path.join(project_root, '.cmod', module_name + '.cmodg')
        if os.path.isfile(cache_path):
            with open(cache_path, 'rb') as f:
                cached_mtimes, graph = pickle.load(f)
            for cached_module_name, cached_mtime in cached_mtimes.items():
                module_path = os.path.join(project_root, cached_module_name + '.cmod')
                if cached_mtime < os.path.getmtime(module_path):
                    break
            else:
                module_graph.update(graph)
                return

    graph = generate_dependency_graph(module_name, module_data)
    module_graph.update(graph)

    if storeCache and logging.errorCount == 0:
        assert project_root is not None, "project_root must be set in order to use caches"
        cache_path = os.path.join(project_root, '.cmod', module_name + '.cmodg')
        cached_mtimes = {module_name: module_mtimes[module_name]}
        for imported_module in module_data[module_name].imports:
            cached_mtimes[imported_module] = module_mtimes[imported_module]
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        with open(cache_path, 'wb') as f:
            pickle.dump((cached_mtimes, graph), f)
