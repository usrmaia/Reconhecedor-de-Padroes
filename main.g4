grammar main;
// antlr4 -Dlanguage=Python3 main.g4 "Compilar a gramática para o python"
// grun main "testar a gramática"
// Parser Rules

// Lexer Rules
TXT: ([a - z] | [A - Z] | [0 - 9] | ' ')+;
WHITESPACE: ' ' -> skip; 