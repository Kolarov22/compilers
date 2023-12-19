%option noyywrap

%{
#include <stdio.h>
#include <math.h>

#define YY_DECL int yylex()

#include "example.tab.h"

%}

%%

[ \t]	;
[0-9]+		{yylval.ival = atoi(yytext); return T_INT;}
\n		{return T_NEWLINE;}
"+"		{return T_PLUS;}
"-"		{return T_MINUS;}
"*"     {return T_MUL;}
"/"     {return T_DIV;}
"^"	    {return T_POW;}
"("     { return LPAREN;}
")"     { return RPAREN;}


%%
