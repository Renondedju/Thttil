import antlr4
from .ThttilLexer        import ThttilLexer
from .ThttilParser       import ThttilParser
from .ThttilFileStream   import ThttilFileStream
from .ThttilErrorHandler import ThttilErrorHandler

class ThttilTreeParser:

    def __init__(self, template_file: str):
        self.tree          = None 
        self.file          = None
        self.lexer         = None
        self.parser        = None
        self.token_stream  = None
        self.error_handler = ThttilErrorHandler(None)

        self.ParseTemplate(template_file)

    def ParseTemplate(self, template_file: str):
        
        # Reading the file
        self.file = ThttilFileStream(template_file)
        
        # Updating the error handler to output coherent errors
        self.error_handler.file_stream = self.file
        
        # Lexing the file
        self.lexer = ThttilLexer(self.file)
        self.lexer.removeErrorListeners()
        self.lexer.addErrorListener(self.error_handler)
        self.token_stream = antlr4.CommonTokenStream(self.lexer)

        # Parsing the file
        self.parser = ThttilParser(self.token_stream)
        self.parser.removeErrorListeners()
        self.parser.addErrorListener(self.error_handler)
        
        # Generating the template tree
        self.tree = self.parser.program()

        # If errors has been detected during parsing, stoping here
        if (self.error_handler.handleHerrors()):
            exit(1)