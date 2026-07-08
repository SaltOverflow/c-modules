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
# lCodegenHelper = ListenerCodegenHelper("b", {8: "_anon_struct_0"})
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
from parser.CMODLexer import CMODLexer
from collections import defaultdict

class ListenerCodegenHelper(CMODListener):
    def __init__(self, definition_name: str, anonymous_map: dict[int, str]):
        super().__init__()
        self.reset(definition_name, anonymous_map)

    def reset(self, definition_name: str, anonymous_map: dict[int, str]):
        # Output values
        self.clip_ranges = []  # list[(start_token_idx: int, end_token_idx: int)]
        self.anonymous_names = []  # list[(idx: int, name: str)]
        self.symbol_dependencies = defaultdict(list)  # dict[symbol_name: str, list[idx: int]]
        # Input values
        self.definition_name = definition_name  # name of definition to keep
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
        if name == self.definition_name:
            return
        self.symbol_dependencies[name].append(idx)
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
        if name == self.definition_name:
            return
        self.symbol_dependencies[name].append(idx)
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
        if ctx.getText() == self.definition_name:
            return
        self.symbol_dependencies[ctx.getText()].append(ctx.getSourceInterval()[0])

    def exitSkipTokens(self, ctx: CMODParser.SkipTokensContext):
        if self.start_clip_info is not None:
            # Listener traverses entire AST, but we want to skip clipped sections
            return
        node = ctx.getChild(0)
        if node.getSymbol().type != CMODLexer.Identifier:
            return
        if node.getText() == self.definition_name:
            return
        self.symbol_dependencies[node.getText()].append(node.getSourceInterval()[0])
