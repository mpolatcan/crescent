from crescent.core import Model, Validator
from .constants import AllowedValues


class AccelerateConfiguration(Model):
    @Validator.validate(type=str, allowed_values=AllowedValues.ACCELERATION_STATUS)
    def AccelerationStatus(self, acceleration_status: str):
        return self._set_field(self.AccelerationStatus.__name__, acceleration_status)
