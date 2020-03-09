from resources.shared import BaseModel
from resources.firehose import (
    CloudwatchLoggingOptions,
    ProcessingConfiguration,
    S3DestinationConfiguration,
    SplunkRetryOptions
)


class SplunkDestinationConfiguration(BaseModel):
    __PROPERTY_CLOUDWATCH_LOGGING_OPTIONS = "CloudwatchLoggingOptions"
    __PROPERTY_HEC_ACKNOWLEDGMENT_TIMEOUT_IN_SECONDS = "HECAcknowledgmentTimeoutInSeconds"
    __PROPERTY_HEC_ENDPOINT = "HECEndpoint"
    __PROPERTY_HEC_ENDPOINT_TYPE = "HECEndpointType"
    __PROPERTY_HEC_TOKEN = "HECToken"
    __PROPERTY_PROCESSING_CONFIGURATION = "ProcessingConfiguration"
    __PROPERTY_RETRY_OPTIONS = "RetryOptions"
    __PROPERTY_S3_BACKUP_MODE = "S3BackupMode"
    __PROPERTY_S3_CONFIGURATION = "S3Configuration"

    def cloudwatch_logging_options(self, value: CloudwatchLoggingOptions):
        return self._add_field(self.__PROPERTY_CLOUDWATCH_LOGGING_OPTIONS, value.create())

    def hec_acknowledgment_timeout_in_seconds(self, value: int):
        return self._add_field(self.__PROPERTY_HEC_ACKNOWLEDGMENT_TIMEOUT_IN_SECONDS, value)

    def hec_endpoint(self, value: str):
        return self._add_field(self.__PROPERTY_HEC_ENDPOINT, value)

    def hec_endpoint_type(self, value: str):
        return self._add_field(self.__PROPERTY_HEC_ENDPOINT_TYPE, value)

    def hec_token(self, value: str):
        return self._add_field(self.__PROPERTY_HEC_TOKEN, value)

    def processing_configuration(self, value: ProcessingConfiguration):
        return self._add_field(self.__PROPERTY_PROCESSING_CONFIGURATION, value.create())

    def retry_options(self, value: SplunkRetryOptions):
        return self._add_field(self.__PROPERTY_RETRY_OPTIONS, value.create())

    def s3_backup_mode(self, value: str):
        return self._add_field(self.__PROPERTY_S3_BACKUP_MODE, value)

    def s3_configuration(self, value: S3DestinationConfiguration):
        return self._add_field(self.__PROPERTY_S3_CONFIGURATION, value.create())
