grammar FiveStar;

// assignment 
assignment:
ID (ASSIGN | ADD_ASSIGN | MINUS_ASSIGN | MUL_ASSIGN | DIV_ASSIGN) expression ;

// list
list:
'[' (expression (',' expression)*)? (',')? ']'; //trailing commas allowed


//tokens
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
INTEGER : [0-9]+ ;
DOUBLE  : [0-9]+ '.' [0-9]* | '.' [0-9]+ ;
STRING  : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'' ;
BOOLEAN : 'True' | 'False' ;

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
DIV  : '/' ;
MOD   : '%' ;

//whitespace ignored
WS     : [ \t]+ -> skip ;
NEWLINE: [\r\n]+ ;

