import os
import pickle
from .interface_generation import ModuleInterface, generate_module_interface
from .. import logging

project_root: str | None = None
lazyLoad: bool = False
readCache: bool = False
storeCache: bool = False

module_mtimes: dict[str, float] = {}  # used by lazy_scope

class ModuleNotFound(Exception):
    pass

def getInterface(module_name: str, module_data: dict[str, ModuleInterface]) -> ModuleInterface:
    """Get module interface, filling in the entry if needed."""
    if module_name not in module_data:
        if lazyLoad:
            generateInterface(module_name, module_data)
    assert module_name in module_data, f"Missing interface for {module_name=}"
    assert module_name in module_mtimes, f"Module mtimes should also be set (used in caches)"
    return module_data[module_name]

def generateInterface(module_name: str, module_data: dict[str, ModuleInterface]) -> None:
    """Fill in missing module interface entry in module_data. Uses file caches to avoid extra processing."""
    assert project_root is not None, "project_root must be set in order to generate the interface"
    module_path = os.path.join(project_root, module_name + '.cmod')
    if not os.path.isfile(module_path):
        logging.error(f"could not find module {module_name!r} (expected {module_path!r})")
        raise ModuleNotFound(f"could not find module {module_name!r} (expected {module_path!r})")

    module_mtime = os.path.getmtime(module_path)
    cache_path = os.path.join(project_root, '.cmod', module_name + '.cmodi')
    if readCache:
        if os.path.isfile(cache_path) and os.path.getmtime(cache_path) >= module_mtime:
            with open(cache_path, 'rb') as f:
                cached_mtime, interface = pickle.load(f)
            if cached_mtime >= module_mtime:
                module_data[module_name] = interface
                module_mtimes[module_name] = cached_mtime
                return

    with open(module_path) as f:
        text = f.read()
    interface = generate_module_interface(text)
    if interface.module != module_name:
        logging.error(f"module {module_name!r} (file {module_path!r}) declares itself as {interface.module!r}")
    module_data[module_name] = interface
    module_mtimes[module_name] = module_mtime

    if storeCache:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        with open(cache_path, 'wb') as f:
            pickle.dump((module_mtime, interface), f)
