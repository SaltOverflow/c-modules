# # This logic was written from back when the grammar was different and we were using type-stub strategy
# # This would use top-level information of other modules to perform some renaming, but I don't think it was particularly successful (visitTerminal is essentially a CTRL-F)
# # The grammar is different now; this is kept mostly as historical and syntax reference
#
# from antlr import *
# from parser.CLexer import CLexer
# from parser.CParser import CParser
#
# input_stream = FileStream("testing/graph.c")
# lexer = CLexer(input_stream)
# tokens = lexer.getAllTokens()
# stream = CommonTokenStream(lexer)
# parser = CParser(stream)
# tree = parser.compilationUnit()
#
# walker = ParseTreeWalker()
# lrenaming = ListenerRenaming()
# walker.walk(lrenaming, tree)
# lrenaming.rename_list  # symbol_collisions, used_symbol_collisions

from antlr4 import *
from parser.CListener import CListener

# copied over from Driver because I don't want to deal with circular imports
# technically I can do all of this in Driver by token stream scanning,
#  but only because I'm doing it incorrectly rn (types and variables live in separate envs, local variables not considered)
std_modules = {"stdio", "stdlib", "unistd"}

class ListenerRenaming(CListener):
    def __init__(self, module_imports, module_data, module_name, is_module):
        # passed in (technically not used in traversal)
        self.module_imports = module_imports  # dict[file_path:str, list[(file_path:str, import_name:str)]], see Driver
        self.module_data = module_data  # dict[file_path:str, (functions, structs, variables)], see ListenerTopLevel
        self.module_name = module_name  # file_path:str
        self.is_module = is_module  # bool
        # used in traversal
        self.symbol_renaming, self.symbol_collisions = self._get_symbol_renaming()
        # output
        self.rename_list = []  # list[(token_idx:int, new_symbol_name:str, from_module_name:str)]
        self.used_symbol_collisions = []  # list[(token_idx:int, symbol_name:str)]

    def _get_symbol_renaming(self):
        symbol_renaming = {}  # dict[symbol_name:str, (new_symbol_name:str, from_module_name:str)]
        symbol_collisions = {}  # dict[symbol_name:str, (list[module_name:str], is_ambiguous:bool)]
        def new_symbol_name(symbol_name: str, module_name: str) -> str:
            return module_name.replace('/', '$') + '$$' + symbol_name
        def add_symbol(symbol_name: str, module_name: str, is_module: bool):
            if symbol_name in symbol_renaming:
                module_name_of_collision = symbol_renaming[symbol_name][1]
                is_resolvable = module_name_of_collision == self.module_name != module_name  # this has shadowing
                if symbol_name not in symbol_collisions:
                    symbol_collisions[symbol_name] = [module_name_of_collision], not is_resolvable
                symbol_collisions[symbol_name][0].append(module_name)
            else:
                symbol_renaming[symbol_name] = new_symbol_name(symbol_name, module_name) if is_module else symbol_name, module_name
        def add_data(module_name: str, is_imported: bool, is_module: bool):
            def grab_first_token(ctx) -> str:
                while ctx.getChildCount():
                    ctx = ctx.getChild(0)
                return ctx.getText()
            functions, _, variables = self.module_data[module_name]
            for name, (_, ctx) in functions.items():
                if is_imported and grab_first_token(ctx) != 'export':
                    continue
                add_symbol(name, module_name, is_module)
            # structs are always visible to the compiler, even if not exported (needed for size/align analysis)
            # There's some special logic for type stubbing, conversions and having types in separate envs, to be done later
            # Moving struct logic out to parent function to simplify logic for now
            for names, _, ctx in variables:
                if is_imported and grab_first_token(ctx) != 'export':
                    continue
                for name in names:
                    add_symbol(name, module_name, is_module)

        add_data(self.module_name, False, self.is_module)
        for name in self.module_data[self.module_name][1]:
            add_symbol(name, self.module_name, self.is_module)
        for file_path, import_name in self.module_imports[self.module_name]:
            if import_name in std_modules or file_path == self.module_name:
                continue
            add_data(file_path, True, True)
        for module_name, (_, structs, _) in self.module_data.items():
            if module_name == self.module_name:
                continue
            for name in structs:
                add_symbol(name, module_name, True)

        return symbol_renaming, symbol_collisions

    def visitTerminal(self, node):
        if node.getText() in self.symbol_renaming:
            if node.getText() in self.symbol_collisions and self.symbol_collisions[node.getText()][1]:
                self.used_symbol_collisions.append((node.getSourceInterval()[0], node.getText()))
            self.rename_list.append((node.getSourceInterval()[0], *self.symbol_renaming[node.getText()]))
