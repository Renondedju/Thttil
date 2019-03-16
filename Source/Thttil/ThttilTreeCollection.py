class ThttilTreeCollection:

    def __init__(self):
        self.__collection: dict = {}

    def add(name, tree):
        if not self.exists(name):
            self.__collection[name] = tree
        return

    def remove(name):
        if self.exists(name):
            del self.__collection[name]
        return

    def get(self, name):
        return self.__collection.get(name, None)

    def exists(self, name) -> bool:
        return name in self.__collection