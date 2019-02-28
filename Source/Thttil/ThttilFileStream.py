from antlr4 import FileStream
from typing import Tuple

class ThttilFileStream(FileStream):

    class Line(object):

        def __init__(self, start, end):
            self.start = start
            self.end   = end

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lines = []

        index = 0
        start = 0
        end   = len(self.strdata)
        while index != -1:

            index = self.strdata.find('\n', start, end)
            if index == -1:
                continue

            self.lines.append(ThttilFileStream.Line(start, index))
            start = index + 1

    def getLineWithColumn(self, column: int) -> Tuple[str, int, int]:
        for index, line in enumerate(self.lines):
            if column >= line.start and column <= line.end:
                return self.strdata[line.start:line.end], index, line.start
        return "", -1, 0

    def getLine(self, line_index: int):
        line = self.lines[line_index]
        return self.strdata[line.start:line.end]
