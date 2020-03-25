from crescent.core import Model, Validator
from .constants import AllowedValues


class FilterRule(Model):
    @Validator.validate(type=str, allowed_values=AllowedValues.NAME)
    def Name(self, value: str):
        return self._set_field(self.Name.__name__, value)

    @Validator.validate(type=str)
    def Value(self, value: str):
        return self._set_field(self.Value.__name__, value)
