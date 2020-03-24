from pyformation.core import Model, Validator
from .constants import AllowedValues


class VersioningConfiguration(Model):
    @Validator.validate(type=str, status=AllowedValues.VERSIONING_CONFIGURATION_STATUS)
    def Status(self, value: str):
        return self._set_field(self.Status.__name__, value)
