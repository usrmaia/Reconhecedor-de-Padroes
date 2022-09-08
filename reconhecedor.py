import sys
from antlr4 import *
from reconhecedorLexer import reconhecedorLexer
from reconhecedorParser import reconhecedorParser
from reconhecedorListener import reconhecedorListener

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = reconhecedorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = reconhecedorParser(stream)
    tree = parser.input_()
    parser.Input_Context(tree)
    # print(tree.input_txt())

    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)

    walker = ParseTreeWalker()
    walker.walk(reconhecedorListener(), tree)
    print()

if __name__ == '__main__':
    main(sys.argv)
