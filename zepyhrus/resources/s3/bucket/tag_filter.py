from zepyhrus.core import Model, Validator


class TagFilter(Model):
    @Validator.validate(type=str)
    def Key(self, value: str):
        return self._set_field(self.Key.__name__, value)

    @Validator.validate(type=str)
    def Value(self, value: str):
        return self._set_field(self.Value.__name__, value)
