from antlr4 import FileStream

class ThttilFileStream(FileStream):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lines = self.strdata.split('\n')

    def getLine(self, line_index: int):
        return self.lines[min(line_index - 1, len(self.lines))]
