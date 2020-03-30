from crescent.core import Model, Validator


class ProcessorFeature(Model):
    @Validator.validate(type=str)
    def Name(self, name: str):
        return self._set_field(self.Name.__name__, name)

    @Validator.validate(type=str)
    def Value(self, value: str):
        return self._set_field(self.Value.__name__, value)
