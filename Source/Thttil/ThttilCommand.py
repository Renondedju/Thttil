from  typing                    import Any
from .ThttilCommandReturnType   import ThttilCommandReturnType

import inspect

class ThttilCommand(object):

    class ThttilCommandArgument(object):

        def __init__(self, name: str, vartype: Any, default: Any):
            self.name     : str  = name
            self.type     : Any  = vartype
            self.default  : Any  = default
            self.optional : bool = default != inspect._empty

    def __init__(self, command,
                 return_type:ThttilCommandReturnType = ThttilCommandReturnType.DATA,
                 pass_interpreter_instance: bool     = False,
                 require_instruction_block: bool     = False,
                 *args, **kwargs):

        self.command                       = command
        self.max_args                      = 0
        self.arguments                     = []
        self.return_type                   = return_type
        self.min_required_args             = 0
        self.requires_interpreter_instance = pass_interpreter_instance
        self.require_instruction_block     = require_instruction_block

        for name, param in inspect.signature(command).parameters.items():
            argument = ThttilCommand.ThttilCommandArgument(name, self.command.__annotations__.get(name, None), param.default)
            self.min_required_args += int(not argument.optional)
            self.arguments.append(argument)

        if (self.requires_interpreter_instance):
            self.arguments = self.arguments[1:]
        
        if (self.require_instruction_block):
            self.arguments = self.arguments[:-1]

        self.min_required_args -= int(pass_interpreter_instance) + int(require_instruction_block)
        self.max_args           = len(self.arguments)

    def __call__(self, *args, **kwargs):
        return self.command(*args, **kwargs)