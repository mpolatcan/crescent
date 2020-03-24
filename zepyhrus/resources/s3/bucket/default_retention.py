from zepyhrus.core import Model, Validator
from .constants import AllowedValues


class DefaultRetention(Model):
    @Validator.validate(type=int)
    def Days(self, value: int):
        return self._set_field(self.Days.__name__, value)

    @Validator.validate(type=str, allowed_values=AllowedValues.MODE)
    def Mode(self, value: str):
        return self._set_field(self.Mode.__name__, value)

    @Validator.validate(type=int)
    def Years(self, value: int):
        return self._set_field(self.Years.__name__, value)
