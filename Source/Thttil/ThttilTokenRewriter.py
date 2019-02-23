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

from  antlr4      import CommonTokenStream, Token, TokenStreamRewriter
from .ThttilLexer import ThttilLexer

class ThttilTokenRewriter:

    def __init__(self, token_stream: CommonTokenStream):
        self.token_stream = token_stream
        self.replacement_dict: dict = {
            "\\r" : "\r",
            "\\n" : "\n",
            "\\t" : "\t",
            "\\a" : "\a",
            "\\b" : "\b",
            "\\f" : "\f",
            "\\v" : "\v",
            "\\\"": "\"",
            "\\%" : "%",
            "\\\\": "\\"
        }

    # Stripping carriage returns might be useful if you want to write the output of
    # the interpretation to a file. Some APIs considers \n AND \r as newlines.
    # This also depends of your operating system.
    def rewrite(self, strip_file_carriage_return: bool = False):

        current_token = self.token_stream.tokens[0]
        index         = 0
        while (current_token.type != Token.EOF):
            
            if (current_token.type == ThttilLexer.STRING or current_token.type == ThttilLexer.PRINT):
                if (strip_file_carriage_return):
                    current_token.text = current_token.text.replace("\r", "")
                for key, value in self.replacement_dict.items():
                    current_token.text = current_token.text.replace(key, value)

            index += 1
            current_token = self.token_stream.tokens[index]