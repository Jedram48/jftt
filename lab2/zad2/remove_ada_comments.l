%x BRACKET
%x COMMENT

%%

\(                      { ECHO; BEGIN(BRACKET); }
<BRACKET>\)             { ECHO; BEGIN(INITIAL); }
<BRACKET>.              { ECHO; }

^[[:blank:]]*--.*\n     ; 
(^|[[:space:]]?)--      { BEGIN(COMMENT); }

<COMMENT>[^\n]*         ;
<COMMENT>\n             { BEGIN(INITIAL); ECHO; }

%%

int yywrap() {
    return 1;
}

int main() {
    return yylex();
}