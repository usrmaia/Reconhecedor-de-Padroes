# Generated from reconhecedor.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\27\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\4\3\4\6\4\21\n\4\r\4\16\4\22\3\4\3\4\3\4\2\2\5\2\4\6")
        buf.write("\2\3\3\2\6\7\2\24\2\b\3\2\2\2\4\13\3\2\2\2\6\16\3\2\2")
        buf.write("\2\b\t\7\3\2\2\t\n\5\6\4\2\n\3\3\2\2\2\13\f\7\4\2\2\f")
        buf.write("\r\5\6\4\2\r\5\3\2\2\2\16\20\7\5\2\2\17\21\t\2\2\2\20")
        buf.write("\17\3\2\2\2\21\22\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2")
        buf.write("\23\24\3\2\2\2\24\25\7\5\2\2\25\7\3\2\2\2\3\22")
        return buf.getvalue()


class reconhecedorParser ( Parser ):

    grammarFileName = "reconhecedor.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'txt[] = '", "'pat[] = '", "'\"'", "<INVALID>", 
                     "<INVALID>", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WOR", "NUM", "WHITESPACE" ]

    RULE_input_txt = 0
    RULE_input_pat = 1
    RULE_txt = 2

    ruleNames =  [ "input_txt", "input_pat", "txt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WOR=4
    NUM=5
    WHITESPACE=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Input_txtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def txt(self):
            return self.getTypedRuleContext(reconhecedorParser.TxtContext,0)


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
        self.enterRule(localctx, 0, self.RULE_input_txt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(reconhecedorParser.T__0)
            self.state = 7
            self.txt()
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

        def txt(self):
            return self.getTypedRuleContext(reconhecedorParser.TxtContext,0)


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
        self.enterRule(localctx, 2, self.RULE_input_pat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(reconhecedorParser.T__1)
            self.state = 10
            self.txt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TxtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WOR(self, i:int=None):
            if i is None:
                return self.getTokens(reconhecedorParser.WOR)
            else:
                return self.getToken(reconhecedorParser.WOR, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(reconhecedorParser.NUM)
            else:
                return self.getToken(reconhecedorParser.NUM, i)

        def getRuleIndex(self):
            return reconhecedorParser.RULE_txt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTxt" ):
                listener.enterTxt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTxt" ):
                listener.exitTxt(self)




    def txt(self):

        localctx = reconhecedorParser.TxtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_txt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(reconhecedorParser.T__2)
            self.state = 14 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 13
                _la = self._input.LA(1)
                if not(_la==reconhecedorParser.WOR or _la==reconhecedorParser.NUM):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==reconhecedorParser.WOR or _la==reconhecedorParser.NUM):
                    break

            self.state = 18
            self.match(reconhecedorParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





