# Symbol table used for disambiguation when parsing module files fully.
# We use global variables to communicate with ANTLR.
# Alternatively, you could use @Parser::members in the grammar instead.

from antlr4 import ParserRuleContext
from typing import Literal
from .. import logging
from ..interface_generation.ListenerExtractSymbolDefinitions import SymbolType, QuerySymbolType
from ..interface_generation.interface_generation import Definition

fileSymbolTable: dict[tuple[str, QuerySymbolType], tuple[SymbolType, str]] = {}  # dict[(name: str, QuerySymbolType), (SymbolType, module_name: str)], represents symbol table at file level
                      # QuerySymbolType is SymbolType.STRUCT, UNION, ENUM, VARIABLE only
localSymbolTable: list[dict[tuple[str, QuerySymbolType], tuple[SymbolType, bool]]] = []  # list[dict[(name: str, QuerySymbolType), (SymbolType, is_decl: bool)]], represents the stack of local symbol tables
fileSymbolTableUses: list[tuple[str, str, SymbolType, ParserRuleContext]] = []  # list[(module_name: str, name: str, SymbolType, identifierParent: ParserRuleContext)], so we can figure out what is being used
# Rest are ad-hoc patches, which work but are not robust.
# Alternatively, we could replace these with AST introspection if it becomes a problem.
type DeclaratorSymbolType = Literal[SymbolType.TYPEDEF, SymbolType.VARIABLE, SymbolType.FUNCTION]  # Python 3.12 syntax
declaratorType: DeclaratorSymbolType = SymbolType.VARIABLE  # DeclaratorSymbolType, used for determining the type of a declarator
positiveIfParameter = 0  # int >= 0, declarators in parameters are always variables
functionSymbolTable: dict[tuple[str, QuerySymbolType], SymbolType] | None = None  # dict[(name: str, QuerySymbolType), SymbolType] | None, function definitions have a scope that's split across () and {}
positiveIfStruct = 0  # int >= 0, declarators in struct bodies aren't part of symbol tables

def reset():
    global fileSymbolTable, localSymbolTable, fileSymbolTableUses, declaratorType, positiveIfParameter, functionSymbolTable, positiveIfStruct
    fileSymbolTable = {}
    localSymbolTable = []
    fileSymbolTableUses = []
    declaratorType = SymbolType.VARIABLE
    positiveIfParameter = 0
    functionSymbolTable = None
    positiveIfStruct = 0

def sanityCheck():
    assert len(localSymbolTable) == 0, f"localSymbolTable is not empty: {localSymbolTable}"
    assert positiveIfParameter == 0, f"{positiveIfParameter=} is not 0"
    assert positiveIfStruct == 0, f"{positiveIfStruct=} is not 0"
    for module_name, name, symbolType, identifierParent in fileSymbolTableUses:
        assert identifierParent.Identifier() is not None, f"{identifierParent=} is missing Identifier?"
        assert name == identifierParent.Identifier().getText(), f"fileSymbolTableUses has {name=}, which has a different name than {identifierParent.Identifier().getText()=}"
        querySymbolType = symbolType.toQuerySymbolType()
        assert (name, querySymbolType) in fileSymbolTable and fileSymbolTable[(name, querySymbolType)] == (symbolType, module_name), f"fileSymbolTableUses has entry {name} which doesn't exist in fileSymbolTable"

def addToFileSymbolTable(module_name: str, definition_list: list[Definition], exported_only: bool):
    for name, is_exported, symbolType, _ in definition_list:
        if exported_only and not is_exported:
            continue
        querySymbolType = symbolType.toQuerySymbolType()
        if (name, querySymbolType) in fileSymbolTable:
            logging.error(f"fileSymbolTable collision with {(name, querySymbolType)} -> {fileSymbolTable[(name, querySymbolType)]}")
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
        logging.error(f"function does not have a parameter list!")
    localSymbolTable.append(functionSymbolTable)
    functionSymbolTable = None

