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

import os

from  typing                    import Dict, Callable, List, Any, Union
from .ThttilParser              import ThttilParser
from .ThttilCommand             import ThttilCommand
from .ThttilVariablePool        import ThttilVariablePool
from .ThttilCommandReturnType   import ThttilCommandReturnType

class ThttilCommandCollection:
    # Every command parameter should be annotated either by 'content' or 'var'
    # This way you specify what type of argument you need
    # 'var' gives you a variable name
    # 'content' gives you any content, must be converted to Thttil data type to be printed to output stream

    class ForeachIterator:

        class Index:

            def __init__(self, index, max):
                self.value = index
                self.max   = max 

        def __init__(self, value, index, max):
            self.value = ""
            self.index = ThttilCommandCollection.ForeachIterator.Index(index, max)

    def __init__(self):
        self.__commands : Dict[str, Callable[List[...], Any]] = {method: getattr(self, method) 
            for method in dir(type(self)) if isinstance(getattr(self, method), ThttilCommand)}

    @staticmethod
    def ConvertData(data, strict: bool = False) -> Union[str, List[str]]:
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

    def Command(command = None,
                return_type: ThttilCommandReturnType = ThttilCommandReturnType.DATA, 
                pass_interpreter_instance: bool      = False,
                require_instruction_block: bool      = False,
                *args, **kwargs):
        """ Main decorator used to declare commands
        """

        if callable(command):
            return ThttilCommand(command, return_type, pass_interpreter_instance,
                require_instruction_block)
        else:
            def wrapper(function):
                return ThttilCommand(function, return_type, pass_interpreter_instance,
                    require_instruction_block, *args, **kwargs)
            
            return wrapper

    def GetCommand(self, name: str):
        if (not name in self.__commands):
            print("Thttil runtime error: no command named", name)
            return None
        
        return self.__commands[name]

    @staticmethod
    @Command(return_type = ThttilCommandReturnType.STREAM_DATA)
    def OUT(content: 'content') -> str:
        """ Default method to output something to the output stream
        """
        return ThttilCommandCollection.ConvertData(content, True)

    @staticmethod
    @Command(pass_interpreter_instance = True)
    def SET(interpreter, var_name: 'var', value: 'content' = "") -> None:
        """ Sets the content of a variable
        """
        interpreter.variable_pool.SetVar(var_name, value)
        return

    @staticmethod
    @Command
    def JOIN(array: 'content', char: 'content') -> None:
        return char.join(ThttilCommandCollection.ConvertData(array, False))

    @staticmethod
    @Command(pass_interpreter_instance = True, require_instruction_block = True)
    def IFEQ(interpreter, left_operand: 'content', right_operand: 'content', commands: List[ThttilParser.CommandContext]) -> None:
        """ Compares 2 operands and executes every command in the list 'commands' if the 2 operands are equals
        """
        if (left_operand == right_operand):
            for command in commands:
                interpreter.visit(command)

        return

    @staticmethod
    @Command(pass_interpreter_instance = True, require_instruction_block = True)
    def IFNEQ(interpreter, left_operand: 'content', right_operand: 'content', commands: List[ThttilParser.CommandContext]) -> None:
        """ Compares 2 operands and executes every command in the list 'commands' if the 2 operands are non equals
        """
        if (left_operand != right_operand):
            for command in commands:
                interpreter.visit(command)

        return

    @staticmethod
    @Command
    def SPLIT(content: 'content', char: 'content') -> List[Any]:
        content = ThttilCommandCollection.ConvertData(content, True)
        char    = ThttilCommandCollection.ConvertData(char   , True)
        if (char == ''):
            return [content]
        return content.split(char)

    @staticmethod
    @Command
    def PRINT(content: 'content') -> None:
        """ Prints some content to the console
        """
        print(content)
        return

    @staticmethod
    @Command
    def UPPER(content: 'content') -> None:
        """ Returns the input content to upper
        """
        return ThttilCommandCollection.ConvertData(content, True).upper()

    @staticmethod
    @Command
    def LOWER(content: 'content') -> None:
        """ Returns the input content to lower
        """
        return ThttilCommandCollection.ConvertData(content, True).lower()

    @staticmethod
    @Command
    def TITLE(content: 'content') -> None:
        """ Returns the input content to title
        """
        return ThttilCommandCollection.ConvertData(content, True).lower()

    @staticmethod
    @Command
    def SHELL(command: 'content') -> None:
        """ Returns the result of a command
        """ 
        return os.popen(ThttilCommandCollection.ConvertData(command, True)).read()[:-1]

    @staticmethod
    @Command(pass_interpreter_instance = True)
    def CREATE(interpreter, var_name: 'content', default_value: 'content' = "") -> None:
        """ Creates a variable and sets it's default value
        """
        interpreter.variable_pool.CreateVar(var_name, default_value)
        return

    @staticmethod
    @Command(pass_interpreter_instance = True)
    def DELETE(interpreter, var_name: 'var') -> None:
        """ Deletes a variable
        """
        interpreter.variable_pool.DeleteVar(var_name)
        return

    @staticmethod
    @Command(pass_interpreter_instance = True, require_instruction_block = True)
    def FOREACH(interpreter, temp_var_name: 'content', array: List['content'], commands: List[ThttilParser.CommandContext]) -> None:
        """ Iterates over an array of strings
        """
        if (isinstance(array, str)):
            array = [array]

        interpreter.variable_pool.CreateVar(temp_var_name, ThttilCommandCollection.ForeachIterator("", "0", str(len(array) - 1)))

        for index, value in enumerate(array):
            interpreter.variable_pool.SetVar(temp_var_name + '.value', value)
            interpreter.variable_pool.SetVar(temp_var_name + '.index.value', str(index))
            for command in commands:
                interpreter.visit(command)

        interpreter.variable_pool.DeleteVar(temp_var_name)
        return

    @staticmethod
    @Command(pass_interpreter_instance = True)
    def REPLACE(interpreter, content: 'content', target: 'content', replacement: 'content') -> None:
        target      = ThttilCommandCollection.ConvertData(target     , True)
        content     = ThttilCommandCollection.ConvertData(content    , True)
        replacement = ThttilCommandCollection.ConvertData(replacement, True)

        return content.replace(target, replacement)
