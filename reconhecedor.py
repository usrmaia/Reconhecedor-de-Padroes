import sys
from antlr4 import *
from reconhecedorLexer import reconhecedorLexer
from reconhecedorParser import reconhecedorParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = reconhecedorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = reconhecedorParser(stream)
    tree = parser.startRule()

if __name__ == '__main__':
    main(sys.argv)
