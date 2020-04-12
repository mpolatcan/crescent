from .model import Model
from .parameter_types import ParameterType


class Parameter(Model):
    __KEY_TYPE = "Type"

    def __init__(self, id: str, _type: ParameterType):
        super(Parameter, self).__init__(
            pattern={self.ConstraintDescription.__name__: r"[A-Za-z0-9]+"},
            max_length={self.Description.__name__: 4000}
        )
        self._set_field(id, {self.__KEY_TYPE: _type})
        self.__properties = self.__get_field__(id)

    def __set_property(self, property, value):
        self.__properties[property] = value

        return self

    def AllowedPattern(self, allowed_pattern: str):
        return self.__set_property(self.AllowedPattern.__name__, allowed_pattern)

    def AllowedValues(self, *allowed_values: str):
        return self.__set_property(self.AllowedValues.__name__, list(allowed_values))

    def ConstraintDescription(self, value: str):
        return self.__set_property(self.ConstraintDescription.__name__, value)

    def Default(self, default: str):
        return self.__set_property(self.Default.__name__, default)

    def Description(self, description: str):
        return self.__set_property(self.Description.__name__, description)

    def MaxLength(self, max_length: int):
        return self.__set_property(self.MaxLength.__name__, max_length)

    def MaxValue(self, max_value: int):
        return self.__set_property(self.MaxValue.__name__, max_value)

    def MinLength(self, min_length: int):
        return self.__set_property(self.MinLength.__name__, min_length)

    def MinValue(self, min_value: int):
        return self.__set_property(self.MinValue.__name__, min_value)

    def NoEcho(self, no_echo: bool):
        return self.__set_property(self.NoEcho.__name__, no_echo)
