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

from  typing                     import Callable, List, Union, Any
from .ThttilParser               import ThttilParser
from .ThttilVisitor              import ThttilVisitor
from .ThttilVariablePool         import ThttilVariablePool
from .ThttilCommandCollection    import ThttilCommandCollection

import re

class ThttilCommandInterpreter(ThttilVisitor):

    def __init__(self):
        self.output_stream     : str                         = ""
        self.variable_pool     : ThttilVariablePool          = ThttilVariablePool()
        self.command_collection: ThttilCommandCollection     = ThttilCommandCollection(self)

    def convertData(self, data, strict: bool = False) -> Union[str, List[str]]:
        """ Converts any python data to Thttil readable data
            If strict = True, the data returned will always be string
        """
        if (strict):
            return str(data)

        if (isinstance(data, str)):
            return data

        if (hasattr(data, '__iter__')):
            return [str(item) for item in data]

        return str(data)

    def visitArgument(self, ctx: ThttilParser.ArgumentContext, request_var: bool) -> str:
        """ Visits an argument and retuns it's content or name
        """

        if (ctx.STRING() != None):
            if request_var:
                # Requested a variable but we only carry a string ERROR
                return ""
            # Requested a data, got a string
            return ctx.STRING().getText()[1:-1]

        if (ctx.VARIABLE() != None):
            if request_var:
                #requested a var name, got a variable name
                return ctx.VARIABLE().getText()[1:]
            # Requested a data, got a variable content
            return self.variable_pool.GetVar(ctx.VARIABLE().getText()[1:])

        if request_var:
            # Requested a variable name, got a token to parse ERROR
            return ""

        # Requested a data, got a token to parse
        return self.visit(ctx.command())

    def visitPrint_command(self, ctx: ThttilParser.Print_commandContext):
        self.output_stream += ctx.PRINT().getText()[1:-1]
        return

    def visitCommand(self, ctx: ThttilParser.CommandContext) -> Any:

        if(ctx.print_command()):
            return self.visit(ctx.print_command())

        command = self.command_collection.GetCommand(ctx.function.text)
        if (command == None):
            return ""

        args     : List[str] = []
        args_type: List[str] = [arg for arg in command.__annotations__.values() if arg != List[ThttilParser.CommandContext]]

        if (len(ctx.args) != len(args_type) - 1):
            print("Thttil runtime error: the function named", ctx.function.text,
                "takes", str(len(args_type) - 1), "argument(s), got", len(ctx.args))
            return ""

        for index, argument in enumerate(ctx.args):
            args.append(self.visitArgument(argument, args_type[index] == 'var'))

        if (len(ctx.commands) > 0):
            return command(self.command_collection, *args, ctx.commands)

        return command(self.command_collection, *args)

    def visitProgram(self, ctx: ThttilParser.ProgramContext) -> str:
        """ Executes the program and returns the content result
        """

        self.output_stream = ""
        for command in ctx.commands:
            self.visit(command)

        return self.output_stream