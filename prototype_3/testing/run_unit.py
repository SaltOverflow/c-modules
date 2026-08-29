# Run `python3 testing/run_unit.py` while in venv

from antlr4 import InputStream, CommonTokenStream

import src.logging as logging
from src.scope_resolution import symbolTable as st
from src.scope_resolution.parser.CMODFullLexer import CMODFullLexer
from src.scope_resolution.parser.CMODFullParser import CMODFullParser
from src.interface_generation.ListenerExtractSymbolDefinitions import SymbolType, QuerySymbolType

passed = 0
failed = 0


def check(rule_name, text, expect_errors=False, label=None, seed=None, extra_check=None):
    global passed, failed
    st.reset()
    logging.reset()
    if seed:
        seed()
    else:
        seed_basic()
    lexer = CMODFullLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = CMODFullParser(stream)
    tree = getattr(parser, rule_name)()
    if parser.getNumberOfSyntaxErrors():
        logging.error(f"syntax errors running CMODFull on {text!r}")
    st.sanityCheck()
    got_errors = logging.errorCount != 0
    if extra_check is not None:
        got_errors &= extra_check()
    ok = (got_errors == expect_errors)
    status = 'PASS' if ok else 'FAIL'
    if ok:
        passed += 1
    else:
        failed += 1
    print(f'[{status}] {label or text!r}: ({got_errors=}, {expect_errors=})')
    if not ok:
        raise "hello"
    return tree


def seed_basic():
    st.fileSymbolTable[('MyType', QuerySymbolType.Q_NAME)] = (SymbolType.TYPEDEF, 'testmod')
    st.fileSymbolTable[('foo', QuerySymbolType.Q_NAME)] = (SymbolType.FUNCTION, 'testmod')
    st.fileSymbolTable[('bar', QuerySymbolType.Q_NAME)] = (SymbolType.FUNCTION, 'testmod')
    st.fileSymbolTable[('baz', QuerySymbolType.Q_NAME)] = (SymbolType.FUNCTION, 'testmod')
    st.fileSymbolTable[('S', QuerySymbolType.Q_STRUCT)] = (SymbolType.STRUCT, 'testmod')
    st.fileSymbolTable[('U', QuerySymbolType.Q_UNION)] = (SymbolType.UNION, 'testmod')
    st.fileSymbolTable[('E', QuerySymbolType.Q_ENUM)] = (SymbolType.ENUM, 'testmod')
    st.fileSymbolTable[('f', QuerySymbolType.Q_NAME)] = (SymbolType.FUNCTION, 'testmod')


print('=== typedefs ===')
check('typeSpecifier', 'MyType', label='known typedef used as type')
check('statement', '{MyType x;}', label='typedef -> declaration')
def seed_foo_and_x():
    seed_basic()
    st.fileSymbolTable[('x', QuerySymbolType.Q_NAME)] = (SymbolType.VARIABLE, 'testmod')
def check_uses():
    values = [x[:3] for x in st.fileSymbolTableUses]
    expected = [('testmod', 'foo', SymbolType.FUNCTION), ('testmod', 'x', SymbolType.VARIABLE)]
    return values == expected
check('statement', 'foo(x);', label='function call -> expression statement', seed=seed_foo_and_x, extra_check=check_uses)

print()
print('=== structs / unions / enums (named) ===')
check('structOrUnionSpecifier', 'struct S', label='reference to known struct tag')
check('structOrUnionSpecifier', 'union U', label='reference to known union tag')
check('enumSpecifier', 'enum E', label='reference to known enum tag')
check('statement', '{struct NewTag { int x; };}', label='define brand-new struct tag')
check('statement', '{union NewUnion { int x; float y; };}', label='define brand-new union tag')

print()
print('=== structs / unions / enums (anonymous) ===')
check('structOrUnionSpecifier', 'struct { int x; }', label='anonymous struct definition')
def seed_enum_const():
    st.fileSymbolTable[('A', QuerySymbolType.Q_NAME)] = (SymbolType.ENUM_CONSTANT, 'testmod')
    st.fileSymbolTable[('B', QuerySymbolType.Q_NAME)] = (SymbolType.ENUM_CONSTANT, 'testmod')
    st.fileSymbolTable[('C', QuerySymbolType.Q_NAME)] = (SymbolType.ENUM_CONSTANT, 'testmod')
    st.fileSymbolTable[('RED', QuerySymbolType.Q_NAME)] = (SymbolType.ENUM_CONSTANT, 'testmod')
check('enumSpecifier', 'enum { A, B, C }', label='anonymous enum definition', seed=seed_enum_const)

print()
print('=== enum constants ===')
check('primaryExpression', 'RED', label='enum constant used as expression', seed=seed_enum_const)
check('statement', '{enum Color { RED, GREEN, BLUE };}', label='full enum definition with constants')

print()
print('=== function parameters / locals ===')
check('functionDefinition', 'int foo(int a, int b) { return a + b; }', label='function with int params used in body')
check('functionDefinition', 'void bar(void) { int x = 1; x = x + 1; }', label='function with local variable')
check('functionDefinition', 'int baz() { int x; { int y = x; } return x; }', label='nested block scope, inner sees outer')

print()
print('=== nested scopes / shadowing ===')
check('functionDefinition', 'void f(int x) { { int x = 2; x = x + 1; } x = 3; }', label='shadowing param in nested block')
check('functionDefinition', 'void f() { { int x = 2; x = x + 1; } x = 3; }', expect_errors=True, label='shadowing param in nested block (case 2)')
check('functionDefinition', 'void f(int x) { { x = 2; x = x + 1; } x = 3; }', label='shadowing param in nested block (case 3)')
check('statement', '{ int i = 0; for (int i = 0; i < 10; i++) { i = i; } i = i; }', label='for-loop shadowing outer local (scope pushed via statement)')

print()
print('=== for-loop declarations ===')
check('iterationStatement', 'for (int i = 0; i < 10; i++) { i = i; }', label='for with declaration in init')
check('iterationStatement', 'for (i = 0; i < 10; i++) { i = i; }', expect_errors=True, label='for without declaration, i undeclared (5 uses)')

print()
print('=== function pointers ===')
def seed_function_pointers():
    st.fileSymbolTable[('signal', QuerySymbolType.Q_NAME)] = (SymbolType.FUNCTION, 'testmod')
    st.fileSymbolTable[('fp', QuerySymbolType.Q_NAME)] = (SymbolType.VARIABLE, 'testmod')
    st.fileSymbolTable[('arr_of_fp', QuerySymbolType.Q_NAME)] = (SymbolType.VARIABLE, 'testmod')
check('functionDefinition', 'void (*signal(int sig, void (*handler)(int)))(int) { return handler; }',
      label='function returning function pointer, with function-pointer parameter', seed=seed_function_pointers)
check('declaration', 'void (*fp)(int);', label='function pointer variable declaration', seed=seed_function_pointers)
check('declaration', 'int (*arr_of_fp[3])(int, int);', label='array of function pointers', seed=seed_function_pointers)

print()
print(f'TOTAL: {passed} passed, {failed} failed')
