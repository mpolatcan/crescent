from zepyhrus.core import Model, Validator
from .constants import AllowedValues


class AccelerateConfiguration(Model):
    @Validator.validate(type=str, allowed_values=AllowedValues.ACCELERATION_STATUS)
    def AccelerationStatus(self, value: str):
        return self._set_field(self.AccelerationStatus.__name__, value)
