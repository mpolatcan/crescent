from crescent.core import Model
from crescent.functions import AnyFn
from .constants import AllowedValues
from typing import Union


class DefaultRetention(Model):
    def __init__(self):
        super(DefaultRetention, self).__init__(
            allowed_values={self.Mode.__name__: AllowedValues.MODE}
        )

    def Days(self, days: Union[int, AnyFn]):
        return self._set_field(self.Days.__name__, days)

    def Mode(self, mode: Union[str, AnyFn]):
        return self._set_field(self.Mode.__name__, mode)

    def Years(self, years: Union[int, AnyFn]):
        return self._set_field(self.Years.__name__, years)
