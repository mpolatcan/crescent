from pyformation.resources.shared import BaseModel


class CloudwatchLoggingOptions(BaseModel):
    __PROPERTY_ENABLED = "Enabled"
    __PROPERTY_LOG_GROUP_NAME = "LogGroupName"
    __PROPERTY_LOG_STREAM_NAME = "LogStreamName"

    def enabled(self, value: bool):
        return self._add_field(self.__PROPERTY_ENABLED, value)

    def log_group_name(self, value: str):
        return self._add_field(self.__PROPERTY_LOG_GROUP_NAME, value)

    def log_stream_name(self, value: str):
        return self._add_field(self.__PROPERTY_LOG_STREAM_NAME, value)
