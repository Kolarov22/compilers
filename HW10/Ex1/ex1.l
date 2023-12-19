%{
#include <stdio.h>
%}


%%
^[0-9]{2}\/[0-9]{2}\/[0-9]{4}   { printf("Valid date: %s\n", yytext); }
.                                           { printf("Invalid date: %s\n", yytext); }
%%

int main() {
    yylex();
    return 0;
}
