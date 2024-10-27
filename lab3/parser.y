%{
  #define YYSTYPE int

  #include <stdio.h>
  #include <math.h>
  #include <string>

  #define TOP 1234577
  #define PLUS_OP 1
  #define MINUS_OP 2
  #define MULT_OP 3
  #define DIV_OP 4
  #define MOD_OP 5
  #define POW_OP 6

  using namespace std;

  int yylex();
  int yyerror(string);
  extern int yylineno;

  int GF(int a){
    int neg = false;
    if( a < 0 ) neg = true; 
    a = abs(a);
    while ( a > TOP) a -= TOP;
    if(neg) return TOP - a;
    return a;
  }

  int modinv(int a, int p) {
    int m0 = p, t, q;
    int x0 = 0, x1 = 1;
    if (p == 1) return 0;
    while (a > 1) {
        q = a / p;
        t = p;
        p = a % p, a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }
    if (x1 < 0) x1 += m0;
    return x1;
}

int divide(int a, int b) {
    int b_inverse = modinv(GF(b), TOP);
    if (b_inverse == 0) {
        printf("Dzielenie przez 0!\n");
        return 0;
    }
    long long result = ((long long)a * b_inverse) % TOP;
    return GF(result);
}
  
  int neg_num(int a){
    a = abs(a);
    while ( a > TOP) a -= TOP;
    return TOP - a;
  }

  int potengowanie(int a, int b){
    int result = a;
    bool neg = b < 0;
    b = abs(b);
    while ( b > 1 ){
        result *= a;
        b--;
        if ( result > TOP ) result -= TOP;
    }
    if(neg) return divide(1, result);
    return result;
  }

  int calculate(int op, int a, int b) {
    switch (op) {
        case PLUS_OP: return GF(a + b);
        case MINUS_OP: return GF(a - b);
        case MULT_OP : return GF((long long)(a * b));
        case DIV_OP: return GF(divide(a, b));
        case MOD_OP: return GF(a % b);
        case POW_OP: return GF(potengowanie(a, b));
        default: return 0;
    }
}



  string rpn = "";
  int error = 0;
%}

%token NUM
%token LBRACKET
%token RBRACKET

%left PLUS MINUS
%left MULT DIV MOD
%right POW
%precedence NEG
%nonassoc UMINUS

%token END
%token ERROR

%% /* Grammar rules and actions follow. */



input:
  %empty
| input line
;

line:   expr END {
                    if (!error) {
                        printf("%s\n= %d\n", rpn.c_str(), GF($$));
                    }
                    error = 0;
                    rpn = "";

                }
        | error END {
                        printf("Błąd w linii %d\n", yylineno - 1);
                        error = 0;
                        rpn = "";
        }
;

expr:
    NUM                         { rpn += to_string($1) + " "; $$ = GF($1); }
    | expr PLUS expr            { rpn += "+ "; $$ = calculate(PLUS_OP, $1, $3); }
    | expr MINUS expr           { rpn += "- "; $$ = calculate(MINUS_OP, $1, $3); }
    | expr MULT expr            { rpn += "* "; $$ = calculate(MULT_OP, $1, $3); }
    | expr DIV expr             { rpn += "/ ";
                                  if ($3 == 0) {
                                      printf("%s\n", rpn.c_str());
                                      yyerror("Nie dzielimy przez 0");
                                  } else {
                                      $$ = calculate(DIV_OP, $1, $3);
                                  } 
                                }
    | expr MOD expr             { rpn += "% ";
                                  if ($3 == 0) {
                                      printf("%s\n", rpn.c_str());
                                      yyerror("Nie modulujemy przez 0");
                                  } else {
                                      $$ = calculate(MOD_OP, $1, $3);
                                  } 
                                }
    | MINUS NUM %prec NEG       { rpn += to_string(neg_num($2)) + " "; $$ = -$2;}
    | expr POW expr             { rpn += "^ "; $$ = calculate(POW_OP, $1, $3); }
    | LBRACKET expr RBRACKET    { $$ = $2; }
;

%%

int yyerror(string str) {
    error = 1;
    printf("%s\n", str.c_str());
    return 0;
}

int main () {
  return yyparse();
}