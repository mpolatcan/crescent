from crescent.core import Model
from crescent.functions import AnyFn
from typing import Union


class ProcessorFeature(Model):
    def Name(self, name: Union[str, AnyFn]):
        return self._set_field(self.Name.__name__, name)

    def Value(self, value: Union[str, AnyFn]):
        return self._set_field(self.Value.__name__, value)
