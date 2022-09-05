grammar reconhecedor;
// antlr4 -Dlanguage=Python3 reconhecedor.g4 "Compilar a gramática para o python"
// grun reconhecedor "testar a gramática"
// Parser Rules
input_txt: 'txt[] = ' txt;
input_pat: 'pat[] = ' txt;

txt: '"' WOR '"';
// Lexer Rules
WOR: (LET | NUM)+;
LET: [a - z] | [A - Z]; // ' ' esta implícito em [a - z]
NUM: [0 - 9];
WHITESPACE: ' ' -> skip; 