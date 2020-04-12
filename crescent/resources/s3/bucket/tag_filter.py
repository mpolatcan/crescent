from crescent.core import Model
from crescent.functions import AnyFn
from .constants import ModelRequiredProperties
from typing import Union


class TagFilter(Model):
    def __init__(self):
        super(TagFilter, self).__init__(required_properties=ModelRequiredProperties.TAG_FILTER)

    def Key(self, key: Union[str, AnyFn]):
        return self._set_field(self.Key.__name__, key)

    def Value(self, value: Union[str, AnyFn]):
        return self._set_field(self.Value.__name__, value)
