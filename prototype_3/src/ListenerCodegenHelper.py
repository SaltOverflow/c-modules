# Generates information such as symbols to clip when performing codegen,
# where to insert anonymous names, and a list of symbol dependencies

# # Example code (execute inside src/)
# from antlr4 import *
# from parser.CMODLexer import CMODLexer
# from parser.CMODParser import CMODParser
# from ListenerCodegenHelper import *
# from pprint import pprint
#
# input_stream = FileStream("../testing/anonymousStruct.cmod")
# text = str(input_stream)
# lexer = CMODLexer(input_stream)
# tokens = lexer.getAllTokens()
# lexer.reset()
# stream = CommonTokenStream(lexer)
# parser = CMODParser(stream)
# tree = parser.compilationUnit()
#
# walker = ParseTreeWalker()
# lCodegenHelper = ListenerCodegenHelper("b", SymbolLookupKind.IDENTIFIER, {8: "_anon_struct_0"})
# d = tree.translationUnit().externalDeclaration(0).declaration()
# lCodegenHelper.enterDeclaration(d)
# walker.walk(lCodegenHelper, d.declarationSpecifiers())
# walker.walk(lCodegenHelper, d.initDeclaratorList().initDeclarator(1))
# lCodegenHelper.exitDeclaration(d)
# pprint(lCodegenHelper.clip_ranges)
# pprint(lCodegenHelper.anonymous_names)
# pprint(lCodegenHelper.symbol_dependencies)
# pprint([(i, tokens[i].text) for i in range(d.getSourceInterval()[0], d.getSourceInterval()[1]+1)])

from antlr4 import *
from parser.CMODListener import CMODListener
from parser.CMODParser import CMODParser
from collections import defaultdict
from enum import StrEnum, auto
from typing import NamedTuple

class SymbolLookupKind(StrEnum):
    STRUCT = auto()
    UNION = auto()
    ENUM = auto()
    IDENTIFIER = auto()

    @classmethod
    def _missing_(cls, value):
        return cls.IDENTIFIER

class ListenerCodegenHelper(CMODListener):
    def __init__(self, definition_name: str, definition_kind: SymbolLookupKind, anonymous_map: dict[int, str]):
        super().__init__()
        self.reset(definition_name, definition_kind, anonymous_map)

    def reset(self, definition_name: str, definition_kind: SymbolLookupKind, anonymous_map: dict[int, str]):
        # Output values
        self.clip_ranges = []  # list[(start_token_idx: int, end_token_idx: int)]
        self.anonymous_names = []  # list[(idx: int, name: str)]
        self.symbol_dependencies = {kind: defaultdict(lambda: False) for kind in SymbolLookupKind}  # dict[symbol_kind: SymbolLookupKind, dict[symbol_name: str, needs_defn: bool]]
        # Input values
        self.definition_name = definition_name  # name of definition to keep
        self.definition_kind = definition_kind  # and its kind
        self.anonymous_map = anonymous_map  # names for anonymous types
        # for internal computation
        self.start_clip_info: tuple[int, ParserRuleContext] | None = None
        self.declaration_stack: list[ListenerCodegenHelper.SymbolDependencyInfo] = []
        self.negativeIfParentIsDefinition: int = -1

    class SymbolDependencyInfo:
        def __init__(self):
            self.name: str | None = None
            self.kind: SymbolLookupKind | None = None
            self.needs_defn: bool = False

    def pushDeclarationStack(self):
        self.declaration_stack.append(self.SymbolDependencyInfo())
    
    def popDeclarationStack(self):
        sdi = self.declaration_stack.pop()
        if sdi.kind is None or sdi.name is None:
            return
        self.symbol_dependencies[sdi.kind][sdi.name] |= sdi.needs_defn

    def enterDeclaration(self, ctx):
        self.pushDeclarationStack()
        is_extern = any(scs.getText() == 'extern' for scs in ctx.declarationSpecifiers().storageClassSpecifier())
        self.negativeIfParentIsDefinition += is_extern
    
    def exitDeclaration(self, ctx):
        self.popDeclarationStack()
        is_extern = any(scs.getText() == 'extern' for scs in ctx.declarationSpecifiers().storageClassSpecifier())
        self.negativeIfParentIsDefinition -= is_extern

    def enterStructDeclaration(self, ctx):
        self.pushDeclarationStack()

    def exitStructDeclaration(self, ctx):
        self.popDeclarationStack()

    def enterFunctionDefinition(self, ctx):
        self.pushDeclarationStack()
        self.negativeIfParentIsDefinition -= 1  # undo effect of enterParameterTypeList

    def exitFunctionDefinition(self, ctx):
        self.popDeclarationStack()
        self.negativeIfParentIsDefinition += 1

    def enterParameterDeclaration(self, ctx):
        self.pushDeclarationStack()
    
    def exitParameterDeclaration(self, ctx):
        self.popDeclarationStack(False)
    
    def enterParameterTypeList(self, ctx):
        self.negativeIfParentIsDefinition += 1
    
    def exitParameterTypeList(self, ctx):
        self.negativeIfParentIsDefinition -= 1

    def exitRootDeclarator(self, ctx: CMODParser.RootDeclaratorContext):
        is_pointer_of_type = False
        is_array_of_type = False
        def recurseDeclarator(ctx: CMODParser.DeclaratorContext):
            nonlocal is_pointer_of_type
            if ctx.pointer() is not None:
                is_pointer_of_type = True
                return
            recurseDirectDeclarator(ctx.directDeclarator())
        def recurseDirectDeclarator(ctx: CMODParser.DirectDeclaratorContext):
            nonlocal is_array_of_type
            if ctx.getChild(ctx.getChildCount()-1).getText() == ']':
                is_array_of_type = True
                return
            if ctx.declarator() is not None:
                recurseDeclarator(ctx.declarator())
        recurseDeclarator(ctx.declarator())
        if is_array_of_type:
            needs_defn = True  # C99 standard 6.7.5.2/1
        elif is_pointer_of_type:
            needs_defn = False
        else:
            needs_defn = self.negativeIfParentIsDefinition < 0
        self.declaration_stack[-1].needs_defn |= needs_defn
    
    def exitRootAbstractDeclarator(self, ctx: CMODParser.RootAbstractDeclaratorContext):
        is_pointer_of_type = False
        is_array_of_type = False
        def recurseAbstractDeclarator(ctx: CMODParser.AbstractDeclaratorContext):
            nonlocal is_pointer_of_type
            if ctx.pointer() is not None:
                is_pointer_of_type = True
                return
            if ctx.directAbstractDeclarator():
                recurseDirectAbstractDeclarator(ctx.directAbstractDeclarator())
        def recurseDirectAbstractDeclarator(ctx: CMODParser.DirectAbstractDeclaratorContext):
            nonlocal is_array_of_type
            if ctx.directAbstractDeclaratorAfter():
                directAbstractDeclaratorAfter = ctx.getChild(ctx.getChildCount()-1)
                is_array_of_type = directAbstractDeclaratorAfter.getChild(0).getText() == '['
                return
            recurseAbstractDeclarator(ctx.abstractDeclarator())
        recurseAbstractDeclarator(ctx.abstractDeclarator())
        if is_array_of_type:
            needs_defn = True  # C99 standard 6.7.5.2/1
        elif is_pointer_of_type:
            needs_defn = False
        else:
            needs_defn = self.negativeIfParentIsDefinition < 0
        self.declaration_stack[-1].needs_defn |= needs_defn

    def enterStructOrUnionSpecifier(self, ctx: CMODParser.StructOrUnionSpecifierContext):
        if self.start_clip_info is not None:
            # Listener traverses entire AST, but we want to skip clipped sections
            return
        if ctx.Identifier() is None:
            idx = ctx.getSourceInterval()[0]
            if idx not in self.anonymous_map:
                # Let it keep going
                print(f"// ERROR: implementation error, {idx} should be in anonymous_map")
                return
            name = self.anonymous_map[idx]
            self.anonymous_names.append((idx, name))
        else:
            name: str = ctx.Identifier().getText()
        kind = SymbolLookupKind.STRUCT if ctx.getChild(0).getText() == 'struct' else SymbolLookupKind.ENUM
        if kind == self.definition_kind and name == self.definition_name:
            return
        self.declaration_stack[-1].name = name
        self.declaration_stack[-1].kind = kind
        if not ctx.structDeclaration():
            return
        self.start_clip_info = ctx.getChild(1).getSourceInterval()[0], ctx

    def exitStructOrUnionSpecifier(self, ctx: CMODParser.StructOrUnionSpecifierContext):
        if self.start_clip_info is not None:
            if self.start_clip_info[1] is ctx:
                self.clip_ranges.append((self.start_clip_info[0], ctx.getSourceInterval()[1]))
                self.start_clip_info = None

    def enterEnumSpecifier(self, ctx: CMODParser.EnumSpecifierContext):
        if self.start_clip_info is not None:
            # Listener traverses entire AST, but we want to skip clipped sections
            return
        if ctx.Identifier() is None:
            idx = ctx.getSourceInterval()[0]
            if idx not in self.anonymous_map:
                # Let it keep going
                print(f"// ERROR: implementation error, {idx} should be in anonymous_map")
                return
            name = self.anonymous_map[idx]
            self.anonymous_names.append((idx, name))
        else:
            name: str = ctx.Identifier().getText()
        kind = SymbolLookupKind.ENUM
        if kind == self.definition_kind and name == self.definition_name:
            return
        self.declaration_stack[-1].name = name
        self.declaration_stack[-1].kind = kind
        if ctx.enumeratorList() is None:
            return
        self.start_clip_info = ctx.getChild(1).getSourceInterval()[0], ctx

    def exitEnumSpecifier(self, ctx: CMODParser.EnumSpecifierContext):
        if self.start_clip_info is not None:
            if self.start_clip_info[1] is ctx:
                self.clip_ranges.append((self.start_clip_info[0], ctx.getSourceInterval()[1]))
                self.start_clip_info = None

    def exitTypedefName(self, ctx: CMODParser.TypedefNameContext):
        if self.start_clip_info is not None:
            # Listener traverses entire AST, but we want to skip clipped sections
            return
        name = ctx.getText()
        kind = SymbolLookupKind.IDENTIFIER
        if kind == self.definition_kind and name == self.definition_name:
            return
        self.declaration_stack[-1].name = name
        self.declaration_stack[-1].kind = kind

    def exitSkipTokens(self, ctx: CMODParser.SkipTokensContext):
        if self.start_clip_info is not None:
            # Listener traverses entire AST, but we want to skip clipped sections
            return
        if ctx.Identifier() is None:
            return
        name = ctx.Identifier().getText()
        kind = SymbolLookupKind(ctx.getChild(0).getText())
        if kind == self.definition_kind and name == self.definition_name:
            return
        self.symbol_dependencies[kind][name] |= True
