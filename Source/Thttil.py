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

        self.variables  : dict = self._parseVariables(self.args.variables)
        self.outputs    : dict = self._parseOutputs  (self.args.outputs)
        # self.output_path, self.output_filename = os.path.split(self.args.output)
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
            help="Variables to declare before the interpretation (format must be: var_name=value)")

        self.required_args.add_argument('-t', '--template', type=str, metavar='template',
            help="Template file to interpret (*.t, *.thtt, *.thttil file)", required=True)

# This is a callback that prints all the variables of the interpreter pool.
def inspect(interpreter: Thttil.ThttilCommandInterpreter) -> None:
    print("Inspecting the current variables in the interpreter variable pool at", hex(id(interpreter.variable_pool)))

    for var in interpreter.variable_pool.getVarList():
        print("\t-", var, ":", getattr(interpreter.variable_pool, var))

def main():

    # Fetching args
    args = ArgParser()

    # Parsing the template file
    tree_parser = Thttil.ThttilTreeParser(args.template)

    # Passing True here since we are running on windows and we want to write the
    # output to a file (python considers both \r and \n as newlines so we are
    # stripping the \r to have proper newlines in our files)
    Thttil.ThttilTokenRewriter(tree_parser.token_stream).rewrite(True)

    # Creating the Thttil interpreter and adding
    # the predeclared variables to the interpreter pool
    interpreter = Thttil.ThttilCommandInterpreter()
    for var_name, var_content in args.variables.items():
        interpreter.variable_pool.createVar(var_name, var_content)

    interpreter.callback_manager.registerCallback(inspect, inspect.__name__)

    # Staring the interpretation
    interpreter.interpret(tree_parser.tree, tree_parser.file)

    # Iterating over every output stream
    for stream_name, file_name in args.outputs.items():
        output_path, output_filename = os.path.split(file_name)

        # Creating the output dirrectory for the output file
        if not os.path.exists(f"./{output_path}"):
            os.makedirs(f"./{output_path}")

        # Writing data to the file
        with open(file_name, "wt+") as file:
            file.write(interpreter.stream_buffer.get(stream_name))

    # Clearing the variable pool and we are done !
    interpreter.variable_pool.clear()

if __name__ == '__main__':
    main()