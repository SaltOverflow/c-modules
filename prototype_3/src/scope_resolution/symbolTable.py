# Symbol table used for disambiguation when parsing module files fully.
# We use global variables to communicate with ANTLR.
# Alternatively, you could use @Parser::members in the grammar instead.

from ..interface_generation.ListenerExtractSymbolDefinitions import SymbolType
from ..interface_generation.process import Definition

fileSymbolTable = {}  # dict[(name: str, QuerySymbolType), (SymbolType, module_name: str)], represents symbol table at file level
                      # QuerySymbolType is SymbolType.STRUCT, UNION, ENUM, VARIABLE only
localSymbolTable = []  # list[dict[(name: str, QuerySymbolType), SymbolType]], represents the stack of local symbol tables
fileSymbolTableUses = []  # list[(module_name: str, name: str, SymbolType, token_idx: int)], so we can figure out what is being used
# Rest are ad-hoc patches, which work but are not robust.
# Alternatively, we could replace these with AST introspection if it becomes a problem.
declaratorType = SymbolType.VARIABLE  # DeclaratorSymbolType, used for determining the type of a declarator
                                      # DeclaratorSymbolType is SymbolType.TYPEDEF, VARIABLE, FUNCTION only
positiveIfParameter = 0  # int >= 0, declarators in parameters are always variables
functionSymbolTable = None  # dict[(name: str, QuerySymbolType), SymbolType] | None, function definitions have a scope that's split across () and {}

def reset():
    global fileSymbolTable, localSymbolTable, fileSymbolTableUses, declaratorType, positiveIfParameter, functionSymbolTable
    fileSymbolTable = {}
    localSymbolTable = []
    fileSymbolTableUses = []
    declaratorType = SymbolType.VARIABLE
    positiveIfParameter = 0
    functionSymbolTable = None

def sanityCheck(tokens: list | None = None):
    violations = 0
    if len(localSymbolTable) != 0:
        # Let it keep going
        print(f"// ERROR: localSymbolTable is not empty: {localSymbolTable}")
        violations += 1
    if positiveIfParameter != 0:
        # Let it keep going
        print(f"// ERROR: positiveIfParameter is not 0: {positiveIfParameter}")
        violations += 1
    if tokens is not None:
        for module_name, name, symbolType, token_idx in fileSymbolTableUses:
            if name != tokens[token_idx].text:
                # Let it keep going
                print(f"// ERROR: fileSymbolTableUses includes {(name, token_idx)}, which differs from {tokens[token_idx].text=}")
                violations += 1
            querySymbolType = symbolType if symbolType in (SymbolType.STRUCT, SymbolType.UNION, SymbolType.ENUM) else SymbolType.VARIABLE
            if (name, querySymbolType) not in fileSymbolTable or fileSymbolTable[(name, querySymbolType)] != (symbolType, module_name):
                # Let it keep going
                print(f"// ERROR: fileSymbolTableUses has entry {name} which doesn't exist in fileSymbolTable")
                violations += 1
    return violations == 0

def addToFileSymbolTable(module_name: str, definition_list: list[Definition], exported_only: bool):
    for name, is_exported, symbolType, _ in definition_list:
        if exported_only and not is_exported:
            continue
        querySymbolType = symbolType if symbolType in (SymbolType.STRUCT, SymbolType.UNION, SymbolType.ENUM) else SymbolType.VARIABLE
        if (name, querySymbolType) in fileSymbolTable:
            # Let it keep going
            print(f"// ERROR: fileSymbolTable collision with {(name, querySymbolType)} -> {fileSymbolTable[(name, querySymbolType)]}")
        else:
            fileSymbolTable[(name, querySymbolType)] = (symbolType, module_name)

def pushScope():
    localSymbolTable.append({})

def popScope(maybeScopeContinues: bool = False):
    global functionSymbolTable
    symbolTable = localSymbolTable.pop()
    if maybeScopeContinues and positiveIfParameter <= 0 and functionSymbolTable is None:
        functionSymbolTable = symbolTable

def pushFunctionScope():
    global functionSymbolTable
    if functionSymbolTable is None:
        # Let it keep going
        print(f"// ERROR: function does not have a parameter list!")
    localSymbolTable.append(functionSymbolTable)
    functionSymbolTable = None

def addSymbol(name: str, symbolType: SymbolType):
    querySymbolType = symbolType if symbolType in (SymbolType.STRUCT, SymbolType.UNION, SymbolType.ENUM) else SymbolType.VARIABLE
    if symbolType == SymbolType.VARIABLE:
        # This means we have a declarator, so consult internal state
        if positiveIfParameter <= 0:
            symbolType = declaratorType
    if len(localSymbolTable) == 0:  # we're still at file scope, skip
        if (name, querySymbolType) not in fileSymbolTable or fileSymbolTable[(name, querySymbolType)][0] != symbolType:
            # Let it keep going
            print(f"// ERROR: encountered symbol {(name, symbolType)} not already in fileSymbolTable")
        return
    if (name, querySymbolType) in localSymbolTable[-1]:
        # Let it keep going
        print(f"// ERROR: symbol name clash in local scope for {name}")
    else:
        localSymbolTable[-1][(name, querySymbolType)] = symbolType
        # # Debugging
        # from pprint import pprint
        # print(f"AFTER addSymbol({name=}, {symbolType=})")
        # pprint(localSymbolTable)

def getSymbol(name: str, querySymbolType: SymbolType = SymbolType.VARIABLE, token_idx: int | None = None) -> SymbolType | None:
    if querySymbolType not in (SymbolType.STRUCT, SymbolType.UNION, SymbolType.ENUM, SymbolType.VARIABLE):
        # Let it keep going
        print(f"// ERROR: implementation error, {querySymbolType=} is invalid, using VARIABLE fallback")
        querySymbolType = SymbolType.VARIABLE
    for st in reversed(localSymbolTable):
        if (name, querySymbolType) in st:
            return st[(name, querySymbolType)]
    if (name, querySymbolType) in fileSymbolTable:
        symbolType, module_name = fileSymbolTable[(name, querySymbolType)]
        if token_idx is not None:  # dependency tracking is moved to semantic actions instead of semantic predicates
            fileSymbolTableUses.append((module_name, name, symbolType, token_idx))
        return symbolType
    else:
        # No need to emit an error message: the parser's speculative lookahead often checks invalid strings
        return None

def updateDeclaratorType(declaratorSymbolType: SymbolType):
    global declaratorType
    if declaratorSymbolType not in (SymbolType.TYPEDEF, SymbolType.VARIABLE, SymbolType.FUNCTION):
        # Let it keep going
        print(f"// ERROR: implementation error, {declaratorSymbolType=} is invalid, using VARIABLE fallback")
        declaratorSymbolType = SymbolType.VARIABLE
    declaratorType = declaratorSymbolType

def enterParameterRegion():
    global positiveIfParameter
    positiveIfParameter += 1

def exitParameterRegion():
    global positiveIfParameter
    positiveIfParameter -= 1
    if positiveIfParameter < 0:
        # Let it keep going
        print(f"// ERROR: implementation error, {positiveIfParameter=} is less than 0, resetting")
        positiveIfParameter = 0
