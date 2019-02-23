# MIT License

# Copyright (c) 2019 Basile Combet

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Generated from Thttil.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\64\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2")
        buf.write("\16\2\r\3\2\3\2\3\3\3\3\3\3\5\3\25\n\3\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\7\5\37\n\5\f\5\16\5\"\13\5\5\5$\n\5\3")
        buf.write("\5\3\5\3\5\6\5)\n\5\r\5\16\5*\3\5\3\5\5\5/\n\5\3\5\5\5")
        buf.write("\62\n\5\3\5\2\2\6\2\4\6\b\2\2\2\67\2\13\3\2\2\2\4\24\3")
        buf.write("\2\2\2\6\26\3\2\2\2\b\61\3\2\2\2\n\f\5\b\5\2\13\n\3\2")
        buf.write("\2\2\f\r\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\17\3\2\2")
        buf.write("\2\17\20\7\2\2\3\20\3\3\2\2\2\21\25\7\13\2\2\22\25\7\n")
        buf.write("\2\2\23\25\5\b\5\2\24\21\3\2\2\2\24\22\3\2\2\2\24\23\3")
        buf.write("\2\2\2\25\5\3\2\2\2\26\27\7\t\2\2\27\7\3\2\2\2\30\31\7")
        buf.write("\3\2\2\31#\7\b\2\2\32$\3\2\2\2\33 \5\4\3\2\34\35\7\4\2")
        buf.write("\2\35\37\5\4\3\2\36\34\3\2\2\2\37\"\3\2\2\2 \36\3\2\2")
        buf.write("\2 !\3\2\2\2!$\3\2\2\2\" \3\2\2\2#\32\3\2\2\2#\33\3\2")
        buf.write("\2\2$%\3\2\2\2%.\7\5\2\2&(\7\6\2\2\')\5\b\5\2(\'\3\2\2")
        buf.write("\2)*\3\2\2\2*(\3\2\2\2*+\3\2\2\2+,\3\2\2\2,-\7\7\2\2-")
        buf.write("/\3\2\2\2.&\3\2\2\2./\3\2\2\2/\62\3\2\2\2\60\62\5\6\4")
        buf.write("\2\61\30\3\2\2\2\61\60\3\2\2\2\62\t\3\2\2\2\t\r\24 #*")
        buf.write(".\61")
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
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                localctx._command = self.command()
                localctx.commands.append(localctx._command)
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ThttilParser.T__0 or _la==ThttilParser.PRINT):
                    break

            self.state = 13
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
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ThttilParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(ThttilParser.VARIABLE)
                pass
            elif token in [ThttilParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(ThttilParser.STRING)
                pass
            elif token in [ThttilParser.T__0, ThttilParser.PRINT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 17
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
            self.state = 20
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
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ThttilParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(ThttilParser.T__0)
                self.state = 23
                localctx.function = self.match(ThttilParser.FUNCTION)
                self.state = 33
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ThttilParser.T__2]:
                    pass
                elif token in [ThttilParser.T__0, ThttilParser.PRINT, ThttilParser.STRING, ThttilParser.VARIABLE]:
                    self.state = 25
                    localctx._argument = self.argument()
                    localctx.args.append(localctx._argument)
                    self.state = 30
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ThttilParser.T__1:
                        self.state = 26
                        self.match(ThttilParser.T__1)
                        self.state = 27
                        localctx._argument = self.argument()
                        localctx.args.append(localctx._argument)
                        self.state = 32
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 35
                self.match(ThttilParser.T__2)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ThttilParser.T__3:
                    self.state = 36
                    self.match(ThttilParser.T__3)
                    self.state = 38 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 37
                        localctx._command = self.command()
                        localctx.commands.append(localctx._command)
                        self.state = 40 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==ThttilParser.T__0 or _la==ThttilParser.PRINT):
                            break

                    self.state = 42
                    self.match(ThttilParser.T__4)


                pass
            elif token in [ThttilParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
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





