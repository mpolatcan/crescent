from crescent.core import Model, Validator
from .constants import AllowedValues


class DefaultRetention(Model):
    @Validator.validate(type=int)
    def Days(self, days: int):
        return self._set_field(self.Days.__name__, days)

    @Validator.validate(type=str, allowed_values=AllowedValues.MODE)
    def Mode(self, mode: str):
        return self._set_field(self.Mode.__name__, mode)

    @Validator.validate(type=int)
    def Years(self, years: int):
        return self._set_field(self.Years.__name__, years)
