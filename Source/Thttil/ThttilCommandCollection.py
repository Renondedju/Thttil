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

from  typing             import Dict, Callable, List, Any
from .ThttilParser       import ThttilParser
from .ThttilVariablePool import ThttilVariablePool

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

    def __init__(self, interperter_instance: 'ThttilCommandInterpreter'):
        self.__interperter_instance: 'ThttilCommandInterpreter' = interperter_instance
        self.__commands            : Dict[str, Callable[List[...], Any]] = {
                "OUT"    : ThttilCommandCollection.OUT,
                "SET"    : ThttilCommandCollection.SET,
                "IFEQ"   : ThttilCommandCollection.IFEQ,
                "JOIN"   : ThttilCommandCollection.JOIN,
                "IFNEQ"  : ThttilCommandCollection.IFNEQ,
                "SPLIT"  : ThttilCommandCollection.SPLIT,
                "PRINT"  : ThttilCommandCollection.PRINT,
                "UPPER"  : ThttilCommandCollection.UPPER,
                "LOWER"  : ThttilCommandCollection.LOWER,
                "TITLE"  : ThttilCommandCollection.TITLE,
                "SHELL"  : ThttilCommandCollection.SHELL,
                "CREATE" : ThttilCommandCollection.CREATE,
                "DELETE" : ThttilCommandCollection.DELETE,
                "FOREACH": ThttilCommandCollection.FOREACH,
                "REPLACE": ThttilCommandCollection.REPLACE
            }

    def GetCommand(self, name: str):
        if (not name in self.__commands):
            print("Thttil runtime error: no command named", name)
            return None
        
        return self.__commands[name]

    def OUT(self, content: 'content') -> None:
        """ Default method to output something to the output stream
        """
        self.__interperter_instance.output_stream += self.__interperter_instance.convertData(content, True)
        return

    def SET(self, var_name: 'var', value: 'content' = "") -> None:
        """ Sets the content of a variable
        """
        self.__interperter_instance.variable_pool.SetVar(var_name, value)

        return

    def JOIN(self, array: 'content', char: 'content') -> None:
        self.OUT(char.join(self.__interperter_instance.convertData(array, False)))
        return

    def IFEQ(self, left_operand: 'content', right_operand: 'content', commands: List[ThttilParser.CommandContext]) -> None:
        """ Compares 2 operands and executes every command in the list 'commands' if the 2 operands are equals
        """
        if (left_operand == right_operand):
            for command in commands:
                self.__interperter_instance.visit(command)

        return

    def IFNEQ(self, left_operand: 'content', right_operand: 'content', commands: List[ThttilParser.CommandContext]) -> None:
        """ Compares 2 operands and executes every command in the list 'commands' if the 2 operands are non equals
        """
        if (left_operand != right_operand):
            for command in commands:
                self.__interperter_instance.visit(command)

        return

    def SPLIT(self, content: 'content', char: 'content') -> List[Any]:
        content = self.__interperter_instance.convertData(content, True)
        char    = self.__interperter_instance.convertData(char, True)
        if (char == ''):
            return [content]
        return content.split(char)

    def PRINT(self, content: 'content') -> None:
        """ Prints some content to the console
        """
        print(content)
        return

    def UPPER(self, content: 'content') -> None:
        """ Returns the input content to upper
        """
        self.OUT(self.__interperter_instance.convertData(content, True).upper())
        return

    def LOWER(self, content: 'content') -> None:
        """ Returns the input content to lower
        """
        self.OUT(self.__interperter_instance.convertData(content, True).lower())
        return

    def TITLE(self, content: 'content') -> None:
        """ Returns the input content to title
        """
        self.OUT(self.__interperter_instance.convertData(content, True).title())
        return

    def SHELL(self, command: 'content') -> None:
        """ Returns the result of a command
        """ 
        self.OUT(os.popen(self.__interperter_instance.convertData(command, True)).read()[:-1])
        return

    def CREATE(self, var_name: 'content', default_value: 'content' = "") -> None:
        """ Creates a variable and sets it's default value
        """
        self.__interperter_instance.variable_pool.CreateVar(var_name, default_value)
        return

    def DELETE(self, var_name: 'content') -> None:
        """ Deletes a variable
        """
        self.__interperter_instance.variable_pool.DeleteVar(var_name)
        return

    def FOREACH(self, temp_var_name: 'content', array: List['content'], commands: List[ThttilParser.CommandContext]) -> None:
        """ Iterates over an array of strings
        """

        if (isinstance(array, str)):
            array = [array]

        self.__interperter_instance.variable_pool.CreateVar(temp_var_name, ThttilCommandCollection.ForeachIterator("", "0", str(len(array) - 1)))

        for index, value in enumerate(array):
            self.__interperter_instance.variable_pool.SetVar(temp_var_name + '.value', value)
            self.__interperter_instance.variable_pool.SetVar(temp_var_name + '.index.value', str(index))
            for command in commands:
                self.__interperter_instance.visit(command)

        self.__interperter_instance.variable_pool.DeleteVar(temp_var_name)

        return

    def REPLACE(self, content: 'content', target: 'content', replacement: 'content') -> None:
        target      = self.__interperter_instance.convertData(target     , True)
        content     = self.__interperter_instance.convertData(content    , True)
        replacement = self.__interperter_instance.convertData(replacement, True)
        self.OUT(content.replace(target, replacement))
        return
