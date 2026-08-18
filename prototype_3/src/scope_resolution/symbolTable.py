# Symbol table used for disambiguation when parsing module files fully.
# We use global variables to communicate with ANTLR.

from ..interface_generation.ListenerExtractSymbolDefinitions import SymbolType
from ..interface_generation.process import Definition

fileSymbolTable = {}  # dict[(name: str, QuerySymbolType), (SymbolType, module_name: str)], represents symbol table at file level
                      # QuerySymbolType is SymbolType.STRUCT, UNION, ENUM, VARIABLE only
localSymbolTable = []  # list[dict[(name: str, QuerySymbolType), SymbolType]], represents the stack of local symbol tables
fileSymbolTableUses = []  # list[(module_name: str, name: str, SymbolType)], so we can figure out what is being used

def reset():
    global fileSymbolTable, localSymbolTable, fileSymbolTableUses
    fileSymbolTable = {}
    localSymbolTable = []
    fileSymbolTableUses = []

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

def popScope():
    localSymbolTable.pop()

def addSymbol(name: str, symbolType: SymbolType):
    querySymbolType = symbolType if symbolType in (SymbolType.STRUCT, SymbolType.UNION, SymbolType.ENUM) else SymbolType.VARIABLE
    if len(localSymbolTable) == 0:  # we're still at file scope, skip
        if name not in fileSymbolTable or fileSymbolTable[(name, querySymbolType)][0] != symbolType:
            # Let it keep going
            print(f"// ERROR: encountered symbol {(name, symbolType)} not already in fileSymbolTable")
        return
    if (name, querySymbolType) in localSymbolTable[-1]:
        # Let it keep going
        print(f"// ERROR: symbol name clash in local scope for {name}")
    else:
        localSymbolTable[-1][(name, querySymbolType)] = symbolType

def getSymbol(name: str, querySymbolType: SymbolType = SymbolType.VARIABLE) -> SymbolType | None:
    if querySymbolType not in (SymbolType.STRUCT, SymbolType.UNION, SymbolType.ENUM, SymbolType.VARIABLE):
        # Let it keep going
        print(f"// ERROR: implementation error, {querySymbolType=} is invalid, using VARIABLE fallback")
        querySymbolType = SymbolType.VARIABLE
    for st in reversed(localSymbolTable):
        if (name, querySymbolType) in st:
            return st[(name, querySymbolType)]
    if (name, querySymbolType) in fileSymbolTable:
        symbolType, module_name = fileSymbolTable[(name, querySymbolType)]
        fileSymbolTableUses.append((module_name, name, symbolType))  # calling getSymbol multiple times will create duplicates, but that's ok
        return symbolType
    else:
        # No need to emit an error message: the parser's speculative lookahead often checks invalid strings
        return None
