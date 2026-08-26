from antlr4 import InputStream, CommonTokenStream
from functools import cache
from enum import Enum, auto
from typing import NamedTuple

from . import symbolTable as st
from .parser.CMODFullLexer import CMODFullLexer
from .parser.CMODFullParser import CMODFullParser
from ..interface_generation.ListenerExtractSymbolDefinitions import SymbolType

class DepType(Enum):
    # A dependency that is set as DECLARATION needs at least a declaration,
    # and the system may choose to provide the full definition instead.
    # For example: the system provides the full definition of a function because it is inline
    DECLARATION = auto()
    DEFINITION = auto()

class GraphNode(NamedTuple):
    module_name: str
    name: str
    symbolType: SymbolType  # Note that dictionary keys are restricted to QuerySymbolType
                            # dictionary values use the full SymbolType
    depType: DepType

class GraphInfo(NamedTuple):
    text: str | None
    dependencies: list[GraphNode]
    extra_text: str | None = None  # inline functions need to explicitly emit their symbol

def generate_dependency_graph(module_name: str, module_data):
    """Builds a dependency graph for a single module.
    ```
        module_data: dict[module_name: str, interface: <generate_module_interface>], should contain at least
            module_name itself and every module it imports (extra entries are ignored)
        returns: dict[GraphNode, GraphInfo]
        (the key GraphNode's symbolType field is restricted to QuerySymbolType)
    ```
    """
    interface = module_data[module_name]

    graph = {}
    for name, is_exported, symbolType, text in interface['definitions']:
        querySymbolType = st.getQuerySymbolType(symbolType)
        node_key_decl = GraphNode(module_name, name, querySymbolType, DepType.DECLARATION)
        node_key_defn = GraphNode(module_name, name, querySymbolType, DepType.DEFINITION)

        if symbolType == SymbolType.ENUM_CONSTANT:
            # text is something like "RED 0"
            enum_name = text.split(' ')[0]
            graph[node_key_decl] = GraphInfo(None, [GraphNode(module_name, enum_name, SymbolType.ENUM, DepType.DEFINITION)])
            graph[node_key_defn] = GraphInfo(None, [GraphNode(module_name, enum_name, SymbolType.ENUM, DepType.DEFINITION)])
            continue

        st.reset()
        st.addToFileSymbolTable(module_name, interface['definitions'], exported_only=False)
        for imported_name in interface['imports']:
            if imported_name not in module_data:
                print(f"// WARNING: {module_name} imports unknown module {imported_name}")
                continue
            imported_interface = module_data[imported_name]
            st.addToFileSymbolTable(imported_name, imported_interface['definitions'], exported_only=True)

        lexer = CMODFullLexer(InputStream(text))
        stream = CommonTokenStream(lexer)
        fullParser = CMODFullParser(stream)
        externalDeclaration = fullParser.externalDeclaration()
        if fullParser.getNumberOfSyntaxErrors() > 0:
            print(f"// ERROR: syntax errors parsing definition text for {node_key_defn}: {text!r}")
        st.sanityCheck()

        # Special cases for decls
        declarator_end = 0
        if symbolType == SymbolType.STRUCT:
            graph[node_key_decl] = GraphInfo(f"struct {name};", [])
        elif symbolType == SymbolType.UNION:
            graph[node_key_decl] = GraphInfo(f"union {name};", [])
        elif symbolType == SymbolType.ENUM:
            graph[node_key_decl] = GraphInfo(None, [node_key_defn])
        elif symbolType == SymbolType.TYPEDEF:
            declarator_end = len(text) - 1
        elif symbolType == SymbolType.FUNCTION:
            declarator_end = externalDeclaration.functionDefinition().declarator().stop.stop
        elif symbolType == SymbolType.VARIABLE:
            declarator_end = externalDeclaration.declaration().initDeclaratorList().initDeclarator()[0].declarator().stop.stop
        else:
            assert False, "shouldn't be reachable"

        dependencies_defn = []
        dependencies_decl = []
        for dep_module_name, dep_name, dep_symbolType, dep_identifierParent in st.fileSymbolTableUses:
            if dep_symbolType in (SymbolType.ENUM_CONSTANT, SymbolType.VARIABLE, SymbolType.FUNCTION):
                depType = DepType.DECLARATION
            else:
                depType = DepType.DECLARATION if onlyNeedsIncompleteType(dep_identifierParent.parentCtx) else DepType.DEFINITION
            dependency = GraphNode(dep_module_name, dep_name, dep_symbolType, depType)
            dependencies_defn.append(dependency)
            if dep_identifierParent.Identifier().symbol.stop <= declarator_end:
                if symbolType == SymbolType.TYPEDEF and not usesArrayType:
                    # typedef declarations don't need definitions, unless we're dealing with an array type (6.7.5.2p1)
                    dependencies_decl.append(GraphNode(dep_module_name, dep_name, dep_symbolType, DepType.DECLARATION))
                else:
                    dependencies_decl.append(dependency)
        if symbolType == SymbolType.FUNCTION and externalDeclaration.functionDefinition().declarationSpecifiers().functionSpecifier():
            extra_text = f"extern {text[:declarator_end+1]};"
        else:
            extra_text = None
        graph[node_key_defn] = GraphInfo(text, dependencies_defn, extra_text)
        if symbolType == SymbolType.TYPEDEF:
            graph[node_key_decl] = GraphInfo(text, dependencies_decl)
        elif symbolType == SymbolType.FUNCTION:
            graph[node_key_decl] = GraphInfo(f"{text[:declarator_end+1]};", dependencies_decl)
        elif symbolType == SymbolType.VARIABLE:
            graph[node_key_decl] = GraphInfo(f"extern {text[:declarator_end+1]};", dependencies_decl)

    return graph

usesArrayType = False
def onlyNeedsIncompleteType(typeSpecifier: CMODFullParser.TypeSpecifierContext) -> bool:
    # In essence, it's whether all declarators are pointers
    # When there are no declarators, it depends on more context
    # Also has side effect of assigning usesArrayType (dirty hack to handle case where array types always need complete type)
    global usesArrayType
    usesArrayType = False
    def declarator_isPointer(declarator: CMODFullParser.DeclaratorContext) -> bool:
        global usesArrayType
        if declarator.pointer() is not None:
            return True
        if (nested_declarator := declarator.directDeclarator().declarator()) is not None:
            return declarator_isPointer(nested_declarator)
        if declarator.directDeclarator().getChildCount() >= 2 and declarator.directDeclarator().getChild(1).getText() == '[':
            usesArrayType = True
        return False
    def abstractDeclarator_isPointer(abstractDeclarator: CMODFullParser.AbstractDeclaratorContext) -> bool:
        global usesArrayType
        if abstractDeclarator.pointer() is not None:
            return True
        if (abstractDeclarator_nested := abstractDeclarator.directAbstractDeclarator().abstractDeclarator()) is not None:
            return abstractDeclarator_isPointer(abstractDeclarator_nested)
        if abstractDeclarator.directAbstractDeclarator().directAbstractDeclaratorAfter()[-1].getChild(0).getText() == '[':
            usesArrayType = True
        return False
    assert type(typeSpecifier) == CMODFullParser.TypeSpecifierContext
    if type(structDeclaration := typeSpecifier.parentCtx.parentCtx) == CMODFullParser.StructDeclarationContext:
        for sd in structDeclaration.structDeclaratorList().structDeclarator():
            if sd.declarator() is None:
                continue  # meaningless case because anonymous bitfields can't use user-defined types
            if not declarator_isPointer(sd.declarator()):
                return False
        # TODO: these declarations produce warnings on GCC because they're useless. Interface generation should be updated to remove these
        #   on a related note, forward declarations link to the wrong symbol right now
        return True
    elif type(typeName := typeSpecifier.parentCtx.parentCtx) == CMODFullParser.TypeNameContext:
        if typeName.abstractDeclarator() is None:
            return False
        return abstractDeclarator_isPointer(typeName.abstractDeclarator())
    elif type(declaration := typeSpecifier.parentCtx.parentCtx) == CMODFullParser.DeclarationContext:
        if declaration.initDeclaratorList() is None:
            return True
        for id in declaration.initDeclaratorList().initDeclarator():
            if not declarator_isPointer(id.declarator()):
                return False
        return True
    elif type(parameterDeclaration := typeSpecifier.parentCtx.parentCtx) == CMODFullParser.ParameterDeclarationContext:
        if parameterDeclaration.declarator() is not None:
            return declarator_isPointer(parameterDeclaration.declarator())
        elif parameterDeclaration.abstractDeclarator() is not None:
            return abstractDeclarator_isPointer(parameterDeclaration.abstractDeclarator())
        else:
            assert False, "shouldn't be reachable"
    elif type(functionDefinition := typeSpecifier.parentCtx.parentCtx) == CMODFullParser.FunctionDefinitionContext:
        return declarator_isPointer(functionDefinition.declarator())
    else:
        assert False, "shouldn't be reachable"
