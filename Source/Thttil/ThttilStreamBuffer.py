from typing import Dict, List

class ThttilStreamBuffer:
    """ Stores streams
    """

    def __init__(self):
        self.__streams       : Dict[str, str] = {"default": ""}
        self.__current_stream: str            = "default"

    def select(self, stream_name: str = "default") -> bool:
        """ Selects the default stream to write to.
            Returns False if the operation failed
            (the selected stream will remain unchanged in this case)
        """
        if stream_name in self.__streams:
            self.__current_stream = stream_name
            return True
        return False

    def create(self, stream_name: str) -> bool:
        """ Creates a stream, returns True if the operation succeeded
        """

        if stream_name in self.__streams:
            return False

        self.__streams[stream_name] = ""
        if (stream_name == "debug"):
            print("Thttil runtime warning: Debug stream enabled.")

        return True

    def append(self, content: str, stream_name: str = None) -> None:
        """ Appends content to a stream, is stream_name isn't specified, the
            last selected stream will be used
        """
        if stream_name == None:
            stream_name = self.__current_stream

        if stream_name == "debug":
            print(content)

        if stream_name in self.__streams:
            self.__streams[stream_name] += content
        else:
            self.__streams[stream_name]  = content

        return

    def get(self, stream_name: str) -> str:
        """ Returns the content of a stream
        """
        return self.__streams.get(stream_name, "")

    def names(self) -> List[str]:
        return self.__streams.keys()

    def clear(self) -> None:
        """ Clears all streams and resets the stream buffer
        """
        self.__streams       : Dict[str, str] = {"default": ""}
        self.__current_stream: str            = "default"
