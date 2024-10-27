%option noyywrap
%option yylineno
%{
#include "parser.tab.h"

int yylex();
%}

%%
^#(.|\\\n)*\n   ;
\\\n            ;
[[:blank:]]+ 	;
[0-9]+	        { yylval = atoi(yytext); return NUM; }
"+"             { return PLUS; }
"-"             { return MINUS; }
"*"             { return MULT; }
"/"             { return DIV; }
"%"             { return MOD; }
"^"             { return POW; }
\(              { return LBRACKET; }
\)              { return RBRACKET; }
\n              { return END; }
.               { return ERROR; }
%%