# Reconhecedor-de-Padroes
 
## Lista de instalações
* sudo apt install antlr4;
* pip install antlr4-python3-runtime==4.7.2 (garanta que antlr4 e runtime estejam na mesma versão);

### "Compilar" a gramática para Python3
* antlr4 -Dlanguage=Python3 MyGrammar.g4 -visitor

### Para executar o programa
* python3 main.py input.txt