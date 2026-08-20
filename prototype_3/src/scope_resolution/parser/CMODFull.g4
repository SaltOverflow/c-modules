// C99 grammar was originally taken from Annex A of C99 standard ( https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf ) and edited.
// Notable differences: module syntax (ie. module, import, export) added, digraphs/trigraphs/K&R syntax removed.
// Here, we perform a full parse by leveraging the symbol table, which should be initialized prior to calling into CMODFull.

grammar CMODFull;

// Used as reference to set up semantic actions: https://martinlwx.github.io/en/how-to-use-antlr4-to-make-semantic-actions/
// Also see https://github.com/antlr/antlr4/blob/dev/doc/actions.md and https://github.com/antlr/antlr4/blob/dev/doc/predicates.md
@header {
from src.scope_resolution.symbolTable import pushScope, popScope, pushFunctionScope, addSymbol, getSymbol, updateDeclaratorType, enterParameterRegion, exitParameterRegion, enterStructRegion, exitStructRegion
from src.interface_generation.ListenerExtractSymbolDefinitions import SymbolType
}

// A.1 Lexical grammar

token
    : keyword
    | Identifier
    | constant
    | StringLiteral
    | punctuator
    ;

keyword
    : 'auto' | 'break' | 'case' | 'char' | 'const' | 'continue' | 'default' | 'do' | 'double' | 'else'
    | 'enum' | 'extern' | 'float' | 'for' | 'goto' | 'if' | 'inline' | 'int' | 'long' | 'register'
    | 'restrict' | 'return' | 'short' | 'signed' | 'sizeof' | 'static' | 'struct' | 'switch' | 'typedef' | 'union'
    | 'unsigned' | 'void' | 'volatile' | 'while' | '_Bool' | '_Complex' | '_Imaginary'
    | 'module' | 'import' | 'export'
    ;

Identifier
    : IdentifierNondigit (IdentifierNondigit | Digit)*
    ;

fragment IdentifierNondigit
    : Nondigit
    | UniversalCharacterName
    ;

fragment Nondigit
    : [a-zA-Z_]
    ;

fragment Digit
    : [0-9]
    ;

fragment UniversalCharacterName
    : '\\u' HexQuad
    | '\\U' HexQuad HexQuad
    ;

fragment HexQuad
    : HexadecimalDigit HexadecimalDigit HexadecimalDigit HexadecimalDigit
    ;

constant
    : IntegerConstant
    | FloatingConstant
    // See https://github.com/antlr/antlr4/blob/dev/doc/actions.md for a list of attributes on $enumerationConstant
    | {getSymbol(self._input.LT(1).text) == SymbolType.ENUM_CONSTANT}?
      enumerationConstant
      {getSymbol($enumerationConstant.text, token_idx=$enumerationConstant.start.tokenIndex)}
    | CharacterConstant
    ;

IntegerConstant
    : DecimalConstant IntegerSuffix?
    | OctalConstant IntegerSuffix?
    | HexadecimalConstant IntegerSuffix?
    ;

fragment DecimalConstant
    : NonzeroDigit Digit*
    ;

fragment OctalConstant
    : '0' OctalDigit*
    ;

fragment HexadecimalConstant
    : HexadecimalPrefix HexadecimalDigit+
    ;

fragment HexadecimalPrefix
    : '0x' | '0X'
    ;

fragment NonzeroDigit
    : [1-9]
    ;

fragment OctalDigit
    : [0-7]
    ;

fragment HexadecimalDigit
    : [0-9a-fA-F]
    ;

fragment IntegerSuffix
    : UnsignedSuffix (LongSuffix | LongLongSuffix)?
    | (LongSuffix | LongLongSuffix) UnsignedSuffix?
    ;

fragment UnsignedSuffix
    : 'u' | 'U'
    ;

fragment LongSuffix
    : 'l' | 'L'
    ;

fragment LongLongSuffix
    : 'll' | 'LL'
    ;

FloatingConstant
    : DecimalFloatingConstant
    | HexadecimalFloatingConstant
    ;

fragment DecimalFloatingConstant
    : FractionalConstant ExponentPart? FloatingSuffix?
    | DigitSequence ExponentPart FloatingSuffix?
    ;

fragment HexadecimalFloatingConstant
    : HexadecimalPrefix (HexadecimalFractionalConstant | HexadecimalDigitSequence) BinaryExponentPart FloatingSuffix?
    ;

fragment FractionalConstant
    : DigitSequence? '.' DigitSequence
    | DigitSequence '.'
    ;

fragment ExponentPart
    : ('e' | 'E') ('+' | '-')? DigitSequence
    ;

fragment DigitSequence
    : Digit+
    ;

fragment HexadecimalFractionalConstant
    : HexadecimalDigitSequence? '.' HexadecimalDigitSequence
    | HexadecimalDigitSequence '.'
    ;

