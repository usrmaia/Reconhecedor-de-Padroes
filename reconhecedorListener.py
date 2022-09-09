# Generated from reconhecedor.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .reconhecedorParser import reconhecedorParser
else:
    from reconhecedorParser import reconhecedorParser

from padrao import Padrao

# This class defines a complete listener for a parse tree produced by reconhecedorParser.
class reconhecedorListener(ParseTreeListener):
    def __init__(self):
        self.p = Padrao()

    # Enter a parse tree produced by reconhecedorParser#input_.
    def enterInput_(self, ctx:reconhecedorParser.Input_Context):
        pass

    # Exit a parse tree produced by reconhecedorParser#input_.
    def exitInput_(self, ctx:reconhecedorParser.Input_Context):
        pass


    # Enter a parse tree produced by reconhecedorParser#input_txt.
    def enterInput_txt(self, ctx:reconhecedorParser.Input_txtContext):
        txt = ctx.getText()[1:-1]
        # print(f"Este é o TXT[] = '{txt}'")
        self.p.setTexto(txt)
        pass

    # Exit a parse tree produced by reconhecedorParser#input_txt.
    def exitInput_txt(self, ctx:reconhecedorParser.Input_txtContext):
        pass


    # Enter a parse tree produced by reconhecedorParser#input_pat.
    def enterInput_pat(self, ctx:reconhecedorParser.Input_patContext):
        pat = ctx.getText()[1:-1]
        # print(f"Este é o PAT[] = '{pat}'")
        self.p.setPadrao(pat)
        
        print("Força Bruta: ")
        self.p.ForcaBruta(self.p.padrao, self.p.texto)

        print("KMP: ")
        self.p.KMP()

        pass

    # Exit a parse tree produced by reconhecedorParser#input_pat.
    def exitInput_pat(self, ctx:reconhecedorParser.Input_patContext):
        pass


    # Enter a parse tree produced by reconhecedorParser#str_.
    def enterStr_(self, ctx:reconhecedorParser.Str_Context):
        pass

    # Exit a parse tree produced by reconhecedorParser#str_.
    def exitStr_(self, ctx:reconhecedorParser.Str_Context):
        pass



