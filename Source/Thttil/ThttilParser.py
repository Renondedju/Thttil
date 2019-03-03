# Generated from Language\Grammar\Thttil.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("Z\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2\3\2\3")
        buf.write("\2\7\2\34\n\2\f\2\16\2\37\13\2\3\2\3\2\3\3\3\3\5\3%\n")
        buf.write("\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\5\78\n\7\3\b\3\b\3\b\3\b\3\b\3\b\7\b")
        buf.write("@\n\b\f\b\16\bC\13\b\5\bE\n\b\3\b\3\b\3\b\7\bJ\n\b\f\b")
        buf.write("\16\bM\13\b\3\b\5\bP\n\b\3\b\5\bS\n\b\3\t\3\t\3\t\5\t")
        buf.write("X\n\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\3\4\2\16\16\20\20")
        buf.write("\2^\2\25\3\2\2\2\4$\3\2\2\2\6&\3\2\2\2\b(\3\2\2\2\n,\3")
        buf.write("\2\2\2\f.\3\2\2\2\16R\3\2\2\2\20W\3\2\2\2\22\24\5\f\7")
        buf.write("\2\23\22\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2")
        buf.write("\2\2\26\35\3\2\2\2\27\25\3\2\2\2\30\34\5\16\b\2\31\34")
        buf.write("\5\6\4\2\32\34\5\b\5\2\33\30\3\2\2\2\33\31\3\2\2\2\33")
        buf.write("\32\3\2\2\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2")
        buf.write("\36 \3\2\2\2\37\35\3\2\2\2 !\7\2\2\3!\3\3\2\2\2\"%\t\2")
        buf.write("\2\2#%\5\16\b\2$\"\3\2\2\2$#\3\2\2\2%\5\3\2\2\2&\'\7\17")
        buf.write("\2\2\'\7\3\2\2\2()\7\17\2\2)*\7\5\2\2*+\7\17\2\2+\t\3")
        buf.write("\2\2\2,-\7\r\2\2-\13\3\2\2\2./\7\3\2\2/\60\7\7\2\2\60")
        buf.write("\61\7\23\2\2\61\67\7\6\2\2\628\3\2\2\2\63\64\7\4\2\2\64")
        buf.write("\65\7\7\2\2\65\66\7\22\2\2\668\7\6\2\2\67\62\3\2\2\2\67")
        buf.write("\63\3\2\2\28\r\3\2\2\29:\7\b\2\2:D\7\21\2\2;E\3\2\2\2")
        buf.write("<A\5\4\3\2=>\7\n\2\2>@\5\4\3\2?=\3\2\2\2@C\3\2\2\2A?\3")
        buf.write("\2\2\2AB\3\2\2\2BE\3\2\2\2CA\3\2\2\2D;\3\2\2\2D<\3\2\2")
        buf.write("\2EF\3\2\2\2FO\7\t\2\2GK\7\13\2\2HJ\5\20\t\2IH\3\2\2\2")
        buf.write("JM\3\2\2\2KI\3\2\2\2KL\3\2\2\2LN\3\2\2\2MK\3\2\2\2NP\7")
        buf.write("\f\2\2OG\3\2\2\2OP\3\2\2\2PS\3\2\2\2QS\5\n\6\2R9\3\2\2")
        buf.write("\2RQ\3\2\2\2S\17\3\2\2\2TX\5\16\b\2UX\5\6\4\2VX\5\b\5")
        buf.write("\2WT\3\2\2\2WU\3\2\2\2WV\3\2\2\2X\21\3\2\2\2\r\25\33\35")
        buf.write("$\67ADKORW")
        return buf.getvalue()


class ThttilParser ( Parser ):

    grammarFileName = "Thttil.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'using'", "'as'", "'->'", "'>'", "'<'", 
                     "'$('", "')'", "','", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "USING", "AS", "ARROW", "END_USING_STRING", 
                      "BEGIN_USING_STRING", "BEGIN_TOKEN", "END_TOKEN", 
                      "ARGUMENT_SEPARATOR", "BEGIN_INSTRUCTION_BLOCK", "END_INSTRUCTION_BLOCK", 
                      "PRINT", "STRING", "STREAM_TAG", "VARIABLE", "FUNCTION", 
                      "ALIAS", "FILENAME", "COMMENT", "WHITESPACE" ]

    RULE_program = 0
    RULE_argument = 1
    RULE_stream_tag = 2
    RULE_stream_redirection = 3
    RULE_print_command = 4
    RULE_using = 5
    RULE_command = 6
    RULE_instruction_block_content = 7

    ruleNames =  [ "program", "argument", "stream_tag", "stream_redirection", 
                   "print_command", "using", "command", "instruction_block_content" ]

    EOF = Token.EOF
    USING=1
    AS=2
    ARROW=3
    END_USING_STRING=4
    BEGIN_USING_STRING=5
    BEGIN_TOKEN=6
    END_TOKEN=7
    ARGUMENT_SEPARATOR=8
    BEGIN_INSTRUCTION_BLOCK=9
    END_INSTRUCTION_BLOCK=10
    PRINT=11
    STRING=12
    STREAM_TAG=13
    VARIABLE=14
    FUNCTION=15
    ALIAS=16
    FILENAME=17
    COMMENT=18
    WHITESPACE=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ThttilParser.EOF, 0)

        def using(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThttilParser.UsingContext)
            else:
                return self.getTypedRuleContext(ThttilParser.UsingContext,i)


        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThttilParser.CommandContext)
            else:
                return self.getTypedRuleContext(ThttilParser.CommandContext,i)


        def stream_tag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThttilParser.Stream_tagContext)
            else:
                return self.getTypedRuleContext(ThttilParser.Stream_tagContext,i)


        def stream_redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThttilParser.Stream_redirectionContext)
            else:
                return self.getTypedRuleContext(ThttilParser.Stream_redirectionContext,i)


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
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ThttilParser.USING:
                self.state = 16
                self.using()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ThttilParser.BEGIN_TOKEN) | (1 << ThttilParser.PRINT) | (1 << ThttilParser.STREAM_TAG))) != 0):
                self.state = 25
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 22
                    self.command()
                    pass

                elif la_ == 2:
                    self.state = 23
                    self.stream_tag()
                    pass

                elif la_ == 3:
                    self.state = 24
                    self.stream_redirection()
                    pass


                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
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
        self._la = 0 # Token type
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ThttilParser.STRING, ThttilParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                _la = self._input.LA(1)
                if not(_la==ThttilParser.STRING or _la==ThttilParser.VARIABLE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [ThttilParser.BEGIN_TOKEN, ThttilParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
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
            self.state = 36
            self.match(ThttilParser.STREAM_TAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stream_redirectionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.input_stream = None # Token
            self.output_stream = None # Token

        def ARROW(self):
            return self.getToken(ThttilParser.ARROW, 0)

        def STREAM_TAG(self, i:int=None):
            if i is None:
                return self.getTokens(ThttilParser.STREAM_TAG)
            else:
                return self.getToken(ThttilParser.STREAM_TAG, i)

        def getRuleIndex(self):
            return ThttilParser.RULE_stream_redirection

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStream_redirection" ):
                return visitor.visitStream_redirection(self)
            else:
                return visitor.visitChildren(self)




    def stream_redirection(self):

        localctx = ThttilParser.Stream_redirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stream_redirection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            localctx.input_stream = self.match(ThttilParser.STREAM_TAG)
            self.state = 39
            self.match(ThttilParser.ARROW)
            self.state = 40
            localctx.output_stream = self.match(ThttilParser.STREAM_TAG)
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
        self.enterRule(localctx, 8, self.RULE_print_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(ThttilParser.PRINT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UsingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USING(self):
            return self.getToken(ThttilParser.USING, 0)

        def BEGIN_USING_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ThttilParser.BEGIN_USING_STRING)
            else:
                return self.getToken(ThttilParser.BEGIN_USING_STRING, i)

        def FILENAME(self):
            return self.getToken(ThttilParser.FILENAME, 0)

        def END_USING_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ThttilParser.END_USING_STRING)
            else:
                return self.getToken(ThttilParser.END_USING_STRING, i)

        def AS(self):
            return self.getToken(ThttilParser.AS, 0)

        def ALIAS(self):
            return self.getToken(ThttilParser.ALIAS, 0)

        def getRuleIndex(self):
            return ThttilParser.RULE_using

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsing" ):
                return visitor.visitUsing(self)
            else:
                return visitor.visitChildren(self)




    def using(self):

        localctx = ThttilParser.UsingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_using)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ThttilParser.USING)
            self.state = 45
            self.match(ThttilParser.BEGIN_USING_STRING)
            self.state = 46
            self.match(ThttilParser.FILENAME)
            self.state = 47
            self.match(ThttilParser.END_USING_STRING)
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ThttilParser.EOF, ThttilParser.USING, ThttilParser.BEGIN_TOKEN, ThttilParser.PRINT, ThttilParser.STREAM_TAG]:
                pass
            elif token in [ThttilParser.AS]:
                self.state = 49
                self.match(ThttilParser.AS)
                self.state = 50
                self.match(ThttilParser.BEGIN_USING_STRING)
                self.state = 51
                self.match(ThttilParser.ALIAS)
                self.state = 52
                self.match(ThttilParser.END_USING_STRING)
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


    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.function = None # Token
            self._argument = None # ArgumentContext
            self.args = list() # of ArgumentContexts
            self._instruction_block_content = None # Instruction_block_contentContext
            self.commands = list() # of Instruction_block_contentContexts

        def BEGIN_TOKEN(self):
            return self.getToken(ThttilParser.BEGIN_TOKEN, 0)

        def END_TOKEN(self):
            return self.getToken(ThttilParser.END_TOKEN, 0)

        def FUNCTION(self):
            return self.getToken(ThttilParser.FUNCTION, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThttilParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(ThttilParser.ArgumentContext,i)


        def BEGIN_INSTRUCTION_BLOCK(self):
            return self.getToken(ThttilParser.BEGIN_INSTRUCTION_BLOCK, 0)

        def END_INSTRUCTION_BLOCK(self):
            return self.getToken(ThttilParser.END_INSTRUCTION_BLOCK, 0)

        def ARGUMENT_SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(ThttilParser.ARGUMENT_SEPARATOR)
            else:
                return self.getToken(ThttilParser.ARGUMENT_SEPARATOR, i)

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
        self.enterRule(localctx, 12, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ThttilParser.BEGIN_TOKEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(ThttilParser.BEGIN_TOKEN)
                self.state = 56
                localctx.function = self.match(ThttilParser.FUNCTION)
                self.state = 66
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ThttilParser.END_TOKEN]:
                    pass
                elif token in [ThttilParser.BEGIN_TOKEN, ThttilParser.PRINT, ThttilParser.STRING, ThttilParser.VARIABLE]:
                    self.state = 58
                    localctx._argument = self.argument()
                    localctx.args.append(localctx._argument)
                    self.state = 63
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ThttilParser.ARGUMENT_SEPARATOR:
                        self.state = 59
                        self.match(ThttilParser.ARGUMENT_SEPARATOR)
                        self.state = 60
                        localctx._argument = self.argument()
                        localctx.args.append(localctx._argument)
                        self.state = 65
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 68
                self.match(ThttilParser.END_TOKEN)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ThttilParser.BEGIN_INSTRUCTION_BLOCK:
                    self.state = 69
                    self.match(ThttilParser.BEGIN_INSTRUCTION_BLOCK)
                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ThttilParser.BEGIN_TOKEN) | (1 << ThttilParser.PRINT) | (1 << ThttilParser.STREAM_TAG))) != 0):
                        self.state = 70
                        localctx._instruction_block_content = self.instruction_block_content()
                        localctx.commands.append(localctx._instruction_block_content)
                        self.state = 75
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 76
                    self.match(ThttilParser.END_INSTRUCTION_BLOCK)


                pass
            elif token in [ThttilParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
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


        def stream_redirection(self):
            return self.getTypedRuleContext(ThttilParser.Stream_redirectionContext,0)


        def getRuleIndex(self):
            return ThttilParser.RULE_instruction_block_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction_block_content" ):
                return visitor.visitInstruction_block_content(self)
            else:
                return visitor.visitChildren(self)




    def instruction_block_content(self):

        localctx = ThttilParser.Instruction_block_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_instruction_block_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 82
                self.command()
                pass

            elif la_ == 2:
                self.state = 83
                self.stream_tag()
                pass

            elif la_ == 3:
                self.state = 84
                self.stream_redirection()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





