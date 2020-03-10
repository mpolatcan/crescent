from pyformation.resources.shared import BaseModel
from pyformation.resources.firehose import BufferingHints, CloudwatchLoggingOptions, EncryptionConfiguration


class S3DestinationConfiguration(BaseModel):
    __PROPERTY_BUCKET_ARN = "BucketARN"
    __PROPERTY_BUFFERING_HINTS = "BufferingHints"
    __PROPERTY_CLOUDWATCH_LOGGING_OPTIONS = "CloudwatchLoggingOptions"
    __PROPERTY_COMPRESSION_FORMAT = "CompressionFormat"
    __PROPERTY_ENCRYPTION_CONFIGURATION = "EncryptionConfiguration"
    __PROPERTY_ERROR_OUTPUT_PREFIX = "ErrorOutputPrefix"
    __PROPERTY_PREFIX = "Prefix"
    __PROPERTY_ROLE_ARN = "RoleARN"

    def bucket_arn(self, value: str):
        return self._add_field(self.__PROPERTY_BUCKET_ARN, value)

    def buffering_hints(self, value: BufferingHints):
        return self._add_field(self.__PROPERTY_BUFFERING_HINTS, value)

    def cloudwatch_logging_options(self, value: CloudwatchLoggingOptions):
        return self._add_field(self.__PROPERTY_CLOUDWATCH_LOGGING_OPTIONS, value)

    def compression_format(self, value: str):
        return self._add_field(self.__PROPERTY_COMPRESSION_FORMAT, value)

    def encryption_configuration(self, value: EncryptionConfiguration):
        return self._add_field(self.__PROPERTY_ENCRYPTION_CONFIGURATION, value)

    def error_output_prefix(self, value: str):
        return self._add_field(self.__PROPERTY_ERROR_OUTPUT_PREFIX, value)

    def prefix(self, value: str):
        return self._add_field(self.__PROPERTY_PREFIX, value)

    def role_arn(self, value: str):
        return self._add_field(self.__PROPERTY_ROLE_ARN, value)
