//Definitions Section
%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*Lex  includes  this  file  and  utilizes  the  definitions  for  token  values.  
To  obtain  tokens  yacc  calls  yylex.  Function  yylex  has  a  return  type  
of  int  that  returns  a  token */

extern int yylex();
extern int yyparse();
extern FILE* yyin;

/*yyerror is used to generate an error in case something is wrong.
It's also called in main function */
void yyerror(const char* s);
%}

//Rules Section
%union {
	int ival;
}
//This is where YACC generates a parser in file y.tab.c and an include file y.tab.h
%token<ival> T_INT
%token T_PLUS T_MINUS, T_MUL T_DIV, T_POW
%token T_NEWLINE 
%token LPAREN, RPAREN


%type<ival> expression


%start calculation


%%

calculation:
	   | calculation line
;

line: T_NEWLINE
    | expression T_NEWLINE { printf("\tResult: %i\n", $1); }
;

/*The  rules  section  resembles  the  BNF  grammar  discussed  earlier.  
The  left-hand  side  of  a  production, or nonterminal, 
is entered left-justified and followed by a colon. 
This is followed by the right-hand side of the production. 
Actions associated with a rule are entered in braces.*/

;

expression: T_INT				{ $$ = $1; }
	  | expression T_PLUS expression	{ $$ = $1 + $3; }
	  | expression T_MINUS expression	{ $$ = $1 - $3; }
	  | expression T_MUL expression	{ $$ = $1 * $3; }
	  | expression T_DIV expression	{ $$ = $1 / $3; }
	  | expression T_POW expression { $$ = pow($1, $3); }
	  | LPAREN expression RPAREN { $$ = $2; }

;

%%

int main() {
	yyin = stdin;

	do {
		yyparse();
	} while(!feof(yyin));

	return 0;
}

void yyerror(const char* s) {
	fprintf(stderr, "Parse error: %s\n", s);
	exit(1);
}

