# Generated from reconhecedor.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("@\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\5\6\5-\n\5\r\5\16\5.\3\6\5\6\62\n\6\3\7\3\7\3\b")
        buf.write("\3\b\3\t\6\t9\n\t\r\t\16\t:\3\t\3\t\3\n\3\n\2\2\13\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\3\2\5\4\2C\\c|\3")
        buf.write("\2\62;\4\2\f\f\"\"\2C\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\36\3\2\2\2\7")
        buf.write("\'\3\2\2\2\t,\3\2\2\2\13\61\3\2\2\2\r\63\3\2\2\2\17\65")
        buf.write("\3\2\2\2\218\3\2\2\2\23>\3\2\2\2\25\26\7v\2\2\26\27\7")
        buf.write("z\2\2\27\30\7v\2\2\30\31\7]\2\2\31\32\7_\2\2\32\33\7\"")
        buf.write("\2\2\33\34\7?\2\2\34\35\7\"\2\2\35\4\3\2\2\2\36\37\7r")
        buf.write("\2\2\37 \7c\2\2 !\7v\2\2!\"\7]\2\2\"#\7_\2\2#$\7\"\2\2")
        buf.write("$%\7?\2\2%&\7\"\2\2&\6\3\2\2\2\'(\7$\2\2(\b\3\2\2\2)-")
        buf.write("\5\13\6\2*-\5\r\7\2+-\7\"\2\2,)\3\2\2\2,*\3\2\2\2,+\3")
        buf.write("\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\n\3\2\2\2\60\62")
        buf.write("\t\2\2\2\61\60\3\2\2\2\62\f\3\2\2\2\63\64\t\3\2\2\64\16")
        buf.write("\3\2\2\2\65\66\7\f\2\2\66\20\3\2\2\2\679\t\4\2\28\67\3")
        buf.write("\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;<\3\2\2\2<=\b\t\2")
        buf.write("\2=\22\3\2\2\2>?\7=\2\2?\24\3\2\2\2\7\2,.\61:\3\b\2\2")
        return buf.getvalue()


class reconhecedorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    WOR = 4
    LET = 5
    NUM = 6
    ENT = 7
    WHITESPACE = 8
    EOF_ = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'txt[] = '", "'pat[] = '", "'\"'", "'\n'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "WOR", "LET", "NUM", "ENT", "WHITESPACE", "EOF_" ]

    ruleNames = [ "T__0", "T__1", "T__2", "WOR", "LET", "NUM", "ENT", "WHITESPACE", 
                  "EOF_" ]

    grammarFileName = "reconhecedor.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


