grammar FiveStar;

//Python-specific tokens
NEWLINE: '\r'? '\n';
COMMENT: '#' ~[\r\n]* -> skip;
WS: [ \t]+ -> skip;

program: (statement | NEWLINE)* EOF;

// assignment 
assignment:
ID (ASSIGN | ADD_ASSIGN | MINUS_ASSIGN | MUL_ASSIGN | DIV_ASSIGN) expression;

// list
list:
'[' (expression (',' expression)*)? (',')? ']';

expression: expression (TIMES | MOD| OVER) expression |
            expression (PLUS | MINUS) expression | 
            (PLUS | MINUS)? value | '(' expression ')' |
            ID | BOOLEAN | STRING | list;

value: INTEGER | DOUBLE | STRING | BOOLEAN | ID | list;

// logical operators 
AND: 'and';
OR: 'or';
NOT: 'not';

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

// comparison operators
NE: '!=';
EQ: '==';
LE: '<=';
GE: '>=';
LT: '<';
GT: '>';

if_statement: 
    'if' condition ':' NEWLINE? block
    ('elif' condition ':' NEWLINE? block)* 
    ('else' ':' NEWLINE? block)? ;

condition: 
    condition (AND | OR) condition | NOT condition | comparison | '(' condition ')';

comparison: 
    expression (LT | LE | GT | GE | EQ | NE) expression | BOOLEAN | ID;

block: statement+ ;


statement: 
    (assignment | expression) NEWLINE | if_statement ;


