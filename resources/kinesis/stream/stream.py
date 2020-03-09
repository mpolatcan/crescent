from resources.shared import BaseCloudFormationResourceModel, Tag
from resources.kinesis.stream import StreamEncryption


class Stream(BaseCloudFormationResourceModel):
    __TYPE = "AWS::Kinesis::Stream"
    __PROPERTY_NAME = "Name"
    __PROPERTY_RETENTION_PERIOD_HOURS = "RetentionPeriodHours"
    __PROPERTY_SHARD_COUNT = "ShardCount"
    __PROPERTY_STREAM_ENCRYPTION = "StreamEncryption"
    __PROPERTY_TAGS = "Tags"

    def __init__(self):
        super(Stream, self).__init__(type=self.__TYPE)

    def name(self, value: str):
        return self._add_property_field(self.__PROPERTY_NAME, value)

    def retention_period_hours(self, value: int):
        return self._add_property_field(self.__PROPERTY_RETENTION_PERIOD_HOURS, value)

    def shard_count(self, value: int):
        return self._add_property_field(self.__PROPERTY_SHARD_COUNT, value)

    def stream_encryption(self, value: StreamEncryption):
        return self._add_property_field(self.__PROPERTY_STREAM_ENCRYPTION, value.create())

    def tags(self, *value: Tag):
        return self._add_property_field(self.__PROPERTY_TAGS, [tag.create() for tag in list(value)])
