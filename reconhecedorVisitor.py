# Generated from reconhecedor.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .reconhecedorParser import reconhecedorParser
else:
    from reconhecedorParser import reconhecedorParser

# This class defines a complete generic visitor for a parse tree produced by reconhecedorParser.

class reconhecedorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by reconhecedorParser#input_txt.
    def visitInput_txt(self, ctx:reconhecedorParser.Input_txtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reconhecedorParser#input_pat.
    def visitInput_pat(self, ctx:reconhecedorParser.Input_patContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reconhecedorParser#txt.
    def visitTxt(self, ctx:reconhecedorParser.TxtContext):
        return self.visitChildren(ctx)



del reconhecedorParser