// C99 grammar was originally taken from Annex A of C99 standard ( https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf ) and edited.
// Notable differences: module syntax (ie. module, import, export) added, digraphs/trigraphs/K&R syntax removed.
// Here, we perform a partial parse to extract file-level names. This means that expression, function bodies and parameter lists are skipped.

grammar CMODInterface;

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
    | enumerationConstant
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
    // This needs disambiguation with identifiers in expressions
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
// The partial parse runs without a symbol table, so just track parentheses

skipTokens
    // This captures CharacterConstant and StringLiteral because those are tokens
    : ~('(' | ')' | '[' | ']' | '{' | '}' | ',' | ';'
        | 'struct' | 'union' | 'enum')
    | ('struct' | 'union' | 'enum') Identifier
    ;

constantExpression
    : (
        skipTokens
        | '(' innerExpression? ')'
        | '[' innerExpression? ']'
        | '{' innerExpression? '}'
    )+
    ;

assignmentExpression
    : constantExpression
    ;

expression
    : (
        constantExpression
        | ','
    )+
    ;

innerExpression
    : (
        expression
        | ';'
    )+
    ;

// A.2.2 Declarations

declaration
    : declarationSpecifiers initDeclaratorList? ';'
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
    : 'typedef' | 'extern' | 'static' | 'auto' | 'register'
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
    : structOrUnion Identifier? '{' structDeclaration+ '}'
    | structOrUnion Identifier
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
    : 'enum' Identifier? '{' enumeratorList ','? '}'
    | 'enum' Identifier
    ;

enumeratorList
    : enumerator (',' enumerator)*
    ;

enumerator
    : enumerationConstant ('=' constantExpression)?
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
    : Identifier
    | '(' declarator ')'
    | directDeclarator '[' typeQualifierList? assignmentExpression? ']'
    | directDeclarator '[' 'static' typeQualifierList? assignmentExpression ']'
    | directDeclarator '[' typeQualifierList 'static' assignmentExpression ']'
    | directDeclarator '[' typeQualifierList? '*' ']'
    | directDeclarator '(' expression? ')'  // int foo(a(b)) is ambiguous, let's skip parameters because we don't need it anyways
    // | directDeclarator '(' identifierList? ')'  // We don't support K&R syntax
    ;

pointer
    : ('*' typeQualifierList?)+
    ;

typeQualifierList
    : typeQualifier+
    ;

typedefName
    // Grammar set up to avoid ambiguity with identifiers for file-level declarations
    : Identifier
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
// The partial parse runs without a symbol table, so just track parentheses

compoundStatement
    : '{' innerExpression? '}'
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
    : declarationSpecifiers declarator compoundStatement
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
