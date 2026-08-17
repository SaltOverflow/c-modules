# Symbol table used for disambiguation when parsing module files fully.
# We use global variables to communicate with ANTLR.

fileSymbolTable = {}  # dict[name: str, (is_type: bool, module_name: str)], represents symbol table at file level
localSymbolTable = []  # list[dict[name: str, is_type: bool]], represents the stack of local symbol tables
fileSymbolTableUses = []  # list[(module_name: str, name: str)], so we can figure out what is being used

def reset():
    global fileSymbolTable, localSymbolTable, fileSymbolTableUses
    fileSymbolTable = {}
    localSymbolTable = []
    fileSymbolTableUses = []

def pushScope():
    localSymbolTable.append({})

def popScope():
    localSymbolTable.pop()

def addSymbol(name: str, is_type: bool):
    if len(localSymbolTable) == 0:  # we're still at file scope, skip
        if name not in fileSymbolTable:
            # Let it keep going
            print(f"// ERROR: encountered symbol {name} not already in fileSymbolTable")
        return
    if name in localSymbolTable[-1]:
        # Let it keep going
        print(f"// ERROR: symbol name clash in local scope for {name}")
    localSymbolTable[-1][name] = is_type

def getSymbol(name: str) -> bool:  # returns is_type: bool
    for st in reversed(localSymbolTable):
        if name in st:
            return st[name]
    if name in fileSymbolTable:
        is_type, module_name = fileSymbolTable[name]
        fileSymbolTableUses.append((module_name, name))  # calling getSymbol multiple times will create duplicates, but that's ok
        return is_type
