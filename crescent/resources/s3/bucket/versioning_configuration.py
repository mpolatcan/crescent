from crescent.core import Model
from .constants import AllowedValues, ModelRequiredProperties


class VersioningConfiguration(Model):
    def __init__(self):
        super(VersioningConfiguration, self).__init__(
            allowed_values={self.Status.__name__: AllowedValues.VERSIONING_CONFIGURATION_STATUS},
            required_properties=ModelRequiredProperties.VERSIONING_CONFIGURATION
        )

    def Status(self, status: str):
        return self._set_field(self.Status.__name__, status)