fragment BinaryExponentPart
    : ('p' | 'P') ('+' | '-')? DigitSequence
    ;

fragment HexadecimalDigitSequence
    : HexadecimalDigit+
    ;

fragment FloatingSuffix
    : 'f' | 'l' | 'F' | 'L'
    ;

enumerationConstant
    // add/getSymbol is handled by callers of this rule
    : Identifier
    ;

CharacterConstant
    : '\'' CChar+ '\''
    | 'L\'' CChar+ '\''
    ;

fragment CChar
    : ~['\\\n\r]
    | EscapeSequence
    ;
fragment EscapeSequence
    : SimpleEscapeSequence
    | OctalEscapeSequence
    | HexadecimalEscapeSequence
    | UniversalCharacterName
    ;

fragment SimpleEscapeSequence
    : '\\\'' | '\\"' | '\\?' | '\\\\'
    | '\\a' | '\\b' | '\\f' | '\\n' | '\\r' | '\\t' | '\\v'
    ;

fragment OctalEscapeSequence
    : '\\' OctalDigit OctalDigit? OctalDigit?
    ;

fragment HexadecimalEscapeSequence
    : '\\x' HexadecimalDigit+
    ;

StringLiteral
    : '"' SChar* '"'
    | 'L"' SChar* '"'
    ;

fragment SChar
    : ~["\\\r\n]
    | EscapeSequence
    ;

punctuator
    : '[' | ']' | '(' | ')' | '{' | '}' | '.' | '->'
    | '++' | '--' | '&' | '*' | '+' | '-' | '~' | '!'
    | '/' | '%' | '<<' | '>>' | '<' | '>' | '<=' | '>=' | '==' | '!=' | '^' | '|' | '&&' | '||'
    | '?' | ':' | ';' | '...'
    | '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|='
    | ','
    // We don't support digraphs/trigraphs
    ;

// A.2 Phrase structure grammar

// A.2.1 Expressions

primaryExpression
    // See https://github.com/antlr/antlr4/blob/dev/doc/actions.md for a list of attributes on $Identifier
    // Annoyingly, they use .index instead of tokenIndex, which differs from CommonToken fields
    : {getSymbol(self._input.LT(1).text) in (SymbolType.VARIABLE, SymbolType.FUNCTION)}?
      Identifier
      {getSymbol($Identifier.text, token_idx=$Identifier.index)}
    | constant
    | StringLiteral
    | '(' expression ')'
    ;

postfixExpression
    : primaryExpression
    | postfixExpression '[' expression ']'
    | postfixExpression '(' argumentExpressionList? ')'
    | postfixExpression '.' Identifier
    | postfixExpression '->' Identifier
    | postfixExpression '++'
    | postfixExpression '--'
    | '(' typeName ')' '{' initializerList ','? '}'
    ;

argumentExpressionList
    : assignmentExpression (',' assignmentExpression)*
    ;

unaryExpression
    : postfixExpression
    | '++' unaryExpression
    | '--' unaryExpression
    | unaryOperator castExpression
    | 'sizeof' unaryExpression
    | 'sizeof' '(' typeName ')'
    ;

unaryOperator
    : '&' | '*' | '+' | '-' | '~' | '!'
    ;

castExpression
    : unaryExpression
    | '(' typeName ')' castExpression
    ;

multiplicativeExpression
    : castExpression
    | multiplicativeExpression ('*' | '/' | '%') castExpression
    ;

additiveExpression
    : multiplicativeExpression
    | additiveExpression ('+' | '-') multiplicativeExpression
    ;

shiftExpression
    : additiveExpression
    | shiftExpression ('<<' | '>>') additiveExpression
    ;

relationalExpression
    : shiftExpression
    | relationalExpression ('<' | '>' | '<=' | '>=') shiftExpression
    ;

equalityExpression
    : relationalExpression
    | equalityExpression ('==' | '!=') relationalExpression
    ;

andExpression
    : equalityExpression
    | andExpression '&' equalityExpression
    ;

exclusiveOrExpression
    : andExpression
    | exclusiveOrExpression '^' andExpression
    ;

inclusiveOrExpression
    : exclusiveOrExpression
    | inclusiveOrExpression '|' exclusiveOrExpression
    ;

logicalAndExpression
    : inclusiveOrExpression
    | logicalAndExpression '&&' inclusiveOrExpression
    ;

logicalOrExpression
    : logicalAndExpression
    | logicalOrExpression '||' logicalAndExpression
    ;

conditionalExpression
    : logicalOrExpression
    | logicalOrExpression '?' expression ':' conditionalExpression
    ;

assignmentExpression
    : conditionalExpression
    | unaryExpression assignmentOperator assignmentExpression
    ;

assignmentOperator
    : '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|='
    ;

expression
    : assignmentExpression (',' assignmentExpression)*
    ;

constantExpression
    : conditionalExpression
    ;

// A.2.2 Declarations

declaration
    : {updateDeclaratorType(SymbolType.VARIABLE)}
      declarationSpecifiers initDeclaratorList? ';'
    ;

declarationSpecifiers
    // Restrict to at most one typedef name (see constraint 6.7.2p2)
    : (storageClassSpecifier | typeQualifier | functionSpecifier)* typeSpecifier (storageClassSpecifier | typeQualifier | functionSpecifier)*
    ;

initDeclaratorList
    : initDeclarator (',' initDeclarator)*
    ;

initDeclarator
    : declarator ('=' initializer)?
    ;

storageClassSpecifier
    : 'typedef'
      {updateDeclaratorType(SymbolType.TYPEDEF)}
    | 'extern' | 'static' | 'auto' | 'register'
    ;

typeSpecifier
    // Grammar augmented with constraint 6.7.2p2 to avoid multiple typedefNames
    // Technically, "long const long" is valid, so this is not fully standard. I choose not to support this
    : 'void'
    | ('signed' | 'unsigned')? 'char'
    | ('signed' | 'unsigned')? 'short' 'int'?
    | ('signed' | 'unsigned')? 'int'
    | 'signed' | 'unsigned'
    | ('signed' | 'unsigned')? 'long' 'int'?
    | ('signed' | 'unsigned')? 'long' 'long' 'int'?
    | 'float' | 'double' | 'long' 'double'
    | '_Bool'
    | ('float' | 'double' | 'long' 'double') '_Complex'
    | structOrUnionSpecifier | enumSpecifier | typedefName
    ;

structOrUnionSpecifier
    : structOrUnion Identifier? '{'
      {if $Identifier is not None: addSymbol($Identifier.text, SymbolType.STRUCT if $structOrUnion.text == 'struct' else SymbolType.UNION)}
      {enterStructRegion()}
      structDeclaration+ '}'
      {exitStructRegion()}
    | {(self._input.LT(1).text == 'struct' and getSymbol(self._input.LT(2).text, SymbolType.STRUCT) == SymbolType.STRUCT
        or self._input.LT(1).text == 'union' and getSymbol(self._input.LT(2).text, SymbolType.UNION) == SymbolType.UNION)}?
      structOrUnion Identifier
      {getSymbol($Identifier.text, SymbolType.STRUCT if $structOrUnion.text == 'struct' else SymbolType.UNION, token_idx=$Identifier.index)}
    ;

structOrUnion
    : 'struct' | 'union'
    ;

structDeclaration
    : specifierQualifierList structDeclaratorList ';'
    ;

specifierQualifierList
    // Restrict to at most one typedef name (see constraint 6.7.2p2)
    : typeQualifier* typeSpecifier typeQualifier*
    ;

structDeclaratorList
    : structDeclarator (',' structDeclarator)*
    ;

structDeclarator
    : declarator
    | declarator? ':' constantExpression
    ;

enumSpecifier
    : 'enum' Identifier? '{'
      {if $Identifier is not None: addSymbol($Identifier.text, SymbolType.ENUM)}
      enumeratorList ','? '}'
    | {getSymbol(self._input.LT(2).text, SymbolType.ENUM) == SymbolType.ENUM}?
      'enum' Identifier
      {getSymbol($Identifier.text, SymbolType.ENUM, token_idx=$Identifier.index)}
    ;

enumeratorList
    : enumerator (',' enumerator)*
    ;

enumerator
    : enumerationConstant
      {addSymbol($enumerationConstant.text, SymbolType.ENUM_CONSTANT)}
      ('=' constantExpression)?
    ;

typeQualifier
    : 'const' | 'restrict' | 'volatile'
    ;

functionSpecifier
    : 'inline'
    ;

declarator
    : pointer? directDeclarator
    ;

directDeclarator
    // ANTLR's powerful prediction + semantic predicates allows us to grab the correct declaratorType context,
    // (when parsing a function definition, it doesn't try parsing a declaration before backing out)
    // It's not the most robust implementation, but it works for now
    : Identifier
      {addSymbol($Identifier.text, SymbolType.VARIABLE)}
    | '(' declarator ')'
    | directDeclarator '[' typeQualifierList? assignmentExpression? ']'
    | directDeclarator '[' 'static' typeQualifierList? assignmentExpression ']'
    | directDeclarator '[' typeQualifierList 'static' assignmentExpression ']'
    | directDeclarator '[' typeQualifierList? '*' ']'
    | directDeclarator '('
      {pushScope()}
      {enterParameterRegion()}
      parameterTypeList? ')'
      {exitParameterRegion()}
      {popScope(True)}  // order matters here because we want to store the parameters of the function definition
    // | directDeclarator '(' identifierList? ')'  // We don't support K&R syntax
    ;

pointer
    : ('*' typeQualifierList?)+
    ;

typeQualifierList
    : typeQualifier+
    ;

parameterTypeList
    : parameterList
    | parameterList ',' '...'
    ;

parameterList
    // The parameter list might be empty, so we move scope work to directDeclarator and directAbstractDeclaratorAfter
    : parameterDeclaration (',' parameterDeclaration)*
    ;

parameterDeclaration
    : declarationSpecifiers declarator
    | declarationSpecifiers abstractDeclarator?
    ;

typeName
    : specifierQualifierList abstractDeclarator?
    ;

abstractDeclarator
    : pointer
    | pointer? directAbstractDeclarator
    ;

directAbstractDeclarator
    : ('(' abstractDeclarator ')' | directAbstractDeclaratorAfter) directAbstractDeclaratorAfter*
    ;

directAbstractDeclaratorAfter
    : '[' typeQualifierList? assignmentExpression? ']'
    | '[' 'static' typeQualifierList? assignmentExpression ']'
    | '[' typeQualifierList 'static' assignmentExpression ']'
    | '[' '*' ']'
    | '('
      {pushScope()}
      {enterParameterRegion()}
      parameterTypeList? ')'
      {exitParameterRegion()}
      {popScope(False)}  // order doesn't technically matter here because it's never part of function scope
    ;

typedefName
    : {getSymbol(self._input.LT(1).text) == SymbolType.TYPEDEF}?
      Identifier
      {getSymbol($Identifier.text, token_idx=$Identifier.index)}
    ;

initializer
    : assignmentExpression
    | '{' initializerList ','? '}'
    ;

initializerList
    : designation? initializer (',' designation? initializer)*
    ;

designation
    : designator+ '='
    ;

designator
    : '[' constantExpression ']'
    | '.' Identifier
    ;

// A.2.3 Statements

statement
    : labeledStatement
    | {pushScope()}
      compoundStatement
      {popScope()}
    | expressionStatement
    | selectionStatement
    | iterationStatement
    | jumpStatement
    ;

labeledStatement
    : Identifier ':' statement
    | 'case' constantExpression ':' statement
    | 'default' ':' statement
    ;

compoundStatement
    // Scope is handled by the callers of this rule
    : '{' blockItemList? '}'
    ;

blockItemList
    : blockItem+
    ;

blockItem
    // the order of statement and declaration needed to be swapped from the original grammar
    // I think it's a bug in ANTLR (using 4.13.2), probably caused by the * in declarationSpecifiers
    // With the original order, it processes the semantic predicate for expressionStatement `d;`,
    // then claims "no viable alternative" (I presume it was only considering declaration)
    // Interestingly, I don't see this happen if I swap the order of the for loop rule
    : statement
    | declaration
    ;

expressionStatement
    : expression? ';'
    ;

selectionStatement
    // ANTLR handles dangling else here (binds to closest if statement)
    : 'if' '(' expression ')' statement ('else' statement)?
    | 'switch' '(' expression ')' statement
    ;

iterationStatement
    : 'while' '(' expression ')' statement
    | 'do' statement 'while' '(' expression ')' ';'
    // ANTLR's powerful prediction + semantic predicates allows us to avoid the scenario
    // where the parser backtracks between pushScope() and popScope().
    // It's not the most robust implementation, but it works for now
    | 'for' '(' expression? ';' expression? ';' expression? ')' statement
    | 'for' '('
      {pushScope()}
      declaration expression? ';' expression? ')' statement
      {popScope()}
    ;

jumpStatement
    : 'goto' Identifier ';'
    | 'continue' ';'
    | 'break' ';'
    | 'return' expression? ';'
    ;

// A.2.4 External definitions

compilationUnit
    : translationUnit EOF
    ;

translationUnit
    : moduleDeclaration importDeclaration* externalDeclaration*
    ;

moduleDeclaration
    : 'module' Identifier ';'
    ;

importDeclaration
    : 'import' Identifier ';'
    ;

externalDeclaration
    : 'export'? (functionDefinition | declaration)
    ;

functionDefinition
    // We don't support K&R syntax, so declarationList is removed
    : {updateDeclaratorType(SymbolType.FUNCTION)}
      declarationSpecifiers declarator
      {pushFunctionScope()}
      compoundStatement
      {popScope()}
    ;

// Comments and whitespace

Whitespace
    : [ \t]+ -> channel(HIDDEN)
    ;

Newline
    : ('\r' '\n'? | '\n') -> channel(HIDDEN)
    ;

BlockComment
    : '/*' .*? '*/' -> channel(HIDDEN)
    ;

LineComment
    : '//' ~[\r\n]* -> channel(HIDDEN)
    ;
