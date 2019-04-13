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

import inspect

from collections import deque
from typing      import Any

class Command(object):

    __slots__ = ("command", "name", "const", "arguments")

    class Argument(object):

        __slots__ = ("name", "optional", "type")

        def __init__(self, name: str, param_type: Any, optional: bool):

            if (param_type == inspect.Parameter.empty):
                raise ValueError("Command parameters must be annotated using the provided thttil.types types.")

            self.name       = name
            self.type       = param_type
            self.optional   = optional

            print(self.name, self.type, self.optional)

    def __init__(self, command: callable, name: str, const: bool = False, *args, **kwargs):

        self.name      = name
        self.const     = const
        self.command   = command
        self.arguments = deque()

        if self.command is not None:
            for name, parameter in inspect.signature(self.command).parameters.items():
                self.arguments.append(Command.Argument(name, parameter.annotation, not parameter.default == inspect.Parameter.empty))

    def __call__(self, *args, **kwargs):
        return self.command(*args, **kwargs)