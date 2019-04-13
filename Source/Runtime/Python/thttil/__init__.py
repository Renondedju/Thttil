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

"""
*** Thttil Python runtime library ***

For further information, please take a look at https://github.com/Renondedju/Thttil

Documentation: https://github.com/Renondedju/Thttil/wiki
"""

# Meta data
__repository__  = "https://github.com/Renondedju/Thttil"
__copyright__   = "Copyright (c) 2019 Renondedju"
__authors__     = ["Renondedju"]
__version__     = "0.3.0-pre"
__licence__     = "MIT"

__slots__ = ("Bytes", "StreamCollection", "SymbolKeyword", "Token",
            "Stream", "Parser", "Lexer", "SymbolInstructionBlock",
            "SymbolVariable", "SymbolArgument", "SymbolProgram",
            "SymbolString", "SymbolStream", "SymbolToken", "TokenDefinition",
            "CommandCollection", "Command", "Interpreter")

# Native haxe symbols
from .ThttilGenerated import haxe_io_Bytes as Bytes

# Submodules
import thttil.types
import thttil.symbols

# Python implementation
from .Command           import Command
from .CommandCollection import CommandCollection

# Generated classes
from .ThttilGenerated import thttil_StreamCollection as StreamCollection
from .ThttilGenerated import thttil_Stream           as Stream
from .ThttilGenerated import thttil_Parser           as Parser
from .ThttilGenerated import thttil_Token            as Token
from .ThttilGenerated import thttil_Lexer            as Lexer