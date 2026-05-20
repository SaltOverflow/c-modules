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
                exported = externalDeclaration.getChild(0).getText() == 'export'
                structDefinition = externalDeclaration.structDefinition()
                globalDefinition = externalDeclaration.globalDefinition()
                functionDefinition = externalDeclaration.functionDefinition()
                if structDefinition:
                    symbol_name = structDefinition.Identifier().getText()
                elif globalDefinition:
                    symbol_name = globalDefinition.declarator().Identifier().getText()
                elif functionDefinition:
                    symbol_name = functionDefinition.declarator().Identifier().getText()
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
    visited = {}  # dict[(module_name: str, idx: int), is_defn: bool]
    visiting = set()  # set[(module_name: str, idx: int)]
    def codegen(parent_module_name: str, idx: int, needs_defn: bool):
        def codegen_type_info(typeSpecifier, uses_defn):
            struct_identifier = typeSpecifier.Identifier()
            if not struct_identifier:
                return
            res = lookup_symbol(parent_module_name, struct_identifier.getText())
            if not res:
                return
            module_name, idx = res
            codegen(module_name, idx, uses_defn)
        def codegen_expression_info(expression):
            for expr in expression.expression():
                codegen_expression_info(expr)
            typeSpecifier = expression.typeSpecifier()
            if typeSpecifier:
                codegen_type_info(typeSpecifier, expression.getChildCount() == 1)
            identifier = expression.Identifier()
            if identifier:
                res = lookup_symbol(parent_module_name, identifier.getText())
                if res:
                    module_name, idx = res
                    codegen(module_name, idx, False)

        if (parent_module_name, idx) in visited:
            # Unless we now need the definition, we can skip
            if visited[(parent_module_name, idx)] == True or not needs_defn:
                return
        if (parent_module_name, idx) in visiting:
            text, tokens, tree = get_module_info(parent_module_name)
            structDefinition = tree.translationUnit().externalDeclaration(idx).structDefinition()
            if not needs_defn and structDefinition:
                # Special case: can revisit struct as a declaration
                token_start = structDefinition.getSourceInterval()[0]
                token_end = structDefinition.Identifier().getSourceInterval()[1]
                text_start, text_end = tokens[token_start].start, tokens[token_end].stop
                code = text[text_start:text_end+1]
                code += ';'
                print(code)
                return
            else:
                # Let it keep going with errors
                print(f"// ERROR: circular reference!")
                return
        visiting.add((parent_module_name, idx))

        # get symbol definition
        text, tokens, tree = get_module_info(parent_module_name)
        externalDeclaration = tree.translationUnit().externalDeclaration(idx)
        structDefinition = externalDeclaration.structDefinition()
        globalDefinition = externalDeclaration.globalDefinition()
        functionDefinition = externalDeclaration.functionDefinition()
        if structDefinition:
            # call codegen on children
            if needs_defn:
                for structField in structDefinition.structField():
                    codegen_type_info(structField.typeSpecifier(),
                                      structField.declarator().getChildCount() == 1)
            # print out declaration / definition
            token_start, token_end = structDefinition.getSourceInterval()
            if not needs_defn:
                token_end = structDefinition.Identifier().getSourceInterval()[1]
            text_start, text_end = tokens[token_start].start, tokens[token_end].stop
            code = text[text_start:text_end+1]
            if not needs_defn:
                code += ';'
            print(code)
        elif globalDefinition:
            # call codegen on children
            codegen_type_info(globalDefinition.typeSpecifier(),
                              globalDefinition.declarator().getChildCount() == 1)
            if needs_defn and globalDefinition.expression():
                codegen_expression_info(globalDefinition.expression())
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
            codegen_type_info(functionDefinition.typeSpecifier(),
                              functionDefinition.declarator().getChildCount() == 1)
            parameterList = functionDefinition.parameterList()
            if parameterList:
                for typeSpecifier, declarator in zip(parameterList.typeSpecifier(),
                                                     parameterList.declarator()):
                    codegen_type_info(typeSpecifier, declarator.getChildCount() == 1)
            if needs_defn:
                for statement in functionDefinition.compoundStatement().statement():
                    codegen_expression_info(statement.expression())
            # print out declaration / definition
            token_start, token_end = functionDefinition.getSourceInterval()
            if not needs_defn:
                token_end = functionDefinition.compoundStatement().getSourceInterval()[0] - 1
            text_start, text_end = tokens[token_start].start, tokens[token_end].stop
            code = text[text_start:text_end+1]
            if not needs_defn:
                code += ';'
            print(code)

        visiting.remove((parent_module_name, idx))
        visited[(parent_module_name, idx)] = needs_defn
    
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
