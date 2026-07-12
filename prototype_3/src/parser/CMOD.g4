// C99 grammar without trigrams and K&R syntax, originally taken from Annex A of C99 standard and edited
// Here, we perform a partial parse to extract file-level names
// We also introduce module syntax to the language

grammar CMOD;

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
    // Restrict to at most one typedef name
    : (storageClassSpecifier | typeQualifier | functionSpecifier)* typeSpecifier (storageClassSpecifier | typeQualifier | functionSpecifier)*
    ;

initDeclaratorList
    : initDeclarator (',' initDeclarator)*
    ;

initDeclarator
    : rootDeclarator ('=' initializer)?
    ;

storageClassSpecifier
    : 'typedef' | 'extern' | 'static' | 'auto' | 'register'
    ;

typeSpecifier
    // Grammar augmented with constraint 6.7.2[2] to avoid multiple typedefNames
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
    // Restrict to at most one typedef name
    : typeQualifier* typeSpecifier typeQualifier*
    ;

structDeclaratorList
    : structDeclarator (',' structDeclarator)*
    ;

structDeclarator
    : rootDeclarator
    | rootDeclarator? ':' constantExpression
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

rootDeclarator
    : declarator
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
    | directDeclarator '(' parameterTypeList? ')'
    // | directDeclarator '(' identifierList? ')'  // I'm not supporting K&R syntax
    ;

pointer
    : ('*' typeQualifierList?)+
    ;

typeQualifierList
    : typeQualifier+
    ;

parameterTypeList
    : parameterDeclaration (',' parameterDeclaration)* (',' '...')?
    ;

parameterDeclaration
    : declarationSpecifiers (rootDeclarator | rootAbstractDeclarator)?
    ;

rootAbstractDeclarator
    : abstractDeclarator
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
    | '(' parameterTypeList? ')'
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
    : declarationSpecifiers rootDeclarator compoundStatement
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
