# -*-coding:utf-8 -*-

# MIT License
# 
# Copyright (c) 2019 Renondedju
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from thttil         import CommandCollection, Parser, Bytes
from thttil.symbols import Program

class Interpreter(object):
    """ Thttil interpreter """

    __slots__ = ("parser", "program", "command_collection")

    def __init__(self, command_collection: CommandCollection = None):

        self.parser            : Parser                 = None
        self.program           : thttil.symbols.Program = None
        self.command_collection: CommandCollection = command_collection

        if not self.command_collection:
            self.command_collection: CommandCollection = CommandCollection(self)

    def interpret(self):
        
        for token in self.program.instructions:
            print(token.command_name)

    def interpret_content(self, content: str, source: str = "unknown"):
        """ Interprets some arbitrary content """

        self.parser  = Parser(Bytes.ofString(content), source)
        self.program = self.parser.parseProgram()
        self.interpret()

    def interpret_file(self, filename: str):
        """ Interprets a thtt file """

        with open(filename, 'rt') as file:
            self.parser = Parser(Bytes.ofString(file.read()), filename)

        self.program = self.parser.parseProgram()
        self.interpret()