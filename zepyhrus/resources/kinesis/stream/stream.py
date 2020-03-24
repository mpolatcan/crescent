from zepyhrus.core import Resource, Tag, Validator
from .stream_encryption import StreamEncryption
from .constants import RequiredProperties


class Stream(Resource):
    __TYPE = "AWS::Kinesis::Stream"

    def __init__(self, id: str):
        super(Stream, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str, min_length=1, max_length=128, pattern="[a-zA-Z0-9_.-]+")
    def Name(self, value: str):
        return self._set_property(self.Name.__name__, value)

    @Validator.validate(type=int)
    def RetentionPeriodHours(self, value: int):
        return self._set_property(self.RetentionPeriodHours.__name__, value)

    @Validator.validate(type=int, min_value=1)
    def ShardCount(self, value: int):
        return self._set_property(self.ShardCount.__name__, value)

    @Validator.validate(type=StreamEncryption, required_properties=RequiredProperties.STREAM_ENCRYPTION)
    def StreamEncryption(self, value: StreamEncryption):
        return self._set_property(self.StreamEncryption.__name__, value.__to_dict__())

    @Validator.validate(type=Tag)
    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
