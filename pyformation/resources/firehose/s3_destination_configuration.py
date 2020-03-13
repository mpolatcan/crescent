from pyformation.core import Model, Validator
from .buffering_hints import BufferingHints
from .cloudwatch_logging_options import CloudwatchLoggingOptions
from .encryption_configuration import EncryptionConfiguration


class S3DestinationConfiguration(Model):
    @Validator.validate(type=str)
    def BucketARN(self, value: str):
        return self._set_field(self.BucketARN.__name__, value)

    @Validator.validate(type=BufferingHints)
    def BufferingHints(self, value: BufferingHints):
        return self._set_field(self.BufferingHints.__name__, value.__to_dict__())

    @Validator.validate(type=CloudwatchLoggingOptions)
    def CloudwatchLoggingOptions(self, value: CloudwatchLoggingOptions):
        return self._set_field(self.CloudwatchLoggingOptions.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def CompressionFormat(self, value: str):
        return self._set_field(self.CompressionFormat.__name__, value)

    @Validator.validate(type=EncryptionConfiguration)
    def EncryptionConfiguration(self, value: EncryptionConfiguration):
        return self._set_field(self.EncryptionConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def ErrorOutputPrefix(self, value: str):
        return self._set_field(self.ErrorOutputPrefix.__name__, value)

    @Validator.validate(type=str)
    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)

    @Validator.validate(type=str)
    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)
