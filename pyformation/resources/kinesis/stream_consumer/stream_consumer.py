from pyformation.resources.shared import BaseCloudFormationResourceModel


class StreamConsumer(BaseCloudFormationResourceModel):
    __TYPE = "AWS::Kinesis::StreamConsumer"
    __PROPERTY_CONSUMER_NAME = "ConsumerName"
    __PROPERTY_STREAM_ARN = "StreamARN"

    def __init__(self):
        super(StreamConsumer, self).__init__(type=self.__TYPE)

    def consumer_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_CONSUMER_NAME, value)

    def stream_arn(self, value: str):
        return self._add_property_field(self.__PROPERTY_STREAM_ARN, value)

