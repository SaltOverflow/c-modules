import argparse
import os
from pprint import pprint
from antlr4 import *
from parser.CMODLexer import CMODLexer
from parser.CMODParser import CMODParser

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="file to parse")
    parser.add_argument("-r", "--project_root", help="the root folder of the project, used to find imported modules. All modules, including imports, should be within this folder")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    generate_code(args)

def generate_code(args):
    # args.input_file
    # args.project_root

    # This changes the OS directory to be project_root, and removes the suffix from input_file
    # (output: input_module)
    input_file = os.path.relpath(args.input_file, args.project_root)
    os.chdir(args.project_root)
    dot_index = input_file.rfind('.')
    if dot_index < 0 or input_file[dot_index:] != '.cmod':
        raise RuntimeError("input_file must use .cmod suffix")
    input_module = input_file[:dot_index]

    # Parses AST of a given module
    # (output: get_module_info())
    module_asts = {}  # dict[module_name: str, (text: str, tokens, tree)]
    def get_module_info(module_name: str):
        def insert_module_info(module_name):
            input_stream = FileStream(module_name + ".cmod")
            text = str(input_stream)
            lexer = CMODLexer(input_stream)
            tokens = lexer.getAllTokens()  # list[token: {text, start, stop, line, column}]
                                           # stop is inclusive, just like getSourceInterval
            lexer.reset()
            stream = CommonTokenStream(lexer)
            parser = CMODParser(stream)
            tree = parser.compilationUnit()  # {getSourceInterval, getChildren, getChildCount, getChild, getText}
            if parser.getNumberOfSyntaxErrors() > 0:
                # Let it keep going with errors
                print(f"// ERROR: syntax errors for file {module_name}")
            module_asts[module_name] = text, tokens, tree

        if module_name not in module_asts:
            insert_module_info(module_name)
        return module_asts[module_name]

    # Gets imports of module
    # (output: get_imports())
    module_imports = {}  # dict[module_name: str, list[module_name: str]]
    def get_imports(module_name: str):
        def insert_imports(module_name):
            _, _, tree = get_module_info(module_name)
            import_names = []  # list[module_name: str]
            for importDeclaration in tree.translationUnit().importDeclaration():
                import_names.append(importDeclaration.Identifier().getText())
            module_imports[module_name] = import_names

        if module_name not in module_imports:
            insert_imports(module_name)
        return module_imports[module_name]

    # Gets info for symbols of module
    # (output: get_symbol_list())
    module_symbols = {}  # dict[module_name: str, list[(symbol_name: str, idx: int, exported: bool)]]
    def get_symbol_list(module_name: str):
        def insert_symbol_list(module_name):
            _, _, tree = get_module_info(module_name)
            symbol_list = []  # list[(symbol_name: str, idx: int, exported: bool)]
            for idx, externalDeclaration in enumerate(tree.translationUnit().externalDeclaration()):
                if externalDeclaration.getChild(0).getText() == ';':
                    continue
                exported = externalDeclaration.getChild(0).getText() == 'export'
                structUnionDefinition = externalDeclaration.structUnionDefinition()
                typedefDefinition = externalDeclaration.typedefDefinition()
                enumDefinition = externalDeclaration.enumDefinition()
                globalDefinition = externalDeclaration.globalDefinition()
                functionDefinition = externalDeclaration.functionDefinition()
                if structUnionDefinition:
                    symbol_name = (structUnionDefinition.getChild(0).getText() + " " +
                                   structUnionDefinition.Identifier().getText())
                elif typedefDefinition:
                    symbol_name = typedefDefinition.Identifier().getText()
                elif globalDefinition:
                    symbol_name = globalDefinition.declarator().Identifier().getText()
                elif functionDefinition:
                    symbol_name = functionDefinition.declarator().Identifier().getText()
                if enumDefinition:
                    if enumDefinition.Identifier():
                        symbol_name = enumDefinition.Identifier().getText()
                        symbol_list.append((symbol_name, idx, exported))
                    for enumerator in enumDefinition.enumerator():
                        symbol_name = enumerator.Identifier().getText()
                        symbol_list.append((symbol_name, idx, exported))
                else:
                    symbol_list.append((symbol_name, idx, exported))
            module_symbols[module_name] = symbol_list

        if module_name not in module_symbols:
            insert_symbol_list(module_name)
        return module_symbols[module_name]

    # Gets info for symbols via lookup
    # (output: lookup_symbol())
    module_lookup = {}  # dict[parent_module_name: str, dict[symbol_name: str, (module_name: str, idx: int)]]
    def lookup_symbol(parent_module_name: str, symbol_name: str) -> tuple[str, int] | None:
        def generate_symbol_table(parent_module_name):
            symbol_table = {}  # dict[symbol_name: str, (module_name: str, idx: int)]
            def add_to_symbol_table(symbol_name, module_name, idx):
                if symbol_name in symbol_table:
                    # Let it keep going with errors
                    print(f"// ERROR: symbol name clash for {symbol_name}")
                else:
                    symbol_table[symbol_name] = module_name, idx
            for symbol_name, idx, _ in get_symbol_list(parent_module_name):
                add_to_symbol_table(symbol_name, parent_module_name, idx)
            for module_name in get_imports(parent_module_name):
                for symbol_name, idx, exported in get_symbol_list(module_name):
                    if exported:
                        add_to_symbol_table(symbol_name, module_name, idx)
            module_lookup[parent_module_name] = symbol_table

        if parent_module_name not in module_lookup:
            generate_symbol_table(parent_module_name)
        if symbol_name in module_lookup[parent_module_name]:
            return module_lookup[parent_module_name][symbol_name]
        else:
            # if symbol not found, hopefully it's fine
            return None

    # Generate the supporting code for a given symbol definition
    # (output: codegen())
    visited = set()  # set[(module_name: str, idx: int, is_defn: bool)]
    visiting = set()  # set[(module_name: str, idx: int, is_defn: bool)]
    typedef_decl_level = [0]  # typedef doesn't have declaration form,
                              # this makes recursions use decls (array for mutability)
    struct_defn_level = [0]  # pointer types coming from struct defns have their defns deferred
                             # this also applies to unions
    deferred_codegen = set()  # set[(module_name: str, idx: int, is_defn: bool)]
    def codegen(parent_module_name: str, idx: int, needs_defn: bool):
        def is_varfunc(module_name, idx):
            _, _, tree = get_module_info(module_name)
            externalDeclaration = tree.translationUnit().externalDeclaration(idx)
            return (externalDeclaration.globalDefinition()
                    or externalDeclaration.functionDefinition())
        def codegen_typeSpecifier_declarator(typeSpecifier, declarator):
            codegen_typeSpecifier(typeSpecifier, declarator.getChild(0).getText() != '*')
            for arraySuffix in declarator.arraySuffix():
                if arraySuffix.expression() is None:
                    continue
                codegen_expression(arraySuffix.expression())
        def codegen_typeSpecifier(typeSpecifier, uses_defn, varfunc_allowed=False):
            if typeSpecifier.Identifier() is None:
                return
            lookup_name = typeSpecifier.Identifier().getText()
            firstText = typeSpecifier.getChild(0).getText()
            if firstText == 'struct' or firstText == 'union':
                lookup_name = firstText + ' ' + lookup_name
            res = lookup_symbol(parent_module_name, lookup_name)
            if not res:
                return
            module_name, idx = res
            if is_varfunc(module_name, idx):
                if not varfunc_allowed:
                    # Let it keep going with errors
                    print(f"// ERROR: variable used in wrong place!")
                uses_defn = False  # var/func names should always be decl
            elif uses_defn == False:
                # We want to expose the underlying type defn,
                # but defer it if we're handling a struct defn (avoid false cycles)
                if struct_defn_level[0]:
                    deferred_codegen.add((module_name, idx, True))
                else:
                    uses_defn = True
            codegen(module_name, idx, uses_defn)
        def codegen_expression(expression):
            for expr in expression.expression():
                codegen_expression(expr)
            for stmt in expression.statement():
                codegen_expression(stmt.expression())
            typeSpecifier = expression.typeSpecifier()
            if typeSpecifier:
                codegen_typeSpecifier(typeSpecifier, expression.getChildCount() == 1, True)

        if typedef_decl_level[0]:
            needs_defn = False  # if we come from a typedef decl, we don't need defns
        if ((parent_module_name, idx, needs_defn) in visited
            or (parent_module_name, idx, True) in visited):
            return  # skip if we already have it (defn also counts as decl)
        if (parent_module_name, idx, needs_defn) in visiting:
            # Let it keep going with errors
            print(f"// ERROR: circular reference!")
            return
        visiting.add((parent_module_name, idx, needs_defn))

        # get symbol definition
        text, tokens, tree = get_module_info(parent_module_name)
        externalDeclaration = tree.translationUnit().externalDeclaration(idx)
        structUnionDefinition = externalDeclaration.structUnionDefinition()
        typedefDefinition = externalDeclaration.typedefDefinition()
        enumDefinition = externalDeclaration.enumDefinition()
        globalDefinition = externalDeclaration.globalDefinition()
        functionDefinition = externalDeclaration.functionDefinition()
        if structUnionDefinition:
            # call codegen on children
            if needs_defn:
                struct_defn_level[0] += 1
                for structField in structUnionDefinition.structField():
                    codegen_typeSpecifier_declarator(structField.typeSpecifier(),
                                                     structField.declarator())
                struct_defn_level[0] -= 1
            # print out declaration / definition
            token_start, token_end = structUnionDefinition.getSourceInterval()
            if not needs_defn:
                token_end = structUnionDefinition.Identifier().getSourceInterval()[1]
            text_start, text_end = tokens[token_start].start, tokens[token_end].stop
            code = text[text_start:text_end+1]
            if not needs_defn:
                code += ';'
            print(code)
        elif typedefDefinition:
            # call codegen on children
            if not needs_defn:
                typedef_decl_level[0] += 1
            codegen_expression(typedefDefinition.expression())
            if not needs_defn:
                typedef_decl_level[0] -= 1
            # print out declaration / definition
            token_start, token_end = typedefDefinition.getSourceInterval()
            text_start, text_end = tokens[token_start].start, tokens[token_end].stop
            code = text[text_start:text_end+1]
            print(code)
        elif enumDefinition:
            # For enums, defn and decl are the same
            if (parent_module_name, idx, False) in visited:
                pass
            elif (parent_module_name, idx, not needs_defn) in visiting:
                # Let it keep going with errors
                print(f"// ERROR: circular reference!")
            else:
                # call codegen on children
                # (no expressions here)
                # print out declaration / definition
                token_start, token_end = enumDefinition.getSourceInterval()
                text_start, text_end = tokens[token_start].start, tokens[token_end].stop
                code = text[text_start:text_end+1]
                print(code)
        elif globalDefinition:
            # call codegen on children
            codegen_typeSpecifier_declarator(globalDefinition.typeSpecifier(),
                                             globalDefinition.declarator())
            if needs_defn and globalDefinition.expression():
                codegen_expression(globalDefinition.expression())
            # print out declaration / definition
            token_start, token_end = globalDefinition.getSourceInterval()
            if not needs_defn:
                token_end = globalDefinition.declarator().getSourceInterval()[1]
            text_start, text_end = tokens[token_start].start, tokens[token_end].stop
            code = text[text_start:text_end+1]
            if not needs_defn:
                code = 'extern ' + code + ';'
            print(code)
        elif functionDefinition:
            # call codegen on children
            codegen_typeSpecifier_declarator(functionDefinition.typeSpecifier(),
                                             functionDefinition.declarator())
            parameterList = functionDefinition.parameterList()
            if parameterList:
                for typeSpecifier, declarator in zip(parameterList.typeSpecifier(),
                                                     parameterList.declarator()):
                    codegen_typeSpecifier_declarator(typeSpecifier, declarator)
            if needs_defn:
                for statement in functionDefinition.compoundStatement().statement():
                    codegen_expression(statement.expression())
            if functionDefinition.getChild(0).getText() == 'inline':
                deferred_codegen.add((parent_module_name, idx, True))
            # print out declaration / definition
            token_start, token_end = functionDefinition.getSourceInterval()
            if not needs_defn:
                token_end = functionDefinition.compoundStatement().getSourceInterval()[0] - 1
            text_start, text_end = tokens[token_start].start, tokens[token_end].stop
            code = text[text_start:text_end+1]
            if not needs_defn:
                code += ';'
            print(code)

        visiting.remove((parent_module_name, idx, needs_defn))
        visited.add((parent_module_name, idx, needs_defn))

        if deferred_codegen and needs_defn and not struct_defn_level:
            # deferred goes after defns, also avoids running while handling a struct defn
            # this relies on decls never recursing into defns
            deferred_codegen_copy = set()
            deferred_codegen_copy.update(deferred_codegen)
            deferred_codegen.clear()
            for module_name, idx, needs_defn in deferred_codegen_copy:
                codegen(module_name, idx, needs_defn)
    
    # Now drive codegen through the input module
    _, _, tree = get_module_info(input_module)
    for _, idx, _ in get_symbol_list(input_module):
        codegen(input_module, idx, True)

def simple_parse(input_file):
    # Used in debugging
    input_stream = FileStream(input_file)
    lexer = CMODLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CMODParser(stream)
    tree = parser.compilationUnit()
    print(tree.getText())

def details(ast):
    # Used in debugging
    print(f"Details for {repr(ast)}")
    num_auto_expand = 0
    while ast.getChildCount() == 1:
        ast = ast.getChild(0)
        num_auto_expand += 1
        print(repr(ast))
    if num_auto_expand:
        print(f"auto expanded {num_auto_expand} times")
    n = ast.getChildCount()
    print(n)
    for i in range(n):
        print()
        print(i)
        print(repr(ast.getChild(i)))
        print(ast.getChild(i).getText())

if __name__ == '__main__':
    main()
