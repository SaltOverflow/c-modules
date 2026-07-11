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
# walker.walk(lCodegenHelper, d.declarationSpecifiers())
# walker.walk(lCodegenHelper, d.initDeclaratorList().initDeclarator(1))
# pprint(lCodegenHelper.clip_ranges)
# pprint(lCodegenHelper.anonymous_names)
# pprint(lCodegenHelper.symbol_dependencies)
# pprint([(i, tokens[i].text) for i in range(d.getSourceInterval()[0], d.getSourceInterval()[1]+1)])

from antlr4 import *
from parser.CMODListener import CMODListener
from parser.CMODParser import CMODParser
from collections import defaultdict
from enum import StrEnum, auto

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
        self.symbol_dependencies = {kind: defaultdict(list) for kind in SymbolLookupKind}  # dict[symbol_kind: SymbolLookupKind, dict[symbol_name: str, list[idx: int]]]
        # Input values
        self.definition_name = definition_name  # name of definition to keep
        self.definition_kind = definition_kind  # and its kind
        self.anonymous_map = anonymous_map  # names for anonymous types
        # for internal computation
        self.start_clip_info: tuple[int, ParserRuleContext] | None = None

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
            idx = ctx.Identifier().getSourceInterval()[0]
            name: str = ctx.Identifier().getText()
        kind = SymbolLookupKind.STRUCT if ctx.getChild(0).getText() == 'struct' else SymbolLookupKind.ENUM
        if kind == self.definition_kind and name == self.definition_name:
            return
        self.symbol_dependencies[kind][name].append(idx)
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
            idx = ctx.Identifier().getSourceInterval()[0]
            name: str = ctx.Identifier().getText()
        kind = SymbolLookupKind.ENUM
        if kind == self.definition_kind and name == self.definition_name:
            return
        self.symbol_dependencies[kind][name].append(idx)
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
        idx = ctx.Identifier().getSourceInterval()[0]
        name = ctx.getText()
        kind = SymbolLookupKind.IDENTIFIER
        if kind == self.definition_kind and name == self.definition_name:
            return
        self.symbol_dependencies[kind][name].append(idx)

    def exitSkipTokens(self, ctx: CMODParser.SkipTokensContext):
        if self.start_clip_info is not None:
            # Listener traverses entire AST, but we want to skip clipped sections
            return
        if ctx.Identifier() is None:
            return
        idx = ctx.Identifier().getSourceInterval()[0]
        name = ctx.Identifier().getText()
        kind = SymbolLookupKind(ctx.getChild(0).getText())
        if kind == self.definition_kind and name == self.definition_name:
            return
        self.symbol_dependencies[kind][name].append(idx)
