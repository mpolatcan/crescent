from pyformation.core import Model, Validator


class LoggingConfiguration(Model):
    @Validator.validate(type=str)
    def DestinationBucketName(self, value: str):
        return self._set_field(self.DestinationBucketName.__name__, value)

    @Validator.validate(type=str)
    def LogFilePrefix(self, value: str):
        return self._set_field(self.LogFilePrefix.__name__, value)
