from crescent.core import Model
from crescent.functions import AnyFn
from .constants import AllowedValues, ModelRequiredProperties
from typing import Union


class FilterRule(Model):
    def __init__(self):
        super(FilterRule, self).__init__(
            allowed_values={self.Name.__name__: AllowedValues.NAME},
            required_properties=ModelRequiredProperties.FILTER_RULE
        )

    def Name(self, name: Union[str, AnyFn]):
        return self._set_field(self.Name.__name__, name)

    def Value(self, value: Union[str, AnyFn]):
        return self._set_field(self.Value.__name__, value)
