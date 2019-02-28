# Generated from Language\Grammar\Thttil.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\7\2\f\n\2\f\2")
        buf.write("\16\2\17\13\2\3\2\3\2\3\3\3\3\3\3\5\3\26\n\3\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\7\5 \n\5\f\5\16\5#\13\5\5\5%\n")
        buf.write("\5\3\5\3\5\3\5\7\5*\n\5\f\5\16\5-\13\5\3\5\5\5\60\n\5")
        buf.write("\3\5\5\5\63\n\5\3\5\2\2\6\2\4\6\b\2\2\28\2\r\3\2\2\2\4")
        buf.write("\25\3\2\2\2\6\27\3\2\2\2\b\62\3\2\2\2\n\f\5\b\5\2\13\n")
        buf.write("\3\2\2\2\f\17\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\20")
        buf.write("\3\2\2\2\17\r\3\2\2\2\20\21\7\2\2\3\21\3\3\2\2\2\22\26")
        buf.write("\7\13\2\2\23\26\7\n\2\2\24\26\5\b\5\2\25\22\3\2\2\2\25")
        buf.write("\23\3\2\2\2\25\24\3\2\2\2\26\5\3\2\2\2\27\30\7\t\2\2\30")
        buf.write("\7\3\2\2\2\31\32\7\3\2\2\32$\7\b\2\2\33%\3\2\2\2\34!\5")
        buf.write("\4\3\2\35\36\7\4\2\2\36 \5\4\3\2\37\35\3\2\2\2 #\3\2\2")
        buf.write("\2!\37\3\2\2\2!\"\3\2\2\2\"%\3\2\2\2#!\3\2\2\2$\33\3\2")
        buf.write("\2\2$\34\3\2\2\2%&\3\2\2\2&/\7\5\2\2\'+\7\6\2\2(*\5\b")
        buf.write("\5\2)(\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,.\3\2\2\2")
        buf.write("-+\3\2\2\2.\60\7\7\2\2/\'\3\2\2\2/\60\3\2\2\2\60\63\3")
        buf.write("\2\2\2\61\63\5\6\4\2\62\31\3\2\2\2\62\61\3\2\2\2\63\t")
        buf.write("\3\2\2\2\t\r\25!$+/\62")
        return buf.getvalue()


class ThttilParser ( Parser ):

    grammarFileName = "Thttil.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'$('", "','", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "FUNCTION", "PRINT", "STRING", 
                      "VARIABLE", "COMMENT", "WHITESPACE" ]

    RULE_program = 0
    RULE_argument = 1
    RULE_print_command = 2
    RULE_command = 3

    ruleNames =  [ "program", "argument", "print_command", "command" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    FUNCTION=6
    PRINT=7
    STRING=8
    VARIABLE=9
    COMMENT=10
    WHITESPACE=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._command = None # CommandContext
            self.commands = list() # of CommandContexts

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
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ThttilParser.T__0 or _la==ThttilParser.PRINT:
                self.state = 8
                localctx._command = self.command()
                localctx.commands.append(localctx._command)
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
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
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ThttilParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(ThttilParser.VARIABLE)
                pass
            elif token in [ThttilParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(ThttilParser.STRING)
                pass
            elif token in [ThttilParser.T__0, ThttilParser.PRINT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 18
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
        self.enterRule(localctx, 4, self.RULE_print_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
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
        self.enterRule(localctx, 6, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ThttilParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(ThttilParser.T__0)
                self.state = 24
                localctx.function = self.match(ThttilParser.FUNCTION)
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ThttilParser.T__2]:
                    pass
                elif token in [ThttilParser.T__0, ThttilParser.PRINT, ThttilParser.STRING, ThttilParser.VARIABLE]:
                    self.state = 26
                    localctx._argument = self.argument()
                    localctx.args.append(localctx._argument)
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ThttilParser.T__1:
                        self.state = 27
                        self.match(ThttilParser.T__1)
                        self.state = 28
                        localctx._argument = self.argument()
                        localctx.args.append(localctx._argument)
                        self.state = 33
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 36
                self.match(ThttilParser.T__2)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ThttilParser.T__3:
                    self.state = 37
                    self.match(ThttilParser.T__3)
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ThttilParser.T__0 or _la==ThttilParser.PRINT:
                        self.state = 38
                        localctx._command = self.command()
                        localctx.commands.append(localctx._command)
                        self.state = 43
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 44
                    self.match(ThttilParser.T__4)


                pass
            elif token in [ThttilParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
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





