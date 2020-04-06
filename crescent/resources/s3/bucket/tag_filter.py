from crescent.core import Model
from .constants import ModelRequiredProperties


class TagFilter(Model):
    def __init__(self):
        super(TagFilter, self).__init__(required_properties=ModelRequiredProperties.TAG_FILTER)

    def Key(self, key: str):
        return self._set_field(self.Key.__name__, key)

    def Value(self, value: str):
        return self._set_field(self.Value.__name__, value)
