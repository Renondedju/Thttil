# -*-coding:utf-8 -*-

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

from typing import Dict, Callable, List, Any
from thttil import Command

class CommandCollection(object):

    def __init__(self):
        self.commands = {getattr(self, method).name: getattr(self, method) for method in dir(type(self)) if isinstance(getattr(self, method), Command)}

    def Command(command = None, *args, **kwargs):
        """ Main decorator used to declare commands """

        if callable(command):
            return Command(command, command.__name__.upper())

        else:
            def wrapper(function):
                return Command(function, *args, **kwargs)
            
            return wrapper

    @staticmethod
    @Command
    def OUT():
        print("OUT !")