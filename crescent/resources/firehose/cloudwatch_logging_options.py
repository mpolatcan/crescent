from crescent.core import Model, Validator


class CloudWatchLoggingOptions(Model):
    @Validator.validate(type=bool)
    def Enabled(self, enabled: bool):
        return self._set_field(self.Enabled.__name__, enabled)

    @Validator.validate(type=str)
    def LogGroupName(self, log_group_name: str):
        return self._set_field(self.LogGroupName.__name__, log_group_name)

    @Validator.validate(type=str)
    def LogStreamName(self, log_stream_name: str):
        return self._set_field(self.LogStreamName.__name__, log_stream_name)
