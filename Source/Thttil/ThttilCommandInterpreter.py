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
from .ThttilCommandReturnType    import ThttilCommandReturnType

import re

class ThttilCommandInterpreter(ThttilVisitor):

    def __init__(self, command_collection = ThttilCommandCollection()):
        self.output_stream     : str                         = ""
        self.variable_pool     : ThttilVariablePool          = ThttilVariablePool()
        self.command_collection: ThttilCommandCollection     = command_collection

    def handleData(self, content: Any, push_to_steam: bool = False):
        if push_to_steam:
            self.output_stream += ThttilCommandCollection.ConvertData(content)
            return ""
        return content

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

        # ctx.args are the received args from Thttil
        args: List[Any] = []
        if (len(ctx.args) < command.min_required_args):
            print(f"Thttil runtime error: the function named \"{ctx.function.text}\""
                  f" takes at least {command.min_required_args} argument(s), got {len(ctx.args)}")
            return ""

        if (len(ctx.args) > command.max_args):
            print(f"Thttil runtime error: the function named \"{ctx.function.text}\""
                  f" takes maximum {command.max_args} argument(s), got {len(ctx.args)}")
            return ""

        for index, argument in enumerate(ctx.args):
            args.append(self.visitArgument(argument, command.arguments[index].type == 'var'))

        if (command.require_instruction_block):
            if (len(ctx.commands) == 0):
                print(f"Thttil runtime error: the function named \"{ctx.function.text}\""
                      f" requires an instruction block after it.")
                exit(1)
            args.append(ctx.commands)

        push_to_stream: bool = command.return_type == ThttilCommandReturnType.STREAM_DATA
        if command.requires_interpreter_instance:
            return self.handleData(command(self, *args), push_to_stream)
        return self.handleData(command(*args), push_to_stream)

    def visitProgram(self, ctx: ThttilParser.ProgramContext) -> str:
        """ Executes the program and returns the content result
        """

        self.output_stream = ""
        for command in ctx.commands:
            self.visit(command)

        return self.output_stream