from pyformation.core import Model, Validator


class AccelerateConfiguration(Model):
    @Validator.validate(type=str)
    def AccelerationStatus(self, value: str):
        return self._set_field(self.AccelerationStatus.__name__, value)
