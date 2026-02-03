import argparse
import os
from pprint import pprint
from antlr4 import *
from parser.CMODLexer import CMODLexer
from parser.CMODParser import CMODParser

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="file to parse")
    parser.add_argument("-r", "--project_root", help="the root folder of the project, used to generate module names. All modules, including imports, should be within this folder")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    parse_top_level(args)

def parse_top_level(args):
    # args.input_file
    # args.project_root

    # This changes the OS directory to be project_root, and removes the suffix from input_file
    # (it makes it easier to navigate the imports)
    input_file = os.path.relpath(args.input_file, args.project_root)
    os.chdir(args.project_root)
    dot_index = input_file.rfind('.')
    if dot_index < 0 or input_file[dot_index:] != '.cmod':
        raise RuntimeError("input_file must use .cmod suffix")
    input_file = input_file[:dot_index]

    # Type notes to help you understand this code
    # (it helps to have this open in another tab while reading the code)
    #
    # module_asts: dict[file_path: str, (text, tokens, tree)]
    # module_imports: dict[file_path: str, list[imported_file_path: str]]
    # text  # str
    # tokens[0].text  # start, stop, line, column
    # a, b = tree.getSourceInterval()  # getChildren, getChildCount, getChild
    #
    # module_data: dict[file_path: str, (types, variables)]
    # types, variables: dict[name: str, 
    #     (idx: int, used_names_decl, used_names_defn, is_exported: bool, AST)]
    # used_names_decl, used_names_defn: 
    #     list[(name: str, idx: int, is_variable: bool, needs_defn: bool)]
    #
    # module_input: dict[file_path: str, (type_symbol_table, var_symbol_table)]
    # type_symbol_table, var_symbol_table: dict[name: str, file_path: str]

    # This parses the input file, as well as any recursively imported modules
    # (output: module_asts, module_imports)
    module_asts = {}  # dict[file_path: str, (text, tokens, tree)]
    module_imports = {}  # dict[file_path: str, list[imported_file_path: str]]
    modules_to_process = [input_file]  # list[file_path: str]
    while modules_to_process:
        file_path = modules_to_process.pop()
        if file_path in module_asts:
            continue
        if "." in file_path:
            raise RuntimeError(f"{file_path=} contains '.', which is disallowed. Make sure {args.project_root=} contains all modules")
        input_stream = FileStream(file_path + ".cmod")
        text = str(input_stream)
        lexer = CMODLexer(input_stream)
        tokens = lexer.getAllTokens()  # list[token: {text, start, stop, line, column}]
                                       # stop is inclusive, just like getSourceInterval
        lexer.reset()
        stream = CommonTokenStream(lexer)
        parser = CMODParser(stream)
        tree = parser.compilationUnit()  # {getSourceInterval, getChildren, getChildCount, getChild}
        if parser.getNumberOfSyntaxErrors() > 0:
            raise RuntimeError(f"syntax errors for file {file_path}")
        module_asts[file_path] = text, tokens, tree

        import_names = []  # list[import_name: str]
        for importDeclaration in tree.getChild(0).getChildren():
            if type(importDeclaration) != CMODParser.ImportDeclarationContext:
                continue
            numChildren = importDeclaration.getChildCount()
            token_start, _ = importDeclaration.getChild(1).getSourceInterval()
            text_start = tokens[token_start].start
            _, token_end = importDeclaration.getChild(numChildren-2).getSourceInterval()
            input_end = tokens[token_end].stop
            import_name = text[text_start:input_end+1]
            if import_name.startswith('"'):
                import_name = import_name[1:len(import_name)-1]
            import_names.append(import_name)
        file_path_dir = os.path.split(file_path)[0]
        import_file_paths = [os.path.normpath('./'+file_path_dir+'/'+x) for x in import_names]
        module_imports[file_path] = import_file_paths
        modules_to_process.extend(module_imports[file_path])

    print("---- MODULE IMPORTS: ----")
    pprint(module_imports)

    # This analyzes each module, extracting top-level symbols
    # (output: module_data)
    module_data = {}  # dict[file_path: str, (types, variables)]
    for file_path, (_, tokens, tree) in module_asts.items():
        types, variables = {}, {}  # dict[name: str, (idx: int, used_names_decl, used_names_defn, is_exported: bool, AST)]
        if tree.translationUnit() is None:
            module_data[file_path] = types, variables
            continue
        for externalDeclaration in tree.translationUnit().externalDeclaration():
            lfd = externalDeclaration.limitedFunctionDefinition()
            lstruct = externalDeclaration.limitedStruct()
            lg = externalDeclaration.limitedGlobal()
            is_exported = tokens[externalDeclaration.getChild(0).getSourceInterval()[0]].text == 'export'
            if lfd is not None:
                used_names_decl, used_names_defn = [], []  # list[(name: str, idx: int, is_variable: bool, needs_defn: bool)]
                return_struct = lfd.limitedTypeSpecifier().Identifier()
                if return_struct is not None:
                    idx, _ = return_struct.getSourceInterval()
                    name = tokens[idx].text
                    used_names_decl.append((name, idx, False, lfd.limitedDeclarator().getChildCount() == 1))
                lpl = lfd.limitedParameterList()
                if lpl is not None:
                    lts_array = lpl.limitedTypeSpecifier()
                    ld_array = lpl.limitedDeclarator()
                    for lts, ld in zip(lts_array, ld_array):
                        used_struct = lts.Identifier()
                        if used_struct is not None:
                            idx, _ = used_struct.getSourceInterval()
                            name = tokens[idx].text
                            used_names_decl.append((name, idx, False, ld.getChildCount() == 1))
                for ls in lfd.limitedCompoundStatement().limitedStatement():
                    idx, _ = ls.Identifier().getSourceInterval()
                    name = tokens[idx].text
                    used_names_defn.append((name, idx, ls.getChildCount() == 2, ls.getChildCount() == 3))

                idx, _ = lfd.limitedDeclarator().Identifier().getSourceInterval()
                name = tokens[idx].text

                # Assume no overloading of names
                variables[name] = idx, used_names_decl, used_names_defn, is_exported, lfd
            elif lstruct is not None:
                used_names_decl, used_names_defn = [], []
                for ls in lstruct.limitedCompoundStatement().limitedStatement():
                    idx, _ = ls.Identifier().getSourceInterval()
                    name = tokens[idx].text
                    used_names_defn.append((name, idx, ls.getChildCount() == 2, ls.getChildCount() == 3))

                idx, _ = lstruct.Identifier().getSourceInterval()
                name = tokens[idx].text

                types[name] = idx, used_names_decl, used_names_defn, is_exported, lstruct
            elif lg is not None:
                used_names_decl, used_names_defn = [], []
                struct_type = lg.limitedTypeSpecifier().Identifier()
                if struct_type is not None:
                    idx, _ = struct_type.getSourceInterval()
                    name = tokens[idx].text
                    # global decls actually don't need the struct defn
                    used_names_decl.append((name, idx, False, False))
                    used_names_defn.append((name, idx, False, lg.limitedDeclarator().getChildCount() == 1))
                li = lg.limitedInitializer()
                if li is not None:
                    for identifier in li.Identifier():
                        idx, _ = identifier.getSourceInterval()
                        name = tokens[idx].text
                        used_names_defn.append((name, idx, True, False))

                idx, _ = lg.limitedDeclarator().Identifier().getSourceInterval()
                name = tokens[idx].text

                variables[name] = idx, used_names_decl, used_names_defn, is_exported, lg
        module_data[file_path] = types, variables

    print("---- MODULE DATA: ----")
    pprint(module_data)

    # This combines imported symbols to produce symbol tables for each module
    # (output: module_input)
    module_input = {}  # dict[file_path: str, (type_symbol_table, var_symbol_table)]
    for file_path, imported_file_paths in module_imports.items():
        type_symbol_table = {}  # dict[name: str, file_path: str]
        var_symbol_table = {}  # dict[name: str, file_path: str]
        for imported_file_path in imported_file_paths:
            types, variables = module_data[imported_file_path]
            # Assume no clashes (ie. overwrites)
            for name, (_, _, _, is_exported, _) in types.items():
                if is_exported:
                    type_symbol_table[name] = imported_file_path
            for name, (_, _, _, is_exported, _) in variables.items():
                if is_exported:
                    var_symbol_table[name] = imported_file_path
        types, variables = module_data[file_path]
        for name in types:
            type_symbol_table[name] = file_path
        for name in variables:
            var_symbol_table[name] = file_path
        module_input[file_path] = type_symbol_table, var_symbol_table

    print("---- MODULE INPUT: ----")
    pprint(module_input)

    # This performs a topological ordering of any needed symbols, as well as renaming them to the correct module
    # (output: module_output)
    module_output = {}  # dict[file_path: str, generated_output: str]
    for file_path in module_asts:
        already_added = {}  # dict[(file_path: str, name: str, is_variable: bool), (idx: int, is_defn: bool)]
        def is_already_added(file_path, name, is_variable: bool, trying_to_add_defn: bool):
            if (file_path, name, is_variable) in already_added:
                # This helps avoid double definitions
                if trying_to_add_defn:
                    _, is_defn = already_added[(file_path, name, is_variable)]
                    return is_defn
                else:
                    return True
            else:
                return False

        generated_parts = []  # list[symbol_output: str]
        circular_check = set()  # set[file_path, name, is_variable, is_defn: bool]
        def try_add_to_parts(file_path, name, is_variable, trying_to_add_defn, idx, used_names_decl, used_names_defn, ast):
            if is_already_added(file_path, name, is_variable, trying_to_add_defn):
                return
            if (file_path, name, is_variable, trying_to_add_defn) in circular_check:
                circular_reference_str = f"// Circular reference! {file_path}, {name}, {is_variable}, {trying_to_add_defn}"
                print(circular_reference_str)
                generated_parts.append(circular_reference_str)
                return
            circular_check.add((file_path, name, is_variable, trying_to_add_defn))

            def add_necessary_symbols(used_names_):
                for u_name, _, u_is_variable, needs_defn in used_names_:
                    if u_name not in module_input[file_path][u_is_variable]:
                        external_reference_str = f"// External reference! {file_path}, {u_name}, {u_is_variable}"
                        print(external_reference_str)
                        generated_parts.append(external_reference_str)
                        continue
                    m_file_path = module_input[file_path][u_is_variable][u_name]
                    m_idx, m_used_names_decl, m_used_names_defn, _, m_ast = module_data[m_file_path][u_is_variable][u_name]
                    try_add_to_parts(m_file_path, u_name, u_is_variable, needs_defn, m_idx, m_used_names_decl, m_used_names_defn, m_ast)
            add_necessary_symbols(used_names_decl)
            if trying_to_add_defn:
                add_necessary_symbols(used_names_defn)
            
            text, tokens, _ = module_asts[file_path]
            if trying_to_add_defn:
                token_start, token_end = ast.getSourceInterval()
                text_start = tokens[token_start].start
                input_end = tokens[token_end].stop
                symbol_output = text[text_start:input_end+1]
            else:
                token_start, _ = ast.getSourceInterval()
                text_start = tokens[token_start].start
                if type(ast) == CMODParser.LimitedFunctionDefinitionContext:
                    token_end, _ = ast.limitedCompoundStatement().getSourceInterval()
                    token_end -= 1
                    while tokens[token_end].text.isspace():
                        token_end -= 1
                    input_end = tokens[token_end].stop
                    symbol_output = text[text_start:input_end+1] + ';'
                elif type(ast) == CMODParser.LimitedGlobalContext:
                    _, token_end = ast.limitedDeclarator().getSourceInterval()
                    input_end = tokens[token_end].stop
                    extern_str = 'extern '
                    symbol_output = extern_str + text[text_start:input_end+1] + ';'
                    text_start -= len(extern_str)  # adjust text_start to make the rewriting work
                elif type(ast) == CMODParser.LimitedStructContext:
                    token_end, _ = ast.limitedCompoundStatement().getSourceInterval()
                    token_end -= 1
                    while tokens[token_end].text.isspace():
                        token_end -= 1
                    input_end = tokens[token_end].stop
                    symbol_output = text[text_start:input_end+1] + ';'
                else:
                    assert False, "This code path should not be reached"
            
            # This renaming is very unoptimized and relies on used_names_* being in order
            def full_name(file_path, name):
                return file_path.replace('/', '$') + '$$' + name
            def update_symbol_output(file_path, name, idx):
                nonlocal symbol_output
                replace_start = tokens[idx].start - text_start
                replace_end = tokens[idx].stop - text_start
                symbol_output = symbol_output[:replace_start] + full_name(file_path, name) + symbol_output[replace_end+1:]
            if trying_to_add_defn:
                for u_name, u_idx, u_is_variable, _ in reversed(used_names_defn):
                    if u_name not in module_input[file_path][u_is_variable]:
                        continue
                    m_file_path = module_input[file_path][u_is_variable][u_name]
                    update_symbol_output(m_file_path, u_name, u_idx)
            for u_name, u_idx, u_is_variable, _ in reversed(used_names_decl):
                if u_idx < idx:
                    break
                if u_name not in module_input[file_path][u_is_variable]:
                    continue
                m_file_path = module_input[file_path][u_is_variable][u_name]
                update_symbol_output(m_file_path, u_name, u_idx)
            update_symbol_output(file_path, name, idx)
            for u_name, u_idx, u_is_variable, _ in reversed(used_names_decl):
                if u_idx >= idx:
                    continue
                if u_name not in module_input[file_path][u_is_variable]:
                    continue
                m_file_path = module_input[file_path][u_is_variable][u_name]
                update_symbol_output(m_file_path, u_name, u_idx)
            generated_parts.append(symbol_output)

            already_added[(file_path, name, is_variable)] = len(generated_parts)-1, trying_to_add_defn
        
        types, variables = module_data[file_path]
        for name, (idx, used_names_decl, used_names_defn, _, ast) in types.items():
            try_add_to_parts(file_path, name, False, True, idx, used_names_decl, used_names_defn, ast)
        for name, (idx, used_names_decl, used_names_defn, _, ast) in variables.items():
            try_add_to_parts(file_path, name, True, True, idx, used_names_decl, used_names_defn, ast)
        module_output[file_path] = "\n\n".join(generated_parts)

    for file_path, generated_output in module_output.items():
        print(f"//////////////// START OF FILE {file_path} ////////////////")
        print(generated_output)

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
