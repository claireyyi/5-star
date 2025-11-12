grammar FiveStar;

<<<<<<< HEAD
//Python-specific tokens
NEWLINE: '\r'? '\n' -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
WS: [ \t]+ -> skip;


program: (assignment | expression)* EOF;

// assignment 
assignment:
ID (ASSIGN | ADD_ASSIGN | MINUS_ASSIGN | MUL_ASSIGN | DIV_ASSIGN) expression ;


// list
list:
'[' (expression (',' expression)*)? (',')? ']'; //trailing commas allowed

expression: expression (TIMES | MOD| OVER) expression |
            expression (PLUS | MINUS) expression | 
            (PLUS | MINUS)? value | 
            ID | BOOLEAN | STRING | list | '(' expression ')';
=======
>>>>>>> 0e567ad (Added statement and value)

//tokens
INTEGER : [0-9]+ ;
DOUBLE  : [0-9]+ '.' [0-9]* | '.' [0-9]+ ;
STRING  : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'' ;
BOOLEAN : 'True' | 'False' ;
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;

//assignment operators
ASSIGN      : '=' ;
ADD_ASSIGN  : '+=' ;
<<<<<<< HEAD
MINUS_ASSIGN  : '-=' ;
=======
SUB_ASSIGN  : '-=' ;
>>>>>>> 0e567ad (Added statement and value)
MUL_ASSIGN  : '*=' ;
DIV_ASSIGN  : '/=' ;

//arithmetic operators
PLUS  : '+' ;
MINUS : '-' ;
TIMES : '*' ;
<<<<<<< HEAD
DIV  : '/' ;
MOD   : '%' ;

=======
OVER  : '/' ;
MOD   : '%' ;

//whitespace ignored
WS     : [ \t]+ -> skip ;
NEWLINE: [\r\n]+ ;
>>>>>>> 0e567ad (Added statement and value)

