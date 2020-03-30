from crescent.core import Model, Validator
from .buffering_hints import BufferingHints
from .cloudwatch_logging_options import CloudWatchLoggingOptions
from .encryption_configuration import EncryptionConfiguration
from .constants import ModelRequiredProperties, AllowedValues, Conditions


class S3DestinationConfiguration(Model):
    @Validator.validate(type=str, min_length=1, max_length=2048, pattern=r"arn:.*")
    def BucketARN(self, bucket_arn: str):
        return self._set_field(self.BucketARN.__name__, bucket_arn)

    @Validator.validate(type=BufferingHints, required_properties=ModelRequiredProperties.BUFFERING_HINTS)
    def BufferingHints(self, buffering_hints: BufferingHints):
        return self._set_field(self.BufferingHints.__name__, buffering_hints.__to_dict__())

    @Validator.validate(type=CloudWatchLoggingOptions, conditions=Conditions.CLOUDWATCH_LOGGING_OPTIONS)
    def CloudWatchLoggingOptions(self, cw_logging_opts: CloudWatchLoggingOptions):
        return self._set_field(self.CloudWatchLoggingOptions.__name__, cw_logging_opts.__to_dict__())

    @Validator.validate(type=str, allowed_values=AllowedValues.S3_DESTINATION_CONFIGURATION_COMPRESSION_FORMAT)
    def CompressionFormat(self, compression_format: str):
        return self._set_field(self.CompressionFormat.__name__, compression_format)

    @Validator.validate(type=EncryptionConfiguration)
    def EncryptionConfiguration(self, encryption_conf: EncryptionConfiguration):
        return self._set_field(self.EncryptionConfiguration.__name__, encryption_conf.__to_dict__())

    @Validator.validate(type=str)
    def ErrorOutputPrefix(self, error_output_prefix: str):
        return self._set_field(self.ErrorOutputPrefix.__name__, error_output_prefix)

    @Validator.validate(type=str)
    def Prefix(self, prefix: str):
        return self._set_field(self.Prefix.__name__, prefix)

    @Validator.validate(type=str, min_length=1, max_length=512, pattern="arn:.*")
    def RoleARN(self, role_arn: str):
        return self._set_field(self.RoleARN.__name__, role_arn)
