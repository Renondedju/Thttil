from typing                     import List
from .ThttilFileStream          import ThttilFileStream
from antlr4.error.ErrorListener import ErrorListener

class ThttilErrorHandler(ErrorListener):

    class Error(object):

        def __init__(self, line: int, start: int, end: int, offending_symbol, error_str: str):
            self.end               = end
            self.line              = line
            self.start             = start
            self.offending_symbols = [offending_symbol]
            self.error_str         = error_str

        def toString(self, handler_instance) -> str:
            error_line, start, end = handler_instance.getErrorLine(self.line - 1, self.start)
            error_output =  f"Thttil parsing error: {self.error_str} on line {self.line}:{self.start}\n"
            error_output += f"{error_line}\n{' '*(self.start - start)}^{'~'*min(self.end - self.start, end - self.start)}"
            return error_output

    def __init__(self, file_stream: ThttilFileStream):
        self.file_stream = file_stream
        self.errors: List[ThttilErrorHandler.Error] = []

    def handleHerrors(self) -> bool:
        for error in self.errors:
            print(error.toString(self))
        hasErrors = len(self.errors) > 0
        self.errors = []
        return hasErrors

    def getErrorLine(self, line, column, max_line_length: int = 300) -> str:
        line  = self.file_stream.getLine(line)
        start = max(0, int(column - max_line_length/2))
        end   = max(len(line), int(column + max_line_length/2))
        return line[start:end], start, end

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        for error in self.errors:
            if error.line == line and error.end + 1 == column:
                error.end = column
                error.offending_symbols.append(offendingSymbol)
                return

        self.errors.append(ThttilErrorHandler.Error(line, column, column, offendingSymbol, "syntax error"))
        return