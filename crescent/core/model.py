class Model:
    def __init__(self):
        self.__data = {}

    def _set_field(self, key, value):
        self.__data[key] = value

        return self

    def _get_field(self, key, default=None):
        return self.__data.get(key, default)

    def _update_model(self, value):
        self.__data.update(value)

        return self

    def __to_dict__(self):
        return self.__data
