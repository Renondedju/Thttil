# Generated from Language\Grammar\Thttil.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write(";\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\7\2\20\n\2\f\2\16\2\23\13\2\3\2\3\2\3\3\3\3\3\3\5\3\32")
        buf.write("\n\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6&\n\6")
        buf.write("\f\6\16\6)\13\6\5\6+\n\6\3\6\3\6\3\6\7\6\60\n\6\f\6\16")
        buf.write("\6\63\13\6\3\6\5\6\66\n\6\3\6\5\69\n\6\3\6\2\2\7\2\4\6")
        buf.write("\b\n\2\2\2>\2\f\3\2\2\2\4\31\3\2\2\2\6\33\3\2\2\2\b\35")
        buf.write("\3\2\2\2\n8\3\2\2\2\f\21\5\6\4\2\r\20\5\n\6\2\16\20\5")
        buf.write("\6\4\2\17\r\3\2\2\2\17\16\3\2\2\2\20\23\3\2\2\2\21\17")
        buf.write("\3\2\2\2\21\22\3\2\2\2\22\24\3\2\2\2\23\21\3\2\2\2\24")
        buf.write("\25\7\2\2\3\25\3\3\2\2\2\26\32\7\f\2\2\27\32\7\13\2\2")
        buf.write("\30\32\5\n\6\2\31\26\3\2\2\2\31\27\3\2\2\2\31\30\3\2\2")
        buf.write("\2\32\5\3\2\2\2\33\34\7\b\2\2\34\7\3\2\2\2\35\36\7\n\2")
        buf.write("\2\36\t\3\2\2\2\37 \7\3\2\2 *\7\t\2\2!+\3\2\2\2\"\'\5")
        buf.write("\4\3\2#$\7\4\2\2$&\5\4\3\2%#\3\2\2\2&)\3\2\2\2\'%\3\2")
        buf.write("\2\2\'(\3\2\2\2(+\3\2\2\2)\'\3\2\2\2*!\3\2\2\2*\"\3\2")
        buf.write("\2\2+,\3\2\2\2,\65\7\5\2\2-\61\7\6\2\2.\60\5\n\6\2/.\3")
        buf.write("\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\64\3")
        buf.write("\2\2\2\63\61\3\2\2\2\64\66\7\7\2\2\65-\3\2\2\2\65\66\3")
        buf.write("\2\2\2\669\3\2\2\2\679\5\b\5\28\37\3\2\2\28\67\3\2\2\2")
        buf.write("9\13\3\2\2\2\n\17\21\31\'*\61\658")
        return buf.getvalue()


class ThttilParser ( Parser ):

    grammarFileName = "Thttil.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'$('", "','", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STREAM_TAG", "FUNCTION", 
                      "PRINT", "STRING", "VARIABLE", "COMMENT", "WHITESPACE" ]

    RULE_program = 0
    RULE_argument = 1
    RULE_stream_tag = 2
    RULE_print_command = 3
    RULE_command = 4

    ruleNames =  [ "program", "argument", "stream_tag", "print_command", 
                   "command" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    STREAM_TAG=6
    FUNCTION=7
    PRINT=8
    STRING=9
    VARIABLE=10
    COMMENT=11
    WHITESPACE=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stream_tag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThttilParser.Stream_tagContext)
            else:
                return self.getTypedRuleContext(ThttilParser.Stream_tagContext,i)


        def EOF(self):
            return self.getToken(ThttilParser.EOF, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThttilParser.CommandContext)
            else:
                return self.getTypedRuleContext(ThttilParser.CommandContext,i)


        def getRuleIndex(self):
            return ThttilParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ThttilParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.stream_tag()
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ThttilParser.T__0) | (1 << ThttilParser.STREAM_TAG) | (1 << ThttilParser.PRINT))) != 0):
                self.state = 13
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ThttilParser.T__0, ThttilParser.PRINT]:
                    self.state = 11
                    self.command()
                    pass
                elif token in [ThttilParser.STREAM_TAG]:
                    self.state = 12
                    self.stream_tag()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(ThttilParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ThttilParser.VARIABLE, 0)

        def STRING(self):
            return self.getToken(ThttilParser.STRING, 0)

        def command(self):
            return self.getTypedRuleContext(ThttilParser.CommandContext,0)


        def getRuleIndex(self):
            return ThttilParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ThttilParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_argument)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ThttilParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(ThttilParser.VARIABLE)
                pass
            elif token in [ThttilParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(ThttilParser.STRING)
                pass
            elif token in [ThttilParser.T__0, ThttilParser.PRINT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.command()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stream_tagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STREAM_TAG(self):
            return self.getToken(ThttilParser.STREAM_TAG, 0)

        def getRuleIndex(self):
            return ThttilParser.RULE_stream_tag

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStream_tag" ):
                return visitor.visitStream_tag(self)
            else:
                return visitor.visitChildren(self)




    def stream_tag(self):

        localctx = ThttilParser.Stream_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stream_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(ThttilParser.STREAM_TAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_commandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ThttilParser.PRINT, 0)

        def getRuleIndex(self):
            return ThttilParser.RULE_print_command

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_command" ):
                return visitor.visitPrint_command(self)
            else:
                return visitor.visitChildren(self)




    def print_command(self):

        localctx = ThttilParser.Print_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_print_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(ThttilParser.PRINT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.function = None # Token
            self._argument = None # ArgumentContext
            self.args = list() # of ArgumentContexts
            self._command = None # CommandContext
            self.commands = list() # of CommandContexts

        def FUNCTION(self):
            return self.getToken(ThttilParser.FUNCTION, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThttilParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(ThttilParser.ArgumentContext,i)


        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThttilParser.CommandContext)
            else:
                return self.getTypedRuleContext(ThttilParser.CommandContext,i)


        def print_command(self):
            return self.getTypedRuleContext(ThttilParser.Print_commandContext,0)


        def getRuleIndex(self):
            return ThttilParser.RULE_command

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = ThttilParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ThttilParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(ThttilParser.T__0)
                self.state = 30
                localctx.function = self.match(ThttilParser.FUNCTION)
                self.state = 40
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ThttilParser.T__2]:
                    pass
                elif token in [ThttilParser.T__0, ThttilParser.PRINT, ThttilParser.STRING, ThttilParser.VARIABLE]:
                    self.state = 32
                    localctx._argument = self.argument()
                    localctx.args.append(localctx._argument)
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ThttilParser.T__1:
                        self.state = 33
                        self.match(ThttilParser.T__1)
                        self.state = 34
                        localctx._argument = self.argument()
                        localctx.args.append(localctx._argument)
                        self.state = 39
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 42
                self.match(ThttilParser.T__2)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ThttilParser.T__3:
                    self.state = 43
                    self.match(ThttilParser.T__3)
                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ThttilParser.T__0 or _la==ThttilParser.PRINT:
                        self.state = 44
                        localctx._command = self.command()
                        localctx.commands.append(localctx._command)
                        self.state = 49
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 50
                    self.match(ThttilParser.T__4)


                pass
            elif token in [ThttilParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.print_command()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





