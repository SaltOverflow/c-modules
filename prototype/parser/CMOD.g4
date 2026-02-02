// C-like language with expressions removed, used to showcase module capabilities

grammar CMOD;

compilationUnit
    : translationUnit EOF
    ;

translationUnit
    : moduleDeclaration importDeclaration* externalDeclaration*
    ;

moduleDeclaration
    : 'module' ';'
    ;

importDeclaration
    : 'import' (StringLiteral | (Identifier ('/' Identifier)*)) ';'
    ;

externalDeclaration
    : 'export'? limitedFunctionDefinition
    | 'export'? limitedGlobal
    | 'export'? limitedStruct
    | ';' // stray ;
    ;

limitedFunctionDefinition
    : limitedTypeSpecifier limitedDeclarator '(' limitedParameterList?  ')' limitedCompoundStatement
    ;

limitedTypeSpecifier
    : 'void'
    | 'char'
    | 'short'
    | 'int'
    | 'long'
    | 'float'
    | 'double'
    | 'struct' Identifier
    ;

limitedDeclarator
    : '*'? Identifier
    ;

limitedParameterList
    : limitedTypeSpecifier limitedDeclarator (',' limitedTypeSpecifier limitedDeclarator)*
    ;

limitedCompoundStatement
    : '{' limitedStatement* '}'
    ;

limitedStatement
    : Identifier ';'  // these are values or functions
    | 'type' Identifier ';'  // these are structs, need full definition
    | 'type' '*' Identifier ';'  // these are structs, only need forward declaration
    ;

limitedGlobal
    : limitedTypeSpecifier limitedDeclarator ('=' limitedInitializer)? ';'
    ;

limitedInitializer
    : Identifier ('+' Identifier)* // these are values or functions
    ;

limitedStruct
    : 'struct' Identifier limitedCompoundStatement ';'
    ;

Identifier
    : Nondigit (Nondigit | Digit)*
    ;

fragment Nondigit
    : [a-zA-Z_$]
    ;

fragment Digit
    : [0-9]
    ;

StringLiteral
    : '"' SChar* '"'
    ;

fragment SChar
    : ~["\r\n]
    ;

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
