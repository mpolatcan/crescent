from crescent.core import Model
from crescent.functions import AnyFn
from .constants import AllowedValues
from typing import Union


class ProcessorParameter(Model):
    def __init__(self):
        super(ProcessorParameter, self).__init__(
            min_length={self.ParameterValue.__name__: 1},
            max_length={self.ParameterValue.__name__: 512},
            allowed_values={self.ParameterName.__name__: AllowedValues.PROCESSOR_PARAMETER_NAME}
        )

    def ParameterName(self, parameter_name: Union[str, AnyFn]):
        return self._set_field(self.ParameterName.__name__, parameter_name)

    def ParameterValue(self, parameter_value: Union[str, AnyFn]):
        return self._set_field(self.ParameterValue.__name__, parameter_value)
