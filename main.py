import sys
from antlr4 import *
from reconhecedorLexer import reconhecedorLexer
from reconhecedorParser import reconhecedorParser
from padrao import Padrao

def main(argv):
    input = FileStream(argv[1]) # input.txt
    print(input)

        

if __name__ == '__main__':
    main(sys.argv)