from zepyhrus.core import Model, Validator
from .buffering_hints import BufferingHints
from .cloudwatch_logging_options import CloudWatchLoggingOptions
from .encryption_configuration import EncryptionConfiguration
from .constants import RequiredProperties, AllowedValues, Conditions


class S3DestinationConfiguration(Model):
    @Validator.validate(type=str, min_length=1, max_length=2048, pattern=r"arn:.*")
    def BucketARN(self, value: str):
        return self._set_field(self.BucketARN.__name__, value)

    @Validator.validate(type=BufferingHints, required_properties=RequiredProperties.BUFFERING_HINTS)
    def BufferingHints(self, value: BufferingHints):
        return self._set_field(self.BufferingHints.__name__, value.__to_dict__())

    @Validator.validate(type=CloudWatchLoggingOptions, conditions=Conditions.CLOUDWATCH_LOGGING_OPTIONS)
    def CloudWatchLoggingOptions(self, value: CloudWatchLoggingOptions):
        return self._set_field(self.CloudWatchLoggingOptions.__name__, value.__to_dict__())

    @Validator.validate(type=str, allowed_values=AllowedValues.S3_DESTINATION_CONFIGURATION_COMPRESSION_FORMAT)
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

    @Validator.validate(type=str, min_length=1, max_length=512, pattern="arn:.*")
    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)
