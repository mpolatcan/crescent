from .validator import Validator
from .model import Model
from .type import Type


class Parameter(Model):
    __KEY_TYPE = "Type"

    def __init__(self, id: str, _type: Type):
        super(Parameter, self).__init__()
        self._data[id] = {self.__KEY_TYPE: _type}
        self.__properties = self._data[id]

    def __set_property(self, property, value):
        self.__properties[property] = value

        return self

    @Validator.validate(type=str)
    def AllowedPattern(self, value: str):
        return self.__set_property(self.AllowedPattern.__name__, value)

    @Validator.validate(type=str)
    def AllowedValues(self, *values: str):
        return self.__set_property(self.AllowedPattern.__name__, list(values))

    @Validator.validate(type=str, pattern=r"[A-Za-z0-9]+")
    def ConstraintDescription(self, value: str):
        return self.__set_property(self.ConstraintDescription.__name__, value)

    @Validator.validate(type=str)
    def Default(self, value: str):
        return self.__set_property(self.Default.__name__, value)

    @Validator.validate(type=str, max_length=4000)
    def Description(self, value: str):
        return self.__set_property(self.Description.__name__, value)

    @Validator.validate(type=int)
    def MaxLength(self, value: int):
        return self.__set_property(self.MaxLength.__name__, value)

    @Validator.validate(type=int)
    def MaxValue(self, value: int):
        return self.__set_property(self.MaxValue.__name__, value)

    @Validator.validate(type=int)
    def MinLength(self, value: int):
        return self.__set_property(self.MinLength.__name__, value)

    @Validator.validate(type=int)
    def MinValue(self, value: int):
        return self.__set_property(self.MinValue.__name__, value)

    @Validator.validate(type=bool)
    def NoEcho(self, value: bool):
        return self.__set_property(self.NoEcho.__name__, value)
