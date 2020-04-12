from crescent.core import Model
from crescent.functions import AnyFn
from .constants import AllowedValues, ModelRequiredProperties
from typing import Union


class VersioningConfiguration(Model):
    def __init__(self):
        super(VersioningConfiguration, self).__init__(
            allowed_values={self.Status.__name__: AllowedValues.VERSIONING_CONFIGURATION_STATUS},
            required_properties=ModelRequiredProperties.VERSIONING_CONFIGURATION
        )

    def Status(self, status: Union[str, AnyFn]):
        return self._set_field(self.Status.__name__, status)
