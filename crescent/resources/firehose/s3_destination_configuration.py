from crescent.core import Model
from crescent.functions import AnyFn
from .buffering_hints import BufferingHints
from .cloudwatch_logging_options import CloudWatchLoggingOptions
from .encryption_configuration import EncryptionConfiguration
from .constants import ModelRequiredProperties, AllowedValues
from typing import Union


class S3DestinationConfiguration(Model):
    def __init__(self):
        super(S3DestinationConfiguration, self).__init__(
            min_length={self.BucketARN.__name__: 1,
                        self.RoleARN.__name__: 1},
            max_length={self.BucketARN.__name__: 2048,
                        self.RoleARN.__name__: 512},
            pattern={self.BucketARN.__name__: r"arn:.*",
                     self.RoleARN.__name__: r"arn:.*"},
            allowed_values={self.CompressionFormat.__name__: AllowedValues.S3_DESTINATION_CONFIGURATION_COMPRESSION_FORMAT},
            required_properties=ModelRequiredProperties.S3_DESTINATION_CONFIGURATION
        )

    def BucketARN(self, bucket_arn: Union[str, AnyFn]):
        return self._set_field(self.BucketARN.__name__, bucket_arn)

    def BufferingHints(self, buffering_hints: BufferingHints):
        return self._set_field(self.BufferingHints.__name__, buffering_hints)

    def CloudWatchLoggingOptions(self, cw_logging_opts: CloudWatchLoggingOptions):
        return self._set_field(self.CloudWatchLoggingOptions.__name__, cw_logging_opts)

    def CompressionFormat(self, compression_format: Union[str, AnyFn]):
        return self._set_field(self.CompressionFormat.__name__, compression_format)

    def EncryptionConfiguration(self, encryption_conf: EncryptionConfiguration):
        return self._set_field(self.EncryptionConfiguration.__name__, encryption_conf)

    def ErrorOutputPrefix(self, error_output_prefix: Union[str, AnyFn]):
        return self._set_field(self.ErrorOutputPrefix.__name__, error_output_prefix)

    def Prefix(self, prefix: Union[str, AnyFn]):
        return self._set_field(self.Prefix.__name__, prefix)

    def RoleARN(self, role_arn: Union[str, AnyFn]):
        return self._set_field(self.RoleARN.__name__, role_arn)
