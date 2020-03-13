from pyformation.core import Model, Validator


class VersioningConfiguration(Model):
    @Validator.validate(type=str)
    def Status(self, value: str):
        return self._set_field(self.Status.__name__, value)
