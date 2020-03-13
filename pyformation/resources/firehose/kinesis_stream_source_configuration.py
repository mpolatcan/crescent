from pyformation.core import Model, Validator


class KinesisStreamSourceConfiguration(Model):
    @Validator.validate(type=str)
    def KinesisStreamARN(self, value: str):
        return self._set_field(self.KinesisStreamARN.__name__, value)

    @Validator.validate(type=str)
    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)
