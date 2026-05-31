// C-like language with expressions removed, used to showcase module capabilities

grammar CMOD;

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
    : 'export'? structUnionDefinition
    | 'export'? typedefDefinition
    | 'export'? globalDefinition
    | 'export'? functionDefinition
    | ';' // stray ;
    ;

structUnionDefinition
    : ('struct' | 'union') Identifier '{' structField* '}' ';'
    ;

structField
    : typeSpecifier declarator ';'
    ;

typedefDefinition
    : 'typedef' expression Identifier ';'
    ;

globalDefinition
    : typeSpecifier declarator ('=' expression)? ';'
    ;

functionDefinition
    : typeSpecifier declarator '(' parameterList? ')' compoundStatement
    ;

parameterList
    : typeSpecifier declarator (',' typeSpecifier declarator)*
    ;

compoundStatement
    : '{' statement* '}'
    ;

statement
    : 'typedef'? expression ';'
    ;

expression
    // Modules doesn't need to parse expressions correctly
    // We just need to know which symbols are used
    // Note this is a conservative overestimate
    : expression expression
    | ',' | '.' | '->' | '*' | '/' | '+' | '-' | '!' | '~' | '&' | '|' | '?' | ':' | '=' | '<' | '>'
    | '(' expression ')'
    | '[' expression ']'
    | '{' expression '}'
    | StringLiteral
    | CharLiteral
    | Number
    | typeSpecifier '*'*  // Identifier is contained inside
    ;

typeSpecifier
    : 'void'
    | 'char'
    | 'short'
    | 'int'
    | 'long'
    | 'float'
    | 'double'
    | 'struct' Identifier
    | 'union' Identifier
    | Identifier
    ;

declarator
    : '*'? Identifier
    ;

Identifier
    : Nondigit (Nondigit | Digit)*
    ;

Number
    : Digit+ ('.' Digit*)?
    ;

fragment Nondigit
    : [a-zA-Z_$]
    ;

fragment Digit
    : [0-9]
    ;

CharLiteral
    : '\'' SChar '\''
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
