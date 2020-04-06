from crescent.core import Model
from .constants import AllowedValues, ModelRequiredProperties


class FilterRule(Model):
    def __init__(self):
        super(FilterRule, self).__init__(
            allowed_values={self.Name.__name__: AllowedValues.NAME},
            required_properties=ModelRequiredProperties.FILTER_RULE
        )

    def Name(self, name: str):
        return self._set_field(self.Name.__name__, name)

    def Value(self, value: str):
        return self._set_field(self.Value.__name__, value)
