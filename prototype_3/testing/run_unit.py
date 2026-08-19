# Run `python3 testing/run_unit.py` while in venv

from antlr4 import InputStream, CommonTokenStream

from src.scope_resolution import symbolTable as st
from src.scope_resolution.parser.CMODFullLexer import CMODFullLexer
from src.scope_resolution.parser.CMODFullParser import CMODFullParser
from src.interface_generation.ListenerExtractSymbolDefinitions import SymbolType

passed = 0
failed = 0


def check(rule_name, text, expect_errors=0, label=None, seed=None, extra_check=None):
    global passed, failed
    st.reset()
    if seed:
        seed()
    lexer = CMODFullLexer(InputStream(text))
    tokens = lexer.getAllTokens()
    lexer.reset()
    stream = CommonTokenStream(lexer)
    parser = CMODFullParser(stream)
    tree = getattr(parser, rule_name)()
    n = parser.getNumberOfSyntaxErrors()
    sane = st.sanityCheck(tokens)
    ok = (n == expect_errors) and sane
    if extra_check is not None:
        ok &= extra_check()
    status = 'PASS' if ok else 'FAIL'
    if ok:
        passed += 1
    else:
        failed += 1
    print(f'[{status}] {label or text!r}: errors={n} (expected {expect_errors})')
    return tree


def seed_basic():
    st.fileSymbolTable[('MyType', SymbolType.VARIABLE)] = (SymbolType.TYPEDEF, 'testmod')
    st.fileSymbolTable[('foo', SymbolType.VARIABLE)] = (SymbolType.FUNCTION, 'testmod')
    st.fileSymbolTable[('S', SymbolType.STRUCT)] = (SymbolType.STRUCT, 'testmod')
    st.fileSymbolTable[('U', SymbolType.UNION)] = (SymbolType.UNION, 'testmod')
    st.fileSymbolTable[('E', SymbolType.ENUM)] = (SymbolType.ENUM, 'testmod')


print('=== typedefs ===')
check('typeSpecifier', 'MyType', label='known typedef used as type', seed=seed_basic)
check('blockItem', 'MyType x;', label='typedef -> declaration', seed=seed_basic)
def seed_foo_and_x():
    seed_basic()
    st.fileSymbolTable[('x', SymbolType.VARIABLE)] = (SymbolType.VARIABLE, 'testmod')
def check_uses():
    expected = [('testmod', 'foo', SymbolType.FUNCTION, 0), ('testmod', 'x', SymbolType.VARIABLE, 2)]
    return st.fileSymbolTableUses == expected
check('blockItem', 'foo(x);', expect_errors=0, label='function call -> expression statement', seed=seed_foo_and_x, extra_check=check_uses)

print()
print('=== structs / unions / enums (named) ===')
check('structOrUnionSpecifier', 'struct S', label='reference to known struct tag', seed=seed_basic)
check('structOrUnionSpecifier', 'union U', label='reference to known union tag', seed=seed_basic)
check('enumSpecifier', 'enum E', label='reference to known enum tag', seed=seed_basic)
check('structOrUnionSpecifier', 'struct NewTag { int x; }', label='define brand-new struct tag', seed=seed_basic)
check('structOrUnionSpecifier', 'union NewUnion { int x; float y; }', label='define brand-new union tag', seed=seed_basic)

print()
print('=== structs / unions / enums (anonymous) ===')
check('structOrUnionSpecifier', 'struct { int x; }', label='anonymous struct definition', seed=seed_basic)
check('enumSpecifier', 'enum { A, B, C }', label='anonymous enum definition')

print()
print('=== enum constants ===')
def seed_enum_const():
    st.fileSymbolTable[('RED', SymbolType.VARIABLE)] = (SymbolType.ENUM_CONSTANT, 'testmod')
check('primaryExpression', 'RED', label='enum constant used as expression', seed=seed_enum_const)
check('enumerator', 'NEWCONST', label='defining a brand new enum constant')
check('enumSpecifier', 'enum Color { RED, GREEN, BLUE }', label='full enum definition with constants')

print()
print('=== function parameters / locals ===')
check('functionDefinition', 'int foo(int a, int b) { return a + b; }', label='function with int params used in body')
check('functionDefinition', 'void bar(void) { int x = 1; x = x + 1; }', label='function with local variable')
check('functionDefinition', 'int baz() { int x; { int y = x; } return x; }', label='nested block scope, inner sees outer')

print()
print('=== nested scopes / shadowing ===')
check('functionDefinition', 'void f(int x) { { int x = 2; x = x + 1; } x = 3; }', label='shadowing param in nested block')
check('statement', '{ int i = 0; for (int i = 0; i < 10; i++) { i = i; } i = i; }', label='for-loop shadowing outer local (scope pushed via statement)')

print()
print('=== for-loop declarations ===')
check('iterationStatement', 'for (int i = 0; i < 10; i++) { i = i; }', label='for with declaration in init')
check('iterationStatement', 'for (i = 0; i < 10; i++) { i = i; }', expect_errors=5, label='for without declaration, i undeclared (5 uses)')

print()
print('=== function pointers ===')
check('functionDefinition', 'void (*signal(int sig, void (*handler)(int)))(int) { return handler; }',
      label='function returning function pointer, with function-pointer parameter')
check('blockItem', 'void (*fp)(int);', label='function pointer variable declaration')
check('blockItem', 'int (*arr_of_fp[3])(int, int);', label='array of function pointers')

print()
print(f'TOTAL: {passed} passed, {failed} failed')
