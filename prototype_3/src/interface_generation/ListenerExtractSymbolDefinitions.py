# Grab all symbol definitions in the AST

# # Example code (execute inside src/interface_generation/)
# from antlr4 import *
# from parser.CMODInterfaceLexer import CMODInterfaceLexer
# from parser.CMODInterfaceParser import CMODInterfaceParser
# from ListenerExtractSymbolDefinitions import *
# from pprint import pprint
#
# input_stream = FileStream("../../testing/clockwiseRule.cmod")
# text = str(input_stream)
# lexer = CMODInterfaceLexer(input_stream)
# tokens = lexer.getAllTokens()
# lexer.reset()
# stream = CommonTokenStream(lexer)
# parser = CMODInterfaceParser(stream)
# tree = parser.compilationUnit()
#
# walker = ParseTreeWalker()
# lExtractSymbolDefinitions = ListenerExtractSymbolDefinitions("clockwiseRule")
# walker.walk(lExtractSymbolDefinitions, tree)
# pprint(lExtractSymbolDefinitions.symbol_definitions)

from antlr4 import *
from parser.CMODInterfaceListener import CMODInterfaceListener
from parser.CMODInterfaceParser import CMODInterfaceParser
from enum import Enum, auto
from typing import NamedTuple

class SymbolType(Enum):
    STRUCT = auto()  # ctx: StructOrUnionSpecifierContext
    UNION = auto()  # ctx: StructOrUnionSpecifierContext
    ENUM = auto()  # ctx: EnumSpecifierContext
    ENUM_CONSTANT = auto()  # ctx: EnumSpecifierContext
    TYPEDEF = auto()  # ctx: DeclarationContext
    VARIABLE = auto()  # ctx: DeclarationContext
    FUNCTION = auto()  # ctx: FunctionDefinitionContext

class SymbolInfo(NamedTuple):
    name: str
    is_exported: bool
    symbolType: SymbolType
    ctx: ParserRuleContext  # see SymbolType for disambiguation
    idx: int | None = None  # set in ENUM_CONSTANT, TYPEDEF, VARIABLE

class ListenerExtractSymbolDefinitions(CMODInterfaceListener):
    def __init__(self, module_name: str):
        super().__init__()
        self.reset(module_name)
    
    def reset(self, module_name: str):
        self.symbol_definitions: list[SymbolInfo] = []  # list[SymbolInfo]
        self.anonymous_map = {}  # dict[start_token_idx: int, str]
        # The rest are for internal computation
        self.module_name = module_name  # str, for generating fresh anoymous names
        self.anonymous_id = 0  # int
        self.enum_constant_names = []  # list[name: str], enum constants get added to symbol table
        self.export_status = False  # bool, tracks whether symbol should be exported
        self.function_prototype = False  # bool, for error diagnostics when user tries to use function prototypes in modules

    def getNameFromDeclarator(self, ctx: CMODInterfaceParser.DeclaratorContext) -> str:
        def recurseDeclarator(ctx: CMODInterfaceParser.DeclaratorContext) -> str:
            if ctx.pointer() is not None:
                self.function_prototype = False
            return recurseDirectDeclarator(ctx.directDeclarator())
        def recurseDirectDeclarator(ctx: CMODInterfaceParser.DirectDeclaratorContext) -> str:
            if ctx.Identifier():
                return ctx.Identifier().getText()
            elif ctx.declarator():
                return recurseDeclarator(ctx.declarator())
            elif ctx.directDeclarator():
                if ctx.getChild(1).getText() == '(':
                    self.function_prototype = True
                elif ctx.getChild(1).getText() == '[':
                    self.function_prototype = False
                return recurseDirectDeclarator(ctx.directDeclarator())
            else:
                # Let it keep going
                print(f"// ERROR: implementation error when parsing {repr(ctx.getText())}")
                return "error_symbol"
        self.function_prototype = False
        return recurseDeclarator(ctx)

    def enterExternalDeclaration(self, ctx: CMODInterfaceParser.ExternalDeclarationContext):
        self.export_status = ctx.getChild(0).getText() == 'export'
    
    def exitExternalDeclaration(self, ctx: CMODInterfaceParser.ExternalDeclarationContext):
        self.export_status = False

    def exitStructOrUnionSpecifier(self, ctx: CMODInterfaceParser.StructOrUnionSpecifierContext):
        if not ctx.structDeclaration():
            return
        if ctx.Identifier() is None:
            name = '_anon_' + ctx.structOrUnion().getText() + '_' + self.module_name + '_' + str(self.anonymous_id)
            self.anonymous_map[ctx.getSourceInterval()[0]] = name
            self.anonymous_id += 1
        else:
            name: str = ctx.Identifier().getText()
            if name.startswith('_anon_'):
                # Let it keep going
                print(f"// ERROR: name starts with _anon_ for {name}")
        symbolType = SymbolType.STRUCT if ctx.structOrUnion().getText() == 'struct' else SymbolType.UNION
        self.symbol_definitions.append(SymbolInfo(name, self.export_status, symbolType, ctx))
        # Nested structs are also in file-level scope (handled automatically)

    def exitEnumSpecifier(self, ctx: CMODInterfaceParser.EnumSpecifierContext):
        if ctx.enumeratorList() is None:
            return
        if ctx.Identifier() is None:
            name = '_anon_enum_' + self.module_name + '_' + str(self.anonymous_id)
            self.anonymous_map[ctx.getSourceInterval()[0]] = name
            self.anonymous_id += 1
        else:
            name: str = ctx.Identifier().getText()
            if name.startswith('_anon_'):
                # Let it keep going
                print(f"// ERROR: name starts with _anon_ for {name}")
        self.symbol_definitions.append(SymbolInfo(name, self.export_status, SymbolType.ENUM, ctx))
        # Enumeration constants are also in file-level scope
        for idx, enum_name in enumerate(self.enum_constant_names):
            self.symbol_definitions.append(SymbolInfo(enum_name, self.export_status, SymbolType.ENUM_CONSTANT, ctx, idx))
        self.enum_constant_names = []

    def exitEnumerationConstant(self, ctx: CMODInterfaceParser.EnumerationConstantContext):
        self.enum_constant_names.append(ctx.Identifier().getText())

    def exitFunctionDefinition(self, ctx: CMODInterfaceParser.FunctionDefinitionContext):
        name = self.getNameFromDeclarator(ctx.declarator())
        self.symbol_definitions.append(SymbolInfo(name, self.export_status, SymbolType.FUNCTION, ctx))

    def exitDeclaration(self, ctx: CMODInterfaceParser.DeclarationContext):
        if ctx.initDeclaratorList() is None:
            return
        symbolType = SymbolType.VARIABLE
        for storageClassSpecifier in ctx.declarationSpecifiers().storageClassSpecifier():
            if storageClassSpecifier.getText() == 'typedef':
                symbolType = SymbolType.TYPEDEF
            elif storageClassSpecifier.getText() == 'extern':
                # Let it keep going
                print(f"// ERROR: extern declarations don't actually define the symbol, for {repr(ctx.getText())}")
                return
        for idx, initDeclarator in enumerate(ctx.initDeclaratorList().initDeclarator()):
            name = self.getNameFromDeclarator(initDeclarator.declarator())
            if self.function_prototype:
                # Let it keep going
                print(f"// ERROR: found function protoype at declarator index {idx} of {repr(ctx.getText())}")
                continue
            self.symbol_definitions.append(SymbolInfo(name, self.export_status, symbolType, ctx, idx))
