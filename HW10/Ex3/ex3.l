%{
#include <stdio.h>
%}

%%
"//"(.*)      { printf("%s", yytext + 2); }  

"/*"(.)+\*+"/"  { int len = yyleng; 
               printf("%.*s", len - 4, yytext + 2);  }  

.           { putchar(yytext[0]); }   

%%

int main() {
    yylex();
    return 0;
}
