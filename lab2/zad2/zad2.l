
%x COMMENT
%x TAG

%%
\<                  ECHO; BEGIN(TAG);
\<!--               BEGIN(COMMENT);

<TAG>.|\n              ECHO;
<TAG>.\>              {ECHO; BEGIN(INITIAL);}
<TAG>.\<!--            BEGIN(COMMENT);

<COMMENT>.|\n            ;
<COMMENT>--\>            BEGIN(INITIAL);

%%

int yywrap() {
    return 1;
}

int main() {
    return yylex();
}