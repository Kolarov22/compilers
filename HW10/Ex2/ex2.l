%{
#include <stdio.h>
#include <stdlib.h>
#include <regex.h>
%}

%option noyywrap

%%
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ {
    printf("Valid email address: %s\n", yytext);
}
. {
    printf("Invalid email address: %s\n", yytext);
}
%%

int main() {
    yylex();
    return 0;
}
