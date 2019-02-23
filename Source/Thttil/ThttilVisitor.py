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


    # Visit a parse tree produced by ThttilParser#print_command.
    def visitPrint_command(self, ctx:ThttilParser.Print_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThttilParser#command.
    def visitCommand(self, ctx:ThttilParser.CommandContext):
        return self.visitChildren(ctx)



del ThttilParser