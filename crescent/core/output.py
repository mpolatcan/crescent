from .model import Model

# TODO Export field will be added


class Output(Model):
    def __init__(self, id: str):
        super(Output, self).__init__(
            required_properties=[self.Value.__name__]
        )
        self.__id = id
        self._set_field(self.__id, {})

    def __set_property(self, property, value):
        self.__get_field__(self.__id)[property] = value
        return self

    def Description(self, description: str):
        return self.__set_property(self.Description.__name__, description)

    def Value(self, value: str):
        return self.__set_property(self.Value.__name__, value)
