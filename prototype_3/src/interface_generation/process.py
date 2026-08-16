from functools import cache
from typing import NamedTuple

from antlr4 import *

from parser.CMODInterfaceLexer import CMODInterfaceLexer
from parser.CMODInterfaceParser import CMODInterfaceParser
from ListenerExtractSymbolDefinitions import ListenerExtractSymbolDefinitions, SymbolInfo, SymbolType

class Definition(NamedTuple):
    name: str
    is_exported: bool
    symbolType: SymbolType
    text: str  # defines exactly the symbol and no others (eg. "struct foo value;"), unless symbolType is ENUM_CONSTANT (eg. "enum_name 4", where 4 is the idx)

def generate_module_interface(text: str):
    ret = {}
    text, tokens, tree = get_module_info(text)
    ret['module'] = tree.translationUnit().moduleDeclaration().getChild(1).getText()
    ret['imports'] = get_imports(text)
    symbol_list = get_symbol_list(text)
    anonymous_map = get_anonymous_map(text)

    def render_region(region_start: int, region_end: int, self_index: int) -> str:
        # symbol_list is generated from a post-order traversal, so scanning backwards from the current index gets the nested definitions
        clips = []  # list[(brace_open_idx: int, brace_close_idx: int, anon_name_or_None: str | None)]
        j = self_index - 1
        while j >= 0:
            other = symbol_list[j]
            j -= 1
            other_start, other_end = other.ctx.getSourceInterval()
            if other_start < region_start:
                break
            if other.symbolType not in (SymbolType.STRUCT, SymbolType.UNION, SymbolType.ENUM):
                continue
            if other_end > region_end:
                continue  # declarations that define multiple symbols hit this case, but we want it to keep going
            if other.ctx.Identifier() is None:
                brace_open = other.ctx.getChild(1).getSourceInterval()[0]
                anon_name = anonymous_map[other_start]
            else:
                brace_open = other.ctx.getChild(2).getSourceInterval()[0]
                anon_name = None
            brace_close = other_end
            clips.append((brace_open, brace_close, anon_name))
        clips.reverse()

        pieces = []
        token_idx = region_start
        if symbol_list[self_index].symbolType in (SymbolType.STRUCT, SymbolType.UNION, SymbolType.ENUM):
            anon_name = anonymous_map.get(region_start)
            if anon_name is not None:
                # struct/union/enum will always be the first token
                pieces.append(tokens[region_start].text + ' ' + anon_name)
                token_idx = region_start + 1
        for brace_open, brace_close, anon_name in clips:
            if token_idx <= brace_open - 1:
                pieces.append(text[tokens[token_idx].start:tokens[brace_open-1].stop+1])
            if anon_name is not None:
                if pieces and not pieces[-1][-1:].isspace():
                    pieces.append(' ')
                pieces.append(anon_name)
            token_idx = brace_close + 1
        if token_idx <= region_end:
            pieces.append(text[tokens[token_idx].start:tokens[region_end].stop+1])
        return ''.join(pieces)

    definitions = []
    for self_index, symbolInfo in enumerate(symbol_list):
        if symbolInfo.symbolType == SymbolType.ENUM_CONSTANT:
            enum_name = (symbolInfo.ctx.Identifier().getText() if symbolInfo.ctx.Identifier() is not None
                         else anonymous_map[symbolInfo.ctx.getSourceInterval()[0]])
            symbol_text = enum_name + ' ' + str(symbolInfo.idx)
        elif symbolInfo.symbolType in (SymbolType.TYPEDEF, SymbolType.VARIABLE):
            specifiers_start, specifiers_end = symbolInfo.ctx.declarationSpecifiers().getSourceInterval()
            declarator_start, declarator_end = symbolInfo.ctx.initDeclaratorList().initDeclarator(symbolInfo.idx).getSourceInterval()
            symbol_text = render_region(specifiers_start, specifiers_end, self_index)
            if not symbol_text[-1].isspace():
                symbol_text += ' '
            symbol_text += render_region(declarator_start, declarator_end, self_index) + ';'
        elif symbolInfo.symbolType == SymbolType.FUNCTION:
            region_start, region_end = symbolInfo.ctx.getSourceInterval()
            symbol_text = render_region(region_start, region_end, self_index)
        else:  # STRUCT, UNION, ENUM
            region_start, region_end = symbolInfo.ctx.getSourceInterval()
            symbol_text = render_region(region_start, region_end, self_index) + ';'
        definitions.append(Definition(symbolInfo.name, symbolInfo.is_exported, symbolInfo.symbolType, symbol_text))
    ret['definitions'] = definitions
    return ret

@cache
def get_module_info(text: str) -> tuple[str, list[Token], CMODInterfaceParser.CompilationUnitContext]:
    """Parses AST of a given module.
    ```
        text: str, tokens, tree
        tokens: list[token: {text, start, stop, line, column}]
        tree: {getSourceInterval, getChildren, getChildCount, getChild, getText}
        (stop is inclusive, just like getSourceInterval)
    ```
    """
    input_stream = InputStream(text)
    lexer = CMODInterfaceLexer(input_stream)
    tokens = lexer.getAllTokens()  # list[token: {text, start, stop, line, column}]
                                   # stop is inclusive, just like getSourceInterval
    lexer.reset()
    stream = CommonTokenStream(lexer)
    parser = CMODInterfaceParser(stream)
    tree = parser.compilationUnit()  # {getSourceInterval, getChildren, getChildCount, getChild, getText}

    if parser.getNumberOfSyntaxErrors() > 0:
        # Let it keep going with errors
        print(f"// ERROR: syntax errors for module text")
    return text, tokens, tree

@cache
def get_imports(text: str) -> list[str]:
    """Gets imports of module.
    ```
        list[module_name: str]
    ```
    """
    _, _, tree = get_module_info(text)
    import_names = []  # list[module_name: str]
    for importDeclaration in tree.translationUnit().importDeclaration():
        import_names.append(importDeclaration.Identifier().getText())
    return import_names

def get_symbol_list(text: str) -> list[SymbolInfo]:
    """Gets info for symbols of module.
    ```
        list[SymbolInfo]
    ```
    """
    return _get_symbol_data(text)[0]

def get_anonymous_map(text: str) -> dict[int, str]:
    """Gets names for anonymous types of module (side effect of get_symbol_list).
    ```
        dict[start_token_idx: int, str]
    ```
    """
    return _get_symbol_data(text)[1]

@cache
def _get_symbol_data(text: str) -> tuple[list[SymbolInfo], dict[int, str]]:
    _, _, tree = get_module_info(text)
    module_name = tree.translationUnit().moduleDeclaration().getChild(1).getText()
    walker = ParseTreeWalker()
    lExtractSymbolDefinitions = ListenerExtractSymbolDefinitions(module_name)
    walker.walk(lExtractSymbolDefinitions, tree)
    return lExtractSymbolDefinitions.symbol_definitions, lExtractSymbolDefinitions.anonymous_map
