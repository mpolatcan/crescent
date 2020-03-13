from .model import Model


class Parameter(Model):
    __KEY_TYPE = "Type"

    def __init__(self, id, data_type):
        super(Parameter, self).__init__()
        self[id] = {
            self.__KEY_TYPE: data_type
        }
        self.__property = self[id]

    def __set_property(self, property, value):
        self.__property[property] = value

        return self

    def AllowedPattern(self, value: str):
        return self.__set_property(self.AllowedPattern.__name__, value)

    def AllowedValues(self, *values: str):
        return self.__set_property(self.AllowedPattern.__name__, list(values))

    def ConstraintDescription(self, value: str):
        return self.__set_property(self.ConstraintDescription.__name__, value)

    def Default(self, value: str):
        return self.__set_property(self.Default.__name__, value)

    def Description(self, value: str):
        return self.__set_property(self.Description.__name__, value)

    def MaxLength(self, value: int):
        return self.__set_property(self.MaxLength.__name__, value)

    def MaxValue(self, value: int):
        return self.__set_property(self.MaxValue.__name__, value)

    def MinLength(self, value: int):
        return self.__set_property(self.MinLength.__name__, value)

    def MinValue(self, value: int):
        return self.__set_property(self.MinValue.__name__, value)

    def NoEcho(self, value: bool):
        return self.__set_property(self.NoEcho.__name__, value)
