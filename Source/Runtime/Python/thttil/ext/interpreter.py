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

import thttil

from thttil.ext.argument_parser import ArgumentParser

class DefaultThttilInterpreter:
    """ This is the default Thttil interpreter, read readme.md for more information.
        Python 3.5+ is required. Python 3.x versions might work but those have not been
        tested, use them at your won risks.
        To get more help of how to use this luncher please execute : ``python Thttil.py -h``
    """
    
    __slots__ = ("arg_parser", "collection")

    def __init__(self):
        """ Main method of the default interpreter """

        self.arg_parser = ArgumentParser()
        self.collection = thttil.CommandCollection(None)

        if self.arg_parser.template:
            self.run_template_file()
        else:
            self.run_live_interpretation()

    def run_live_interpretation(self):

        try:
            content = input("}> ")
            while (True):

                byte = thttil.Bytes.ofString(content)
                thttil_parser = thttil.Parser(byte, "<thttil python live interpreter>")

                for instruction in thttil_parser.parseProgram().instructions:
                    self.pretty_print(instruction, byte)
                    if (instruction.command_name == "EXIT"):
                        exit(0)

                content = input("}> ")

        except KeyboardInterrupt:
            exit(0)

    def run_template_file(self):

        with open(self.arg_parser.template, "rt") as file:
            content = thttil.Bytes.ofString(file.read())

        thttil_parser = thttil.Parser(content, self.arg_parser.template)

        for instruction in thttil_parser.parseProgram().instructions:
            self.pretty_print(instruction, content)

    @staticmethod
    def pretty_print(instruction, content):
        print("{0.command_name:<15} @{0.position.psource}:{0.position.pmin:<5} {1}"
        
        .format(instruction, content.getString(instruction.position.pmin, instruction.position.pmax - instruction.position.pmin)
            .replace("\n", "\\n")
            .replace("\t", "\\t")))