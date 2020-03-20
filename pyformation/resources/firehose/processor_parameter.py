from pyformation.core import Model, Validator
from .constants import AllowedValues


class ProcessorParameter(Model):
    @Validator.validate(type=str, allowed_values=AllowedValues.PROCESSOR_PARAMETER_NAME)
    def ParameterName(self, value: str):
        return self._set_field(self.ParameterName.__name__, value)

    @Validator.validate(type=str, min_length=1, max_length=512)
    def ParameterValue(self, value: str):
        return self._set_field(self.ParameterValue.__name__, value)
