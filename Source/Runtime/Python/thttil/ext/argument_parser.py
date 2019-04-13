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

import argparse
import os

class ArgumentParser:

    def __init__(self):
        self._declareArgs()

        #Parsing arguments
        self.args       : dict = self.parser.parse_args()

        self.variables  : dict = self._parseVariables(self.args.variables)
        self.outputs    : dict = self._parseOutputs  (self.args.outputs)
        self.template   : str  = self.args.template

        self._checkArgs()

    def _checkArgs(self):

        #Checking the template file
        if (self.template):
            if (not os.path.isfile(self.template)):
                print(f"Error: the template file named \"{ self.template }\" does not exists.")
                exit(1)

    def _parseVariables(self, items: list = []):
        variables = {}

        if not items:
            return variables

        for item in items:
            if not '=' in item:
                print(f"Error: invalid variable declaration \"{item}\"")
                exit(1)
            key, value = item.split('=', 1)
            variables[key] = value

        return variables

    def _parseOutputs(self, items: list = []):
        outputs = {}

        if not items:
            return outputs

        for item in items:
            if not ':' in item:
                print(f"Error: invalid output declaration \"{item}\"")
                exit(1)
            key, value = item.split(':', 1)
            outputs[key] = value

        return outputs

    def _declareArgs(self):
        #Generating argparse data
        self.parser = argparse.ArgumentParser("Thttil luncher", description="Default thttil luncher")
        self.parser._action_groups.pop()
        self.required_args = self.parser.add_argument_group("required arguments")
        self.optional_args = self.parser.add_argument_group("optional arguments")
        
        self.optional_args.add_argument('-o', '--outputs', type=str, nargs='+', metavar='outputs', default=["default:Output/thttil.default.txt"],
            help="Name of the stream, followed by the name of the output file. eg. 'default:default.txt' (default: default:./Output/thttil.default.txt)")

        self.optional_args.add_argument('-v', '--variables', type=str, nargs='+', metavar='variables',
            help="Variables to declare before the interpretation (format must be: var_name=value or var_name=\"some other values\")")

        self.optional_args.add_argument('-t', '--template', type=str, metavar='template',
            help="Path to the template file to interpret (*.t, *.thtt, *.thttil file)")