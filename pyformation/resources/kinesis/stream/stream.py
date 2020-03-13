from pyformation.core import Resource, Tag, Validator
from .stream_encryption import StreamEncryption


class Stream(Resource):
    __TYPE = "AWS::Kinesis::Stream"

    def __init__(self, id: str):
        super(Stream, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def Name(self, value: str):
        return self._set_property(self.Name.__name__, value)

    @Validator.validate(type=int)
    def RetentionPeriodHours(self, value: int):
        return self._set_property(self.RetentionPeriodHours.__name__, value)

    @Validator.validate(type=int)
    def ShardCount(self, value: int):
        return self._set_property(self.ShardCount.__name__, value)

    @Validator.validate(type=StreamEncryption)
    def StreamEncryption(self, value: StreamEncryption):
        return self._set_property(self.StreamEncryption.__name__, value.__to_dict__())

    @Validator.validate(type=Tag)
    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
