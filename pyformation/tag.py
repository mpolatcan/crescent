class Tag(dict):
    __PROPERTY_KEY = "Key"
    __PROPERTY_VALUE = "Value"

    def __init__(self, key, value):
        self[self.__PROPERTY_KEY] = key
        self[self.__PROPERTY_VALUE] = value
