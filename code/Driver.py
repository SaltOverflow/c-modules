import argparse
import os
from pprint import pprint
from antlr4 import *
from parser.CLexer import CLexer
from parser.CParser import CParser
from ListenerTopLevel import ListenerTopLevel
from ListenerRenaming import ListenerRenaming

std_modules = {"stdio", "stdlib", "unistd"}

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="file to parse")
    parser.add_argument("-a", "--action", type=int, choices=[0, 1], default=1, help="""
                        what action to take.
                        0 = parse and output text
                        1 = parse top-level symbols
                        """)
    parser.add_argument("-r", "--project_root", help="the root folder of the project, used to generate module names")
    # parser.add_argument("-s", "--type_stub_file", help="file that stores type information, for generating type stub headers")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    if args.action == 0:
        simple_parse(args)
    elif args.action == 1:
        parse_top_level(args)
    else:
        print(f"Unknown value for {args.action=}")

def simple_parse(args):
    input_stream = FileStream(args.input_file)
    lexer = CLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.compilationUnit()
    print(tree.getText())

def parse_top_level(args):
    # args.input_file
    # args.project_root

    input_file = os.path.relpath(args.input_file, args.project_root)
    os.chdir(args.project_root)
    if input_file.endswith('.c'):
        input_file = input_file[0:len(input_file)-2]

    module_asts = {}  # dict[file_path:str, (tokens, tree)]
    module_imports = {}  # dict[file_path:str, list[(file_path:str, import_name:str)]]
    modules_to_process = [(input_file, input_file)]  # list[(file_path:str, import_name:str)]
    unknown_modules = set()  # set[(file_path:str, import_name:str)]
    not_a_module = list()  # list[(file_path:str, import_name:str)]
    while modules_to_process:
        file_path, import_name = modules_to_process.pop()
        if file_path in module_asts:
            continue
        try:
            tokens, tree = parse_file(file_path+'.c')
        except FileNotFoundError:
            unknown_modules.add((file_path, import_name))
            continue
        if not is_module(tree):
            not_a_module.append((file_path, import_name))
        module_asts[file_path] = tokens, tree
        import_names = list(all_imports(tokens, tree))
        file_path_dir = os.path.split(file_path)[0]
        import_file_paths = [os.path.normpath('./'+file_path_dir+'/'+x) for x in import_names]
        module_imports[file_path] = list(zip(import_file_paths, import_names))
        modules_to_process.extend(module_imports[file_path])

    pprint(module_imports)

    if len(not_a_module) > 1 or (len(not_a_module) == 1 and not_a_module[0][0] != input_file):
        raise RuntimeError(f"Non-modules detected ({input_file} is ok, it's the first file): {not_a_module}")
    problem_unknown_modules = []
    for file_path, import_name in unknown_modules:
        if import_name not in std_modules:
            problem_unknown_modules.append((file_path, import_name))
    if problem_unknown_modules:
        raise RuntimeError(f"Unknown module names detected: {problem_unknown_modules}")

    # Stuff after kind of needs to be redone

    module_data = {}  # dict[file_path:str, (functions, structs, variables)], see ListenerTopLevel
    module_problems = {}  # dict[file_path: str, (problem_contexts, colliding_contexts)], see ListenerTopLevel
    walker = ParseTreeWalker()
    for file_path, (_, tree) in module_asts.items():
        ltoplevel = ListenerTopLevel()
        walker.walk(ltoplevel, tree)
        module_data[file_path] = ltoplevel.functions, ltoplevel.structs, ltoplevel.variables
        if ltoplevel.problem_contexts or ltoplevel.colliding_contexts:
            module_problems[file_path] = ltoplevel.problem_contexts, ltoplevel.colliding_contexts

    if module_problems:
        raise RuntimeError(f"Module problems: {module_problems}")

    pprint(module_data)
    pprint(module_problems)

    lrenaming = ListenerRenaming(module_imports, module_data, input_file, is_module(module_asts[input_file][1]))
    walker.walk(lrenaming, module_asts[input_file][1])
    rename_list = lrenaming.rename_list  # list[(token_idx:int, new_symbol_name:str, from_module_name:str)], see ListenerRenaming
    symbol_collisions = lrenaming.symbol_collisions  # dict[symbol_name:str, (list[module_name:str], is_ambiguous:bool)], see ListenerRenaming
    used_symbol_collisions = lrenaming.used_symbol_collisions  # list[(token_idx:int, symbol_name:str)], see ListenerRenaming

    if used_symbol_collisions:
        raise RuntimeError(f"{used_symbol_collisions=}")

    pprint(rename_list)
    pprint(symbol_collisions)
    pprint(used_symbol_collisions)

def all_imports(tokens, tree):
    translationUnit = tree.getChild(0)
    if type(translationUnit) != CParser.TranslationUnitContext:
        return
    for importDeclaration in translationUnit.getChildren():
        if type(importDeclaration) != CParser.ImportDeclarationContext:
            continue
        numChildren = importDeclaration.getChildCount()
        start = importDeclaration.getChild(1).getSourceInterval()[0]
        end = importDeclaration.getChild(numChildren-2).getSourceInterval()[1] + 1
        import_name = ''.join(x.text for x in tokens[start:end])
        if import_name.startswith('"'):
            import_name = import_name[1:len(import_name)-1]
        yield import_name

def is_module(tree):
    try:
        return type(tree.getChild(0).getChild(0)) is CParser.ModuleDeclarationContext
    except AttributeError:
        return False

def parse_file(file_path):
    # Get tokens so we can regenerate the original code
    input_stream = FileStream(file_path)
    lexer = CLexer(input_stream)
    tokens = lexer.getAllTokens()
    # tokens[0].text
    #
    # FileStream is consumed, so need to reopen
    input_stream = FileStream(file_path)
    lexer = CLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.compilationUnit()
    # tree.getSourceInterval()  # eg. a,b = tree.getSourceInterval() ; ''.join(i.text for i in tokens[a:b+1])
    # tree.getChildren()
    # tree.getChildCount()
    # tree.getChild()
    #
    if parser.getNumberOfSyntaxErrors() > 0:
        raise RuntimeError(f"syntax errors for file {file_path}")
    return tokens, tree

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