from enum import Enum

class ThttilCommandReturnType(Enum):
    """ Tells the interpreter what type of data is returned by a command
        This ultimately allows the interpreter to output data to
        the output stream when needed
    """

    DATA        = 0
    STREAM_DATA = 1