from crescent.core import Resource, Tag, Validator
from .stream_encryption import StreamEncryption
from .constants import ModelRequiredProperties


class Stream(Resource):
    __TYPE = "AWS::Kinesis::Stream"

    def __init__(self, id: str):
        super(Stream, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str, min_length=1, max_length=128, pattern=r"[a-zA-Z0-9_.-]+")
    def Name(self, name: str):
        return self._set_property(self.Name.__name__, name)

    @Validator.validate(type=int)
    def RetentionPeriodHours(self, retention_period_hours: int):
        return self._set_property(self.RetentionPeriodHours.__name__, retention_period_hours)

    @Validator.validate(type=int, min_value=1)
    def ShardCount(self, shard_count: int):
        return self._set_property(self.ShardCount.__name__, shard_count)

    @Validator.validate(type=StreamEncryption, required_properties=ModelRequiredProperties.STREAM_ENCRYPTION)
    def StreamEncryption(self, stream_encryption: StreamEncryption):
        return self._set_property(self.StreamEncryption.__name__, stream_encryption.__to_dict__())

    @Validator.validate(type=Tag)
    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
