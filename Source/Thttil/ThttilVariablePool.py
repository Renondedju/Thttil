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

from typing import Any, Union, List

class ThttilVariablePool:
    """ A varable pool is uses python reflection to maintain itself.
        This allow the creation of complex structures on python side and still access
        them using Thill.

        Since Thill uses only strings as variable type, if a python side variable
        isn't a string, it will be converted using the python str() cast.
        
        Python arrays of strings are supported.     
    """

    def __init__(self):
        self.__register = set()

    def __getattr(self, instance: 'ThttilVariablePool', attribute: str, default: Any = None) -> Any:
        sub_attributes   = attribute.split('.')
        current_instance = instance
        for sub_attribute in sub_attributes[:-1]:
            if not hasattr(current_instance, sub_attribute):
                return default
            current_instance = getattr(current_instance, sub_attribute)

        return getattr(current_instance, sub_attributes[-1], default)

    def __setattr(self, instance, attribute: str, value: Any) -> None:
        sub_attributes   = attribute.split('.')
        current_instance = instance
        for sub_attribute in sub_attributes[:-1]:
            if not hasattr(current_instance, sub_attribute):
                return
            current_instance = getattr(current_instance, sub_attribute)

        setattr(current_instance, sub_attributes[-1], value)
        return

    def __hasattr(self, instance, attribute: str) -> bool:
        sub_attributes   = attribute.split('.')
        current_instance = instance
        for sub_attribute in sub_attributes[:-1]:
            if not hasattr(current_instance, sub_attribute):
                return False
            current_instance = getattr(current_instance, sub_attribute)

        return hasattr(current_instance, sub_attributes[-1])

    def clear(self):
        for var in list(self.__register):
            self.deleteVar(var)

    def getVarList(self) -> set:
        return self.__register

    def setVar(self, name: str, value: Any):
        if (not self.__hasattr(self, name)):
            print("Thttil runtime error: cannot set a variable that doesn't exists.", name)
            return

        self.__setattr(self, name, value)
        return

    def getVar(self, name: str) -> Union[str, List[str]]:
        if (not self.__hasattr(self, name)):
            print("Thttil runtime error: cannot get a variable that doesn't exists:", name)
            return ""

        return self.__getattr(self, name)

    def createVar(self, name: str, init_value: Any = None):
        if (self.__hasattr(self, name)):
            print("Thttil runtime error: cannot create a variable already defined.", name)
            return
        
        self.__register.add(name)
        setattr(self, name, init_value)
        return

    def deleteVar(self, name: str):
        if (not self.__hasattr(self, name)):
            print("Thttil runtime error: cannot delete a variable that doesn't exists.", name)
            return

        self.__register.remove(name)
        delattr(self, name)
        return