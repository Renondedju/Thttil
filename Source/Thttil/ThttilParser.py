# Generated from Language\Grammar\Thttil.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\5\3\34\n\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\7\6(\n\6\f\6\16\6+\13\6\5\6-\n\6\3\6\3\6\3\6\7\6\62\n")
        buf.write("\6\f\6\16\6\65\13\6\3\6\5\68\n\6\3\6\5\6;\n\6\3\7\3\7")
        buf.write("\5\7?\n\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2D\2\16\3\2\2\2\4")
        buf.write("\33\3\2\2\2\6\35\3\2\2\2\b\37\3\2\2\2\n:\3\2\2\2\f>\3")
        buf.write("\2\2\2\16\23\5\6\4\2\17\22\5\n\6\2\20\22\5\6\4\2\21\17")
        buf.write("\3\2\2\2\21\20\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\23")
        buf.write("\24\3\2\2\2\24\26\3\2\2\2\25\23\3\2\2\2\26\27\7\2\2\3")
        buf.write("\27\3\3\2\2\2\30\34\7\f\2\2\31\34\7\13\2\2\32\34\5\n\6")
        buf.write("\2\33\30\3\2\2\2\33\31\3\2\2\2\33\32\3\2\2\2\34\5\3\2")
        buf.write("\2\2\35\36\7\b\2\2\36\7\3\2\2\2\37 \7\n\2\2 \t\3\2\2\2")
        buf.write("!\"\7\3\2\2\",\7\t\2\2#-\3\2\2\2$)\5\4\3\2%&\7\4\2\2&")
        buf.write("(\5\4\3\2\'%\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*-")
        buf.write("\3\2\2\2+)\3\2\2\2,#\3\2\2\2,$\3\2\2\2-.\3\2\2\2.\67\7")
        buf.write("\5\2\2/\63\7\6\2\2\60\62\5\f\7\2\61\60\3\2\2\2\62\65\3")
        buf.write("\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65\63")
        buf.write("\3\2\2\2\668\7\7\2\2\67/\3\2\2\2\678\3\2\2\28;\3\2\2\2")
        buf.write("9;\5\b\5\2:!\3\2\2\2:9\3\2\2\2;\13\3\2\2\2<?\5\n\6\2=")
        buf.write("?\5\6\4\2><\3\2\2\2>=\3\2\2\2?\r\3\2\2\2\13\21\23\33)")
        buf.write(",\63\67:>")
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
    RULE_instruction_block_content = 5

    ruleNames =  [ "program", "argument", "stream_tag", "print_command", 
                   "command", "instruction_block_content" ]

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
            self.state = 12
            self.stream_tag()
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ThttilParser.T__0) | (1 << ThttilParser.STREAM_TAG) | (1 << ThttilParser.PRINT))) != 0):
                self.state = 15
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ThttilParser.T__0, ThttilParser.PRINT]:
                    self.state = 13
                    self.command()
                    pass
                elif token in [ThttilParser.STREAM_TAG]:
                    self.state = 14
                    self.stream_tag()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
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
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ThttilParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(ThttilParser.VARIABLE)
                pass
            elif token in [ThttilParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(ThttilParser.STRING)
                pass
            elif token in [ThttilParser.T__0, ThttilParser.PRINT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
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
            self.state = 27
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
            self.state = 29
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
            self._instruction_block_content = None # Instruction_block_contentContext
            self.commands = list() # of Instruction_block_contentContexts

        def FUNCTION(self):
            return self.getToken(ThttilParser.FUNCTION, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThttilParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(ThttilParser.ArgumentContext,i)


        def instruction_block_content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThttilParser.Instruction_block_contentContext)
            else:
                return self.getTypedRuleContext(ThttilParser.Instruction_block_contentContext,i)


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
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ThttilParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(ThttilParser.T__0)
                self.state = 32
                localctx.function = self.match(ThttilParser.FUNCTION)
                self.state = 42
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ThttilParser.T__2]:
                    pass
                elif token in [ThttilParser.T__0, ThttilParser.PRINT, ThttilParser.STRING, ThttilParser.VARIABLE]:
                    self.state = 34
                    localctx._argument = self.argument()
                    localctx.args.append(localctx._argument)
                    self.state = 39
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ThttilParser.T__1:
                        self.state = 35
                        self.match(ThttilParser.T__1)
                        self.state = 36
                        localctx._argument = self.argument()
                        localctx.args.append(localctx._argument)
                        self.state = 41
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 44
                self.match(ThttilParser.T__2)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ThttilParser.T__3:
                    self.state = 45
                    self.match(ThttilParser.T__3)
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ThttilParser.T__0) | (1 << ThttilParser.STREAM_TAG) | (1 << ThttilParser.PRINT))) != 0):
                        self.state = 46
                        localctx._instruction_block_content = self.instruction_block_content()
                        localctx.commands.append(localctx._instruction_block_content)
                        self.state = 51
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 52
                    self.match(ThttilParser.T__4)


                pass
            elif token in [ThttilParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
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


    class Instruction_block_contentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(ThttilParser.CommandContext,0)


        def stream_tag(self):
            return self.getTypedRuleContext(ThttilParser.Stream_tagContext,0)


        def getRuleIndex(self):
            return ThttilParser.RULE_instruction_block_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction_block_content" ):
                return visitor.visitInstruction_block_content(self)
            else:
                return visitor.visitChildren(self)




    def instruction_block_content(self):

        localctx = ThttilParser.Instruction_block_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_instruction_block_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ThttilParser.T__0, ThttilParser.PRINT]:
                self.state = 58
                self.command()
                pass
            elif token in [ThttilParser.STREAM_TAG]:
                self.state = 59
                self.stream_tag()
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





