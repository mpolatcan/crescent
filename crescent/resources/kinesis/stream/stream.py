from crescent.core import Resource, Tag
from .stream_encryption import StreamEncryption
from .constants import ResourceRequiredProperties


class Stream(Resource):
    __TYPE = "AWS::Kinesis::Stream"

    def __init__(self, id: str):
        super(Stream, self).__init__(
            id=id,
            type=self.__TYPE,
            min_length={self.Name.__name__: 1},
            max_length={self.Name.__name__: 128},
            pattern={self.Name.__name__: r"[a-zA-Z0-9_.-]+"},
            min_value={self.ShardCount.__name__: 1},
            required_properties=ResourceRequiredProperties.STREAM
        )

    def Name(self, name: str):
        return self._set_property(self.Name.__name__, name)

    def RetentionPeriodHours(self, retention_period_hours: int):
        return self._set_property(self.RetentionPeriodHours.__name__, retention_period_hours)

    def ShardCount(self, shard_count: int):
        return self._set_property(self.ShardCount.__name__, shard_count)

    def StreamEncryption(self, stream_encryption: StreamEncryption):
        return self._set_property(self.StreamEncryption.__name__, stream_encryption)

    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
