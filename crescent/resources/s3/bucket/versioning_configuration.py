from crescent.core import Model, Validator
from .constants import AllowedValues


class VersioningConfiguration(Model):
    @Validator.validate(type=str, allowed_values=AllowedValues.VERSIONING_CONFIGURATION_STATUS)
    def Status(self, status: str):
        return self._set_field(self.Status.__name__, status)
