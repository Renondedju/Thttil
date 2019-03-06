
from .ThttilFileStream import ThttilFileStream
from enum              import Enum

class ColorPrinter:

    ERROR     = '\033[33m'
    RESET     = '\033[0m'
    NORMAL    = ''
    WARNING   = '\033[33m'
    SUCCESS   = '\033[32m'
    UNDERLINE = '\033[4m'

    def __init__(self, use_colors: bool = True):
        self.use_colors = use_colors

        if use_colors:
            # Checking if we are running on a windows machine.
            import os
            if (os.name == 'nt'):
                # If this is the case, we need to tell windows to use colors...
                # I really hate windows, you shouldn't have to do this :/
                os.system('color')

    def print(self, content: str, color: str = NORMAL, *args, **kwargs):
        if (self.use_colors):
            print(color + content + ColorPrinter.RESET, *args, **kwargs)
            return
        print(content, *args, **kwargs)
        return

class ThttilRuntimeErrorHandler:

    def __init__(self, enable_colors:bool = True):
        self.current_interpreted_template: ThttilFileStream = None
        self.printer: ColorPrinter = ColorPrinter(enable_colors)

    def setCurrentInterpretedTemplate(self, template: ThttilFileStream):
        self.current_interpreted_template: ThttilFileStream = template

    def _printErrorHeader(self):
        self.printer.print("Thttil runtime error: ", ColorPrinter.ERROR + ColorPrinter.UNDERLINE, end="")

    def _printWarningHeader(self):
        self.printer.print("Thttil runtime warning: ", ColorPrinter.WARNING + ColorPrinter.UNDERLINE, end="")

    def _printOffendingTokenReport(self, offending_token, max_report_length: int = 300):
        content, line_index, content_start = self.current_interpreted_template.getLineWithColumn(offending_token.start.start)
        start = max(0           , offending_token.start.start - content_start - int(max_report_length/2))
        end   = min(len(content), offending_token.stop.stop   - content_start + int(max_report_length/2))

        print(f"in {self.current_interpreted_template.fileName}:{line_index + 1}:{offending_token.start.start - content_start}")
        print(f"{content[start:end + 1]}\n{' '*(offending_token.start.start - content_start)}^{'~'*(min(offending_token.stop.stop - offending_token.start.start, len(content)))}")

    def undeclaredStreamWarning(self, offending_token, stream_name):
        """ Usage of an undeclared stream in a stream redirection
        """

        self._printWarningHeader()
        self.printer.print(f"Usage of an undeclared stream (\"{stream_name}\") in a stream redirection", ColorPrinter.WARNING)
        self._printOffendingTokenReport(offending_token)

    def undefinedVariableError(self, var_name):
        """ Trigerred when an undefined variable is required
            this error is recoverable.
        """

        self._printErrorHeader()
        self.printer.print(f"Undefined variable named $\"{var_name}\", did you forgot to add it to the interpreter variable pool ?", ColorPrinter.ERROR)

    def notEnoughArgumentsError(self, offending_token, min_args, got):
        """ Trigerred when there is not enough argument in a command call
            this error is unrecoverable.
        """

        self._printErrorHeader()
        self.printer.print(f"Not enough arguments in command call. Minimum is {min_args}, got {got}.", ColorPrinter.ERROR)
        self._printOffendingTokenReport(offending_token)
        
        exit(1)

    def instructionBlockRequiredError(self, offending_token):
        """ Trigerred when there an instruction block is missing after a command call
            this error is unrecoverable.
        """

        self._printErrorHeader()
        self.printer.print("Instruction block required after command call.", ColorPrinter.ERROR)
        self._printOffendingTokenReport(offending_token)
        
        exit(1)

    def tooMuchArgumentsError(self, offending_token, max_args, got):
        """ Trigerred when there is too much argument in a command call
            this error is unrecoverable.
        """

        self._printErrorHeader()
        self.printer.print(f"Too much arguments in command call. Maximum is {max_args}, got {got}.", ColorPrinter.ERROR)
        self._printOffendingTokenReport(offending_token)
        
        exit(1)

    def incompatibleArgumentTypeError(self, offending_token):
        """ Trigerred when the passed argument isn't compatible with the command requirements
            this error is unrecoverable.
        """
        
        self._printErrorHeader()
        self.printer.print("Incompatible argument type.", ColorPrinter.ERROR)
        self._printOffendingTokenReport(offending_token)

        exit(1)