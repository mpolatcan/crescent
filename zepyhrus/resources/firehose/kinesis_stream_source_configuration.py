from zepyhrus.core import Model, Validator


class KinesisStreamSourceConfiguration(Model):
    @Validator.validate(type=str, min_length=1, max_length=512, pattern="arn:.*")
    def KinesisStreamARN(self, value: str):
        return self._set_field(self.KinesisStreamARN.__name__, value)

    @Validator.validate(type=str, min_length=1, max_length=512, pattern="arn:.*")
    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)
