from crescent.core import Model, Validator


class KinesisStreamSourceConfiguration(Model):
    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"arn:.*")
    def KinesisStreamARN(self, kinesis_stream_arn: str):
        return self._set_field(self.KinesisStreamARN.__name__, kinesis_stream_arn)

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"arn:.*")
    def RoleARN(self, role_arn: str):
        return self._set_field(self.RoleARN.__name__, role_arn)
