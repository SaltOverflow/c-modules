import os
from .interface_generation import ModuleInterface, generate_module_interface
from .. import logging

lazyLoad: bool = False
project_root: str | None = None

def getInterface(module_name: str, module_data: dict[str, ModuleInterface]) -> ModuleInterface:
    if module_name not in module_data:
        if lazyLoad:
            lazyInterfaceGeneration(module_name, module_data)
    assert module_name in module_data, f"Missing interface for {module_name=}"
    return module_data[module_name]

def lazyInterfaceGeneration(module_name: str, module_data: dict[str, ModuleInterface]) -> None:
    assert project_root is not None, "project_root must be set in order to use lazy logic"
    module_path = os.path.join(project_root, module_name + '.cmod')
    if not os.path.isfile(module_path):
        logging.error(f"could not find module {module_name!r} (expected {module_path!r})")
        return
    with open(module_path) as f:
        text = f.read()
    interface = generate_module_interface(text)
    if interface.module != module_name:
        logging.error(f"module {module_name!r} (file {module_path!r}) declares itself as {interface.module!r}")
    module_data[module_name] = interface
