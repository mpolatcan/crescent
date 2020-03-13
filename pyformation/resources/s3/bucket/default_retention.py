from pyformation.core import Model, Validator


class DefaultRetention(Model):
    @Validator.validate(type=int)
    def Days(self, value: int):
        return self._set_field(self.Days.__name__, value)

    @Validator.validate(type=str)
    def Mode(self, value: str):
        return self._set_field(self.Mode.__name__, value)

    @Validator.validate(type=int)
    def Years(self, value: int):
        return self._set_field(self.Years.__name__, value)
