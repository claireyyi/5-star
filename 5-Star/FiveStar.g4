grammar FiveStar;


//Python-specific tokens
NEWLINE: '\r'? '\n';
COMMENT: '#' ~[\r\n]* -> skip;
WS: [ \t]+ -> skip;


program: (assignment | expression | if_statement | block)* EOF;

// assignment 
assignment:
ID (ASSIGN | ADD_ASSIGN | MINUS_ASSIGN | MUL_ASSIGN | DIV_ASSIGN) expression ;


// list
list:
'[' (expression (',' expression)*)? (',')? ']'; //trailing commas allowed

expression: expression (TIMES | MOD| OVER) expression |
            expression (PLUS | MINUS) expression | 
            (PLUS | MINUS)? value | '(' expression ')' |
            ID | BOOLEAN | STRING | list;

value //defines all types of atomic values
: INTEGER
 | DOUBLE
 | STRING
 | BOOLEAN
 | ID
 | list
 ;

//tokens
INTEGER : [0-9]+ ;
DOUBLE  : [0-9]+ '.' [0-9]* | '.' [0-9]+ ;
STRING  : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'' ;
BOOLEAN : 'True' | 'False' ;
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;

//assignment operators
ASSIGN      : '=' ;
ADD_ASSIGN  : '+=' ;
MINUS_ASSIGN  : '-=' ;
MUL_ASSIGN  : '*=' ;
DIV_ASSIGN  : '/=' ;

//arithmetic operators
PLUS  : '+' ;
MINUS : '-' ;
TIMES : '*' ;
MOD   : '%' ;
OVER  : '/' ;

if_statement : 
            'if'  condition ':' block
            ('elif' condition ':' block)* 
            ('else' : block)? ;

condition: 
            condition ('and' | 'or') condition     |
            'not' condition     | expression (LT | LE | GT | GE | EQ | NE) expression     
            | BOOLEAN     | '(' condition ')'     ;

block: 
    NEWLINE? INDENT statement+ DEDENT?  | statement ;

statement:  assignment | expression | if_statement ;

// comparison operators
NE: '!=';
EQ: '==';
LE: '<=';
GE: '>=';
LT: '<';
GT: '>';

// logical
AND: 'and';
OR: 'or';
NOT: 'not';


// handles indentation logic
INDENT: '    ';
DEDENT: ;


