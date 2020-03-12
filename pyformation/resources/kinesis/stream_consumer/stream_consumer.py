from pyformation import PyformationResource


class StreamConsumer(PyformationResource):
    __TYPE = "AWS::Kinesis::StreamConsumer"

    def __init__(self, id: str):
        super(StreamConsumer, self).__init__(id, self.__TYPE)

    def ConsumerName(self, value: str):
        return self._set_property(self.ConsumerName.__name__, value)

    def StreamARN(self, value: str):
        return self._set_property(self.StreamARN.__name__, value)

