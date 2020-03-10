from pyformation.resources.shared import BaseModel
from pyformation.resources.firehose import (
    ElasticsearchBufferingHints,
    CloudwatchLoggingOptions,
    ProcessingConfiguration,
    ElasticsearchRetryOptions,
    S3DestinationConfiguration
)


class ElasticsearchDestinationConfiguration(BaseModel):
    __PROPERTY_BUFFERING_HINTS = "BufferingHints"
    __PROPERTY_CLOUDWATCH_LOGGING_OPTIONS = "CloudwatchLoggingOptions"
    __PROPERTY_DOMAIN_ARN = "DomainARN"
    __PROPERTY_INDEX_NAME = "IndexName"
    __PROPERTY_INDEX_ROTATION_PERIOD = "IndexRotationPeriod"
    __PROPERTY_PROCESSING_CONFIGURATION = "ProcessingConfiguration"
    __PROPERTY_RETRY_OPTIONS = "RetryOptions"
    __PROPERTY_ROLE_ARN = "RoleARN"
    __PROPERTY_S3_BACKUP_MODE = "S3BackupMode"
    __PROPERTY_S3_CONFIGURATION = "S3Configuration"
    __PROPERTY_TYPE_NAME = "TypeName"

    def buffering_hints(self, value: ElasticsearchBufferingHints):
        return self._add_field(self.__PROPERTY_BUFFERING_HINTS, value)

    def cloudwatch_logging_options(self, value: CloudwatchLoggingOptions):
        return self._add_field(self.__PROPERTY_CLOUDWATCH_LOGGING_OPTIONS, value)

    def domain_arn(self, value: str):
        return self._add_field(self.__PROPERTY_DOMAIN_ARN, value)

    def index_name(self, value: str):
        return self._add_field(self.__PROPERTY_INDEX_NAME, value)

    def index_rotation_period(self, value: str):
        return self._add_field(self.__PROPERTY_INDEX_ROTATION_PERIOD, value)

    def processing_configuration(self, value: ProcessingConfiguration):
        return self._add_field(self.__PROPERTY_PROCESSING_CONFIGURATION, value)

    def retry_options(self, value: ElasticsearchRetryOptions):
        return self._add_field(self.__PROPERTY_RETRY_OPTIONS, value)

    def role_arn(self, value: str):
        return self._add_field(self.__PROPERTY_ROLE_ARN, value)

    def s3_backup_mode(self, value: str):
        return self._add_field(self.__PROPERTY_S3_BACKUP_MODE, value)

    def s3_configuration(self, value: S3DestinationConfiguration):
        return self._add_field(self.__PROPERTY_S3_CONFIGURATION, value)

    def type_name(self, value: str):
        return self._add_field(self.__PROPERTY_TYPE_NAME, value)
