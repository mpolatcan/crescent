class Tag:
    __PROPERTY_KEY = "Key"
    __PROPERTY_VALUE = "Value"

    def __init__(self, key, value):
        self.__tag_def = {
            self.__PROPERTY_KEY: key,
            self.__PROPERTY_VALUE: value
        }

    def create(self):
        return self.__tag_def
