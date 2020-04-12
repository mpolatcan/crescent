from crescent.core import Model
from crescent.functions import AnyFn
from .processor_parameter import ProcessorParameter
from .constants import AllowedValues
from typing import Union


class Processor(Model):
    def __init__(self):
        super(Processor, self).__init__(
            allowed_values={self.Type.__name__: AllowedValues.PROCESSOR_TYPE}
        )

    def Parameters(self, *parameters: ProcessorParameter):
        if self.__get_field__(self.Parameters.__name__) is None:
            return self._set_field(self.Parameters.__name__, list(parameters))
        else:
            self.__get_field__(self.Parameters.__name__).extend(list(parameters))
            return self

    def Type(self, type: Union[str, AnyFn]):
        return self._set_field(self.Type.__name__, type)
