from crescent.core import Model
from crescent.functions import AnyFn
from .cloudwatch_logging_options import CloudWatchLoggingOptions
from .processing_configuration import ProcessingConfiguration
from .s3_destination_configuration import S3DestinationConfiguration
from .splunk_retry_options import SplunkRetryOptions
from .constants import ModelRequiredProperties, AllowedValues
from typing import Union


class SplunkDestinationConfiguration(Model):
    def __init__(self):
        super(SplunkDestinationConfiguration, self).__init__(
            min_value={self.HECAcknowledgmentTimeoutInSeconds: 180},
            max_value={self.HECAcknowledgmentTimeoutInSeconds: 600},
            allowed_values={self.HECEndpointType.__name__: AllowedValues.SPLUNK_DESTINATION_CONFIGURATION_HEC_ENDPOINT_TYPE,
                            self.S3BackupMode.__name__: AllowedValues.SPLUNK_DESTINATION_CONFIGURATION_S3_BACKUP_MODE},
            required_properties=ModelRequiredProperties.SPLUNK_DESTINATION_CONFIGURATION,
        )

    def CloudWatchLoggingOptions(self, cw_logging_opts: CloudWatchLoggingOptions):
        return self._set_field(self.CloudWatchLoggingOptions.__name__, cw_logging_opts)

    def HECAcknowledgmentTimeoutInSeconds(self, hec_ack_timeout_in_secs: Union[int, AnyFn]):
        return self._set_field(self.HECAcknowledgmentTimeoutInSeconds.__name__, hec_ack_timeout_in_secs)

    def HECEndpoint(self, hec_endpoint: Union[str, AnyFn]):
        return self._set_field(self.HECEndpoint.__name__, hec_endpoint)

    def HECEndpointType(self, hec_endpoint_type: Union[str, AnyFn]):
        return self._set_field(self.HECEndpointType.__name__, hec_endpoint_type)

    def HECToken(self, hec_token: Union[str, AnyFn]):
        return self._set_field(self.HECToken.__name__, hec_token)

    def ProcessingConfiguration(self, processing_conf: ProcessingConfiguration):
        return self._set_field(self.ProcessingConfiguration.__name__, processing_conf)

    def RetryOptions(self, splunk_retry_options: SplunkRetryOptions):
        return self._set_field(self.RetryOptions.__name__, splunk_retry_options)

    def S3BackupMode(self, s3_backup_mode: Union[str, AnyFn]):
        return self._set_field(self.S3BackupMode.__name__, s3_backup_mode)

    def S3Configuration(self, s3_conf: S3DestinationConfiguration):
        return self._set_field(self.S3Configuration.__name__, s3_conf)
