
from .ThttilFileStream import ThttilFileStream

class ThttilRuntimeErrorHandler:

    def __init__(self):
        self.current_interpreted_template: ThttilFileStream = None

    def setCurrentInterpretedTemplate(self, template: ThttilFileStream):
        self.current_interpreted_template: ThttilFileStream = template

    def _printOffendingTokenReport(self, offending_token, max_report_length: int = 300):
        content, line_index, content_start = self.current_interpreted_template.getLineWithColumn(offending_token.start.start)
        start = max(0           , offending_token.start.start - content_start - int(max_report_length/2))
        end   = min(len(content), offending_token.stop.stop   - content_start + int(max_report_length/2))

        print(f"{self.current_interpreted_template.fileName}:{line_index + 1}:{offending_token.start.start - content_start}")
        print(f"{content[start:end + 1]}\n{' '*(offending_token.start.start - content_start)}^{'~'*(min(offending_token.stop.stop - offending_token.start.start, len(content)))}")

    def undeclaredStreamWarning(self, offending_token, stream_name):
        """ Usage of an undeclared stream in a stream redirection
        """
        print(f"Thttil runtime warning: Usage of an undeclared stream (\"{stream_name}\") in a stream redirection")
        self._printOffendingTokenReport(offending_token)

    def undefinedVariableError(self, var_name):
        """ Trigerred when an undefined variable is required
            this error is recoverable.
        """
        print(f"Thttil runtime error: Undefined variable named $\"{var_name}\", did you forgot to add it to the interpreter variable pool ?")

    def notEnoughArgumentsError(self, offending_token, min_args, got):
        """ Trigerred when there is not enough argument in a command call
            this error is unrecoverable.
        """

        print(f"Thttil runtime error: Not enough arguments in command call. Minimum is {min_args}, got {got}.", end="")
        self._printOffendingTokenReport(offending_token)
        exit(1)

    def instructionBlockRequiredError(self, offending_token):
        """ Trigerred when there an instruction block is missing after a command call
            this error is unrecoverable.
        """

        print("Thttil runtime error: Instruction block required after command call.", end="")
        self._printOffendingTokenReport(offending_token)
        exit(1)

    def tooMuchArgumentsError(self, offending_token, max_args, got):
        """ Trigerred when there is too much argument in a command call
            this error is unrecoverable.
        """

        print(f"Thttil runtime error: Too much arguments in command call. Maximum is {max_args}, got {got}.", end="")
        self._printOffendingTokenReport(offending_token)
        exit(1)

    def incompatibleArgumentTypeError(self, offending_token):
        """ Trigerred when the passed argument isn't compatible with the command requirements
            this error is unrecoverable.
        """
        
        print("Thttil runtime error: Incompatible argument type.", end="")
        self._printOffendingTokenReport(offending_token)
        exit(1)