from antlr4 import *
from parser.CParser import CParser
from parser.CListener import CListener

class ListenerTopLevel(CListener):
    def __init__(self):
        # helpers
        self.outer = []  # list[ctx], stores parent contexts (used in parsing and detecting problem contexts)
        self.variable_names = set()  # list[name:str], holds variable names from self.variables for collision detection (note: only top-level)
        # errors
        self.problem_contexts = []  # list[ctx], stores non-supported definitions (non-top level, nameless)
        self.colliding_contexts = []  # list[(name:str, ctx)], stores definitions with the same name as another
        # output
        self.functions = {}  # dict[name:str, (name_index:int, ctx:functionDefinitionContext)]
        self.structs = {}  # dict[name:str, (name_index:int, ctx:structSpecifierContext)]
        self.variables = []  # list[(list[name:str], list[name_index:int], ctx:declarationContext)], only contains top-level

    def enterFunctionDefinition(self, ctx):
        self.outer.append(ctx)
    
    def exitFunctionDefinition(self, ctx):
        should_be_ctx = self.outer.pop()
        assert(should_be_ctx is ctx)
        if self.outer:
            self.problem_contexts.append(ctx)
            return
        name, name_idx = self._extract_name_and_idx_from_declarator(ctx.declarator())
        if name in self.functions:
            self.colliding_contexts.append((name, ctx))
        else:
            self.functions[name] = name_idx, ctx

    def enterStructSpecifier(self, ctx):
        self.outer.append(ctx)
    
    def exitStructSpecifier(self, ctx):
        should_be_ctx = self.outer.pop()
        assert(should_be_ctx is ctx)
        if ctx.getChildCount() == 2:
            return  # not a struct definition
        if self.outer:
            self.problem_contexts.append(ctx)
            return
        if not ctx.Identifier():
            self.problem_contexts.append(ctx)  # anonymous struct, not supported right now
            return
        name, name_idx = ctx.Identifier().getText(), ctx.Identifier().getSourceInterval()[0]
        if name in self.structs:
            self.colliding_contexts.append((name, ctx))
        else:
            self.structs[name] = name_idx, ctx
    
    def enterDeclaration(self, ctx):
        if not ctx.initDeclaratorList() and not self._extract_name_and_idx_from_declarationSpecifiers(ctx.declarationSpecifiers()):
            return
        self.outer.append(ctx)
    
    def exitDeclaration(self, ctx):
        if not ctx.initDeclaratorList():
            name_and_idx = self._extract_name_and_idx_from_declarationSpecifiers(ctx.declarationSpecifiers())
            if not name_and_idx:
                return
        should_be_ctx = self.outer.pop()
        assert(should_be_ctx is ctx)
        if self.outer:
            return  # non-top level variable
        if not ctx.initDeclaratorList():
            names, name_idxs = zip(name_and_idx)
        else:
            name_and_idxs = [self._extract_name_and_idx_from_declarator(x.declarator()) for x in ctx.initDeclaratorList().initDeclarator()]
            names, name_idxs = zip(*name_and_idxs)
        names, name_idxs = list(names), list(name_idxs)  # unnecessary but let's keep the types
        colliding_names = self.variable_names.intersection(names)
        if colliding_names:
            self.colliding_contexts.append((colliding_names.pop(), ctx))  # could grab all the colliding names, but one is enough
        else:
            self.variable_names.update(names)
            self.variables.append((names, name_idxs, ctx))

    def _extract_name_and_idx_from_declarator(self, ctx:CParser.DeclaratorContext) -> tuple[str, int]:
        directDeclarator = ctx.directDeclarator()
        while directDeclarator.directDeclarator():
            directDeclarator = directDeclarator.directDeclarator()
        if directDeclarator.declarator():
            return self._extract_name_and_idx_from_declarator(directDeclarator.declarator())
        return directDeclarator.Identifier().getText(), directDeclarator.Identifier().getSourceInterval()[0]

    def _extract_name_and_idx_from_declarationSpecifiers(self, ctx:CParser.DeclarationSpecifiersContext) -> tuple[str, int] | None:
        typeSpecifierParsed = False
        for declarationSpecifier in ctx.declarationSpecifier():
            if not declarationSpecifier.typeSpecifier():
                continue
            if not typeSpecifierParsed:
                typeSpecifierParsed = True
            else:
                typedefName = declarationSpecifier.typeSpecifier().typedefName()
                if typedefName:
                    return typedefName.getText(), typedefName.getSourceInterval()[0]  # stuff after may be invalid, but I don't check it
        return None
        