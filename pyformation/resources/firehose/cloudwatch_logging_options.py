from pyformation.core import Model, Validator


class CloudwatchLoggingOptions(Model):
    @Validator.validate(type=bool)
    def Enabled(self, value: bool):
        return self._set_field(self.Enabled.__name__, value)

    @Validator.validate(type=str)
    def LogGroupName(self, value: str):
        return self._set_field(self.LogGroupName.__name__, value)

    @Validator.validate(type=str)
    def LogStreamName(self, value: str):
        return self._set_field(self.LogStreamName.__name__, value)
