grammar reconhecedor;
// antlr4 -Dlanguage=Python3 reconhecedor.g4 "Compilar a gramática para o python"
// grun reconhecedor "testar a gramática"
// Parser Rules
input_: input_txt ENT input_pat;
input_txt: 'txt[] = ' txt;
input_pat: 'pat[] = ' txt;

txt: '"' WOR '"';
// Lexer Rules
WOR: (LET | NUM | ' ')+;
LET: [a-z] | [A-Z];
NUM: [0-9];
ENT: '\n';
WHITESPACE: [ \n]+ -> skip;