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
    : typeQualifierList typeSpecifier typeQualifierList declarator ';'
    ;

typedefDefinition
    : 'typedef' expression Identifier ';'
    ;

globalDefinition
    : typeQualifierList typeSpecifier typeQualifierList declarator ('=' expression)? ';'
    ;

functionDefinition
    : 'inline'? typeQualifierList typeSpecifier typeQualifierList declarator '(' parameterList? ')' compoundStatement
    ;

parameterList
    : typeQualifierList typeSpecifier typeQualifierList declarator (',' typeQualifierList typeSpecifier typeQualifierList declarator)*
    ;

compoundStatement
    : '{' statement* '}'
    ;

statement
    : 'typedef'? expression ';'?
    ;

expression
    // Modules doesn't need to parse expressions correctly
    // We just need to know which symbols are used
    // Note this is a conservative overestimate
    : expression expression
    | ',' | '.' | '->' | '*' | '/' | '%' | '+' | '-' | '!' | '~' | '&' | '|' | '?' | ':' | '=' | '<' | '>'
    | '(' statement* ')'
    | '[' expression? ']'
    | '{' statement* '}'
    | StringLiteral
    | CharLiteral
    | Number
    | typeSpecifier (typeQualifier? '*')*  // Identifier is contained inside
    | typeQualifier
    ;

typeQualifierList
    : typeQualifier*
    ;

typeQualifier
    : 'const' | 'volatile'
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
    : ('*' typeQualifierList)? Identifier arraySuffix*
    ;

arraySuffix
    : '[' expression? ']'
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
