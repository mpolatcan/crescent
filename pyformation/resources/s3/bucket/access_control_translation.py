from pyformation.core import Model, Validator


class AccessControlTranslation(Model):
    @Validator.validate(type=str)
    def Owner(self, value: str):
        return self._set_field(self.Owner.__name__, value)
