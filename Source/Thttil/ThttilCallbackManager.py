from typing import Dict, Callable

class ThttilCallbackManager(object):

    def __init__(self):
        self.callbacks: Dict[str, Callable[['ThttilCommandInterpreter'], None]] = {}

    def registerCallback(self, callback: Callable[['ThttilCommandInterpreter'], None], callback_name: str) -> None:
        """ Registers or updates a callback
        """
        
        self.callbacks[callback_name] = callback
        return

    def invoke(self, callback_name: str, interpreter_instance) -> None:
        """ Tries to invoke a callback. Sends a warning if the callback isn't found
        """

        # callback not found
        if not callback_name in self.callbacks:
            return

        # invoking the callback
        if callable(self.callbacks[callback_name]):
            self.callbacks[callback_name](interpreter_instance)

        return

    def unregisterCallback(self, callback_name: str) -> bool:
        """ Unregisters a callback. Returns True if the operation succeeded
        """

        if not callback_name in self.callbacks:
            return False

        del self.callbacks[callback_name]
        return True
    