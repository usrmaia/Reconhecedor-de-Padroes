grammar reconhecedor;
// antlr4 -Dlanguage=Python3 reconhecedor.g4 "Compilar a gramática para o python"
// grun reconhecedor "testar a gramática"
// Parser Rules
input_: 'txt[] = ' input_txt
        ENT 
        'pat[] = ' input_pat
        EOF_;
input_txt: str_;
input_pat: str_;
str_: '"'WOR'"';
// Lexer Rules
WOR: (LET | NUM | ' ')+;
LET: [a-z] | [A-Z];
NUM: [0-9];
ENT: '\n';
WHITESPACE: [ \n]+ -> skip;
EOF_: ';';