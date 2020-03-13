from pyformation.core import Model, Validator


class ProcessorParameter(Model):
    @Validator.validate(type=str)
    def ParameterName(self, value: str):
        return self._set_field(self.ParameterName.__name__, value)

    @Validator.validate(type=str)
    def ParameterValue(self, value: str):
        return self._set_field(self.ParameterValue.__name__, value)
