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

import argparse
import Thttil
import os

""" This is the default Thttil luncher, read hackme.md for more information.
    Python 3.5+ is required. Python 3.x versions might work but those have not been
    tested, use them at your won risks.

    To get more help of how to use this luncher please execute : ``python Thttil.py -h``
"""

class ArgParser:

    def __init__(self):
        self._declareArgs()

        #Parsing arguments
        self.args       : dict = self.parser.parse_args()

        self.output_path, self.output_filename = os.path.split(self.args.output)
        self.variables  : dict = self._parseVariables(self.args.variables)
        self.template   : str  = self.args.template

        self._checkArgs()

    def _checkArgs(self):

        #Checking the template file
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

    def _declareArgs(self):
        #Generating argparse data
        self.parser = argparse.ArgumentParser("Thttil luncher", description="Default thttil luncher")
        self.parser._action_groups.pop()
        self.required_args = self.parser.add_argument_group("required arguments")
        self.optional_args = self.parser.add_argument_group("optional arguments")
        
        self.optional_args.add_argument('-o', '--output', type=str, metavar='output', default="./thttil.output.txt",
            help="Name of the output file. (default: ./thttil.output.txt)")

        self.optional_args.add_argument('-v', '--variables', type=str, nargs='+', metavar='variables',
            help="Variables to declare before the interpretation (format must be: var_name=value)")

        self.required_args.add_argument('-t', '--template', type=str, metavar='template',
            help="Template file to interpret (*.t, *.thtt, *.thttil file)", required=True)

def main():

    # Fetching args
    args = ArgParser()

    # Creating the output dirrectory for the output file
    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)

    # Reading and parsing the template file
    file      = Thttil.antlr4.FileStream(args.template)
    lexer     = Thttil.ThttilLexer(file)
    stream    = Thttil.antlr4.CommonTokenStream(lexer)
    parser    = Thttil.ThttilParser(stream)
    tree      = parser.program()

    # Passing True here since we are running on windows and we want to write the
    # output to a file (python considers both \r and \n as newlines so we are
    # stripping the \r to have proper newlines in our files)
    Thttil.ThttilTokenRewriter(stream).rewrite(True)

    # Creating the Thttil interpreter and adding
    # the predeclared variables to the interpreter pool
    interpreter = Thttil.ThttilCommandInterpreter()
    for var_name, var_content in args.variables.items():
        interpreter.variable_pool.CreateVar(var_name, var_content)

    # Staring the interpretation
    data = interpreter.visit(tree)

    # Writing the output to the file
    with open(f"{args.output_path}/{args.output_filename}", "wt+") as file:
        file.write(data)

    # Clearing the variable pool and we are done !
    interpreter.variable_pool.Clear()

if __name__ == '__main__':
    main()