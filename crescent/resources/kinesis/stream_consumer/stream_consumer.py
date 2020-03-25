from crescent.core import Resource, Validator


class StreamConsumer(Resource):
    __TYPE = "AWS::Kinesis::StreamConsumer"

    def __init__(self, id: str):
        super(StreamConsumer, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str, min_length=1, max_length=128, pattern=r"[a-zA-Z0-9_.-]+")
    def ConsumerName(self, value: str):
        return self._set_property(self.ConsumerName.__name__, value)

    @Validator.validate(type=str, min_length=1, max_length=2048, pattern=r"arn:aws.*:kinesis:.*:\d{12}:stream/.+")
    def StreamARN(self, value: str):
        return self._set_property(self.StreamARN.__name__, value)

