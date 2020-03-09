from resources.shared import BaseModel
from resources.firehose import (
    BufferingHints,
    CloudwatchLoggingOptions,
    DataFormatConversionConfiguration,
    EncryptionConfiguration,
    ProcessingConfiguration,
    S3DestinationConfiguration
)


class ExtendedS3DestinationConfiguration(BaseModel):
    __PROPERTY_BUCKET_ARN = "BucketARN"
    __PROPERTY_BUFFERING_HINTS = "BufferingHints"
    __PROPERTY_CLOUDWATCH_LOGGING_OPTIONS = "CloudwatchLoggingOptions"
    __PROPERTY_COMPRESSION_FORMAT = "CompressionFormat"
    __PROPERTY_DATA_FORMAT_CONVERSION_CONFIGURATION = "DataFormatConversionConfiguration"
    __PROPERTY_ENCRYPTION_CONFIGURATION = "EncryptionConfiguration"
    __PROPERTY_ERROR_OUTPUT_PREFIX = "ErrorOutputPrefix"
    __PROPERTY_PREFIX = "Prefix"
    __PROPERTY_PROCESSING_CONFIGURATION = "ProcessingConfiguration"
    __PROPERTY_ROLE_ARN = "RoleARN"
    __PROPERTY_S3_BACKUP_CONFIGURATION = "S3BackupConfiguration"
    __PROPERTY_S3_BACKUP_MODE = "S3BackupMode"

    def bucket_arn(self, value: str):
        return self._add_field(self.__PROPERTY_BUCKET_ARN, value)

    def buffering_hints(self, value: BufferingHints):
        return self._add_field(self.__PROPERTY_BUFFERING_HINTS, value.create())

    def cloudwatch_logging_options(self, value: CloudwatchLoggingOptions):
        return self._add_field(self.__PROPERTY_CLOUDWATCH_LOGGING_OPTIONS, value.create())

    def compression_format(self, value: str):
        return self._add_field(self.__PROPERTY_COMPRESSION_FORMAT, value)

    def data_format_conversion_configuration(self, value: DataFormatConversionConfiguration):
        return self._add_field(self.__PROPERTY_DATA_FORMAT_CONVERSION_CONFIGURATION, value.create())

    def encryption_configuration(self, value: EncryptionConfiguration):
        return self._add_field(self.__PROPERTY_ENCRYPTION_CONFIGURATION, value.create())

    def error_output_prefix(self, value: str):
        return self._add_field(self.__PROPERTY_ERROR_OUTPUT_PREFIX, value)

    def prefix(self, value: str):
        return self._add_field(self.__PROPERTY_PREFIX, value)

    def processing_configuration(self, value: ProcessingConfiguration):
        return self._add_field(self.__PROPERTY_PROCESSING_CONFIGURATION, value.create())

    def role_arn(self, value: str):
        return self._add_field(self.__PROPERTY_ROLE_ARN, value)

    def s3_backup_configuration(self, value: S3DestinationConfiguration):
        return self._add_field(self.__PROPERTY_S3_BACKUP_CONFIGURATION, value.create())

    def s3_backup_mode(self, value: str):
        return self._add_field(self.__PROPERTY_S3_BACKUP_MODE, value)
