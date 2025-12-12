
grammar FiveStar;


program
    : statement* EOF
    ;

statement
    : (assignment  | expression) NEWLINE?
    | while_statement | if_statement
    | for_statement
    ;

assignment:
    ID (ASSIGN | ADD_ASSIGN | MINUS_ASSIGN | MUL_ASSIGN | DIV_ASSIGN) expression
    ;



//block statemnts

while_statement
    : 'while' expression ':' NEWLINE ((TAB+ statement)+)+
    ;

if_statement
    : TAB* 'if' expression ':' NEWLINE ((TAB+ statement)+)+

      TAB* ('elif' expression ':' NEWLINE (TAB+ statement)+ )*

      TAB* ('else' ':' NEWLINE ((TAB+ statement)+))?
    ;

for_statement
    : 'for' ID 'in' expression ':' NEWLINE ((TAB+ statement)+)+
    ;


expression
    : function_call
    |'(' expression ')'| token
    | list                                     
    | MINUS expression | 'not' expression  | expression (TIMES | MOD| OVER)  expression  
    | expression (PLUS | MINUS) expression    
    | expression (LE | GE | LT | GT) expression 
    | expression (NE | EQ) expression     
    | expression 'or' expression | expression 'and' expression             
    ;


function_call
    : ID '(' (expression (',' expression)*)? ')'
    ;

// list
list:
    '[' (expression (',' expression)*)? (',')? ']'
    ;


// tokens
token
    : INTEGER | STRING | FLOAT| BOOLEAN | ID
    ;


// Keywords

//bOOLS
BOOLEAN : 'True' | 'False' ;

// Comments 
MULTILINE_COMMENT
    : '\'\'\'' ( . | '\r' | '\n' )*? '\'\'\'' NEWLINE* -> skip
    ;

COMMENT
    : '#' ~[\r\n]* NEWLINE* -> skip
    ;

// Literals 

STRING  : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'' ;


// Literals 
FLOAT : [0-9]+ '.' [0-9]+ ; 
INTEGER   : [0-9]+;

//Identifiers
ID : [a-zA-Z_] [a-zA-Z_0-9]* ;


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

TAB : '\t';

//new line
NEWLINE : ('\r'? '\n')+ ;


// Whitespace
WS : [ ]+ -> skip ;
