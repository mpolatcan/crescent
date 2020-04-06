from crescent.core import Model
from .constants import AllowedValues


class DefaultRetention(Model):
    def __init__(self):
        super(DefaultRetention, self).__init__(
            allowed_values={self.Mode.__name__: AllowedValues.MODE}
        )

    def Days(self, days: int):
        return self._set_field(self.Days.__name__, days)

    def Mode(self, mode: str):
        return self._set_field(self.Mode.__name__, mode)

    def Years(self, years: int):
        return self._set_field(self.Years.__name__, years)
