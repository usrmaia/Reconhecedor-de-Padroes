# Generated from reconhecedor.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\32\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\2\2\6\2")
        buf.write("\4\6\b\2\2\2\25\2\n\3\2\2\2\4\21\3\2\2\2\6\23\3\2\2\2")
        buf.write("\b\25\3\2\2\2\n\13\7\3\2\2\13\f\5\4\3\2\f\r\7\t\2\2\r")
        buf.write("\16\7\4\2\2\16\17\5\6\4\2\17\20\7\13\2\2\20\3\3\2\2\2")
        buf.write("\21\22\5\b\5\2\22\5\3\2\2\2\23\24\5\b\5\2\24\7\3\2\2\2")
        buf.write("\25\26\7\5\2\2\26\27\7\6\2\2\27\30\7\5\2\2\30\t\3\2\2")
        buf.write("\2\2")
        return buf.getvalue()


class reconhecedorParser ( Parser ):

    grammarFileName = "reconhecedor.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'txt[] = '", "'pat[] = '", "'\"'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\n'", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WOR", "LET", "NUM", "ENT", "WHITESPACE", "EOF_" ]

    RULE_input_ = 0
    RULE_input_txt = 1
    RULE_input_pat = 2
    RULE_str_ = 3

    ruleNames =  [ "input_", "input_txt", "input_pat", "str_" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WOR=4
    LET=5
    NUM=6
    ENT=7
    WHITESPACE=8
    EOF_=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Input_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def input_txt(self):
            return self.getTypedRuleContext(reconhecedorParser.Input_txtContext,0)


        def ENT(self):
            return self.getToken(reconhecedorParser.ENT, 0)

        def input_pat(self):
            return self.getTypedRuleContext(reconhecedorParser.Input_patContext,0)


        def EOF_(self):
            return self.getToken(reconhecedorParser.EOF_, 0)

        def getRuleIndex(self):
            return reconhecedorParser.RULE_input_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_" ):
                listener.enterInput_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_" ):
                listener.exitInput_(self)




    def input_(self):

        localctx = reconhecedorParser.Input_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_input_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(reconhecedorParser.T__0)
            self.state = 9
            self.input_txt()
            self.state = 10
            self.match(reconhecedorParser.ENT)
            self.state = 11
            self.match(reconhecedorParser.T__1)
            self.state = 12
            self.input_pat()
            self.state = 13
            self.match(reconhecedorParser.EOF_)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Input_txtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def str_(self):
            return self.getTypedRuleContext(reconhecedorParser.Str_Context,0)


        def getRuleIndex(self):
            return reconhecedorParser.RULE_input_txt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_txt" ):
                listener.enterInput_txt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_txt" ):
                listener.exitInput_txt(self)




    def input_txt(self):

        localctx = reconhecedorParser.Input_txtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_input_txt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.str_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Input_patContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def str_(self):
            return self.getTypedRuleContext(reconhecedorParser.Str_Context,0)


        def getRuleIndex(self):
            return reconhecedorParser.RULE_input_pat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_pat" ):
                listener.enterInput_pat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_pat" ):
                listener.exitInput_pat(self)




    def input_pat(self):

        localctx = reconhecedorParser.Input_patContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_input_pat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.str_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Str_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WOR(self):
            return self.getToken(reconhecedorParser.WOR, 0)

        def getRuleIndex(self):
            return reconhecedorParser.RULE_str_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr_" ):
                listener.enterStr_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr_" ):
                listener.exitStr_(self)




    def str_(self):

        localctx = reconhecedorParser.Str_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_str_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(reconhecedorParser.T__2)
            self.state = 20
            self.match(reconhecedorParser.WOR)
            self.state = 21
            self.match(reconhecedorParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