def addSymbol(name: str, symbolType: SymbolType):
    querySymbolType = symbolType.toQuerySymbolType()
    if symbolType == SymbolType.VARIABLE:
        # This means we have a declarator, so consult internal state
        if positiveIfParameter <= 0:
            symbolType = declaratorType
        if positiveIfStruct > 0:
            return  # declarators in struct bodies aren't part of symbol tables
    if len(localSymbolTable) == 0:  # we're still at file scope, skip
        if (name, querySymbolType) not in fileSymbolTable or fileSymbolTable[(name, querySymbolType)][0] != symbolType:
            logging.error(f"encountered symbol {(name, symbolType)} not already in fileSymbolTable")
        return
    if (name, querySymbolType) in localSymbolTable[-1] and not localSymbolTable[-1][(name, querySymbolType)][1]:
        logging.error(f"symbol name clash in local scope for {(name, querySymbolType)}")
    else:
        localSymbolTable[-1][(name, querySymbolType)] = symbolType, False
        # # Debugging
        # from pprint import pprint
        # print(f"AFTER addSymbol({name=}, {symbolType=})")
        # pprint(localSymbolTable)

def getSymbol(name: str, querySymbolType: QuerySymbolType = QuerySymbolType.Q_NAME, identifierParent: ParserRuleContext | None = None) -> SymbolType | None:
    for st in reversed(localSymbolTable):
        if (name, querySymbolType) in st:
            return st[(name, querySymbolType)][0]
    if (name, querySymbolType) in fileSymbolTable:
        symbolType, module_name = fileSymbolTable[(name, querySymbolType)]
        if identifierParent is not None:  # dependency tracking is moved to semantic actions instead of semantic predicates
            fileSymbolTableUses.append((module_name, name, symbolType, identifierParent))
        return symbolType
    else:
        # No need to emit an error message: the parser's speculative lookahead often checks invalid strings
        return None

def addForwardDeclaration(name: str, symbolType: SymbolType):
    assert symbolType in (SymbolType.STRUCT, SymbolType.UNION), f"cannot add forward declaration of type {symbolType} for {name}"
    querySymbolType = symbolType.toQuerySymbolType()
    if len(localSymbolTable) == 0:  # we're still at file scope, skip
        if (name, querySymbolType) not in fileSymbolTable or fileSymbolTable[(name, querySymbolType)][0] != symbolType:
            logging.error(f"encountered symbol {(name, symbolType)} not already in fileSymbolTable")
        return
    if (name, querySymbolType) in localSymbolTable[-1] and not localSymbolTable[-1][(name, querySymbolType)][1]:
        pass  # skip, it's already defined
    else:
        localSymbolTable[-1][(name, querySymbolType)] = symbolType, True

def updateDeclaratorType(declaratorSymbolType: DeclaratorSymbolType):
    global declaratorType, functionSymbolTable
    assert declaratorSymbolType in (SymbolType.TYPEDEF, SymbolType.VARIABLE, SymbolType.FUNCTION), f"implementation error, {declaratorSymbolType=} is invalid"
    if declaratorSymbolType == SymbolType.FUNCTION:
        functionSymbolTable = None  # Quick fix so function definition doesn't grab the parameter list of some previous variable
    declaratorType = declaratorSymbolType

def enterParameterRegion():
    global positiveIfParameter
    positiveIfParameter += 1

def exitParameterRegion():
    global positiveIfParameter
    positiveIfParameter -= 1
    assert positiveIfParameter >= 0, f"implementation error, {positiveIfParameter=} is less than 0"

def enterStructRegion():
    global positiveIfStruct
    positiveIfStruct += 1

def exitStructRegion():
    global positiveIfStruct
    positiveIfStruct -= 1
    assert positiveIfStruct >= 0, f"implementation error, {positiveIfStruct=} is less than 0"
