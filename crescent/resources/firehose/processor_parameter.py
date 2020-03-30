from crescent.core import Model, Validator
from .constants import AllowedValues


class ProcessorParameter(Model):
    @Validator.validate(type=str, allowed_values=AllowedValues.PROCESSOR_PARAMETER_NAME)
    def ParameterName(self, parameter_name: str):
        return self._set_field(self.ParameterName.__name__, parameter_name)

    @Validator.validate(type=str, min_length=1, max_length=512)
    def ParameterValue(self, parameter_value: str):
        return self._set_field(self.ParameterValue.__name__, parameter_value)
