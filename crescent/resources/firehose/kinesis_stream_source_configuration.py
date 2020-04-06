from crescent.core import Model
from .constants import ModelRequiredProperties


class KinesisStreamSourceConfiguration(Model):
    def __init__(self):
        super(KinesisStreamSourceConfiguration, self).__init__(
            min_length={self.KinesisStreamARN.__name__: 1,
                        self.RoleARN.__name__: 1},
            max_length={self.KinesisStreamARN.__name__: 512,
                        self.RoleARN.__name__: 512},
            pattern={self.KinesisStreamARN.__name__: r"arn:.*",
                     self.RoleARN.__name__: r"arn:.*"},
            required_properties=ModelRequiredProperties.KINESIS_STREAM_SOURCE_CONFIGURATION
        )

    def KinesisStreamARN(self, kinesis_stream_arn: str):
        return self._set_field(self.KinesisStreamARN.__name__, kinesis_stream_arn)

    def RoleARN(self, role_arn: str):
        return self._set_field(self.RoleARN.__name__, role_arn)
