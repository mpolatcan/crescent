from crescent.core import Model
from crescent.functions import AnyFn
from .constants import AllowedValues, ModelRequiredProperties
from typing import Union


class AccelerateConfiguration(Model):
    def __init__(self):
        super(AccelerateConfiguration, self).__init__(
            allowed_values={self.AccelerationStatus.__name__: AllowedValues.ACCELERATION_STATUS},
            required_properties=ModelRequiredProperties.ACCELERATE_CONFIGURATION
        )

    def AccelerationStatus(self, acceleration_status: Union[str, AnyFn]):
        return self._set_field(self.AccelerationStatus.__name__, acceleration_status)
