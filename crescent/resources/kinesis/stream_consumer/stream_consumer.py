from crescent.core import Resource
from crescent.resources.kinesis import StreamArn
from .constants import ResourceRequiredProperties


class StreamConsumer(Resource):
    __TYPE = "AWS::Kinesis::StreamConsumer"

    def __init__(self, id: str):
        super(StreamConsumer, self).__init__(
            id=id,
            type=self.__TYPE,
            min_length={self.ConsumerName.__name__: 1,
                        self.StreamARN.__name__: 1},
            max_length={self.ConsumerName.__name__: 128,
                        self.StreamARN.__name__: 2048},
            pattern={self.ConsumerName.__name__: r"[a-zA-Z0-9_.-]+",
                     self.StreamARN.__name__: r"arn:aws.*:kinesis:.*:\d{12}:stream/.+"},
            required_properties=ResourceRequiredProperties.STREAM_CONSUMER
        )

    def ConsumerName(self, consumer_name: str):
        return self._set_property(self.ConsumerName.__name__, consumer_name)

    def StreamARN(self, stream_arn: StreamArn):
        return self._set_property(self.StreamARN.__name__, stream_arn)

