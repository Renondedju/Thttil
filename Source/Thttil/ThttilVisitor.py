# Generated from Language\Grammar\Thttil.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ThttilParser import ThttilParser
else:
    from ThttilParser import ThttilParser

# This class defines a complete generic visitor for a parse tree produced by ThttilParser.

class ThttilVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ThttilParser#program.
    def visitProgram(self, ctx:ThttilParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThttilParser#argument.
    def visitArgument(self, ctx:ThttilParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThttilParser#stream_tag.
    def visitStream_tag(self, ctx:ThttilParser.Stream_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThttilParser#print_command.
    def visitPrint_command(self, ctx:ThttilParser.Print_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThttilParser#command.
    def visitCommand(self, ctx:ThttilParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThttilParser#instruction_block_content.
    def visitInstruction_block_content(self, ctx:ThttilParser.Instruction_block_contentContext):
        return self.visitChildren(ctx)



del ThttilParser