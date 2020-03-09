from resources.shared import BaseModel


class KinesisStreamSourceConfiguration(BaseModel):
    __PROPERTY_KINESIS_STREAM_ARN = "KinesisStreamARN"
    __PROPERTY_ROLE_ARN = "RoleARN"

    def kinesis_stream_arn(self, value: str):
        return self._add_field(self.__PROPERTY_KINESIS_STREAM_ARN, value)

    def role_arn(self, value: str):
        return self._add_field(self.__PROPERTY_ROLE_ARN, value)
