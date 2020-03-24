from zepyhrus.core import Model, Validator


class ProcessorFeature(Model):
    @Validator.validate(type=str)
    def Name(self, value: str):
        return self._set_field(self.Name.__name__, value)

    @Validator.validate(type=str)
    def Value(self, value: str):
        return self._set_field(self.Value.__name__, value)
