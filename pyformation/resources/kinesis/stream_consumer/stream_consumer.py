from pyformation.core import Resource, Validator


class StreamConsumer(Resource):
    __TYPE = "AWS::Kinesis::StreamConsumer"

    def __init__(self, id: str):
        super(StreamConsumer, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def ConsumerName(self, value: str):
        return self._set_property(self.ConsumerName.__name__, value)

    @Validator.validate(type=str)
    def StreamARN(self, value: str):
        return self._set_property(self.StreamARN.__name__, value)

