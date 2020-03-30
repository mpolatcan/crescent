from crescent.core import Model, Validator
from .cloudwatch_logging_options import CloudWatchLoggingOptions
from .processing_configuration import ProcessingConfiguration
from .s3_destination_configuration import S3DestinationConfiguration
from .splunk_retry_options import SplunkRetryOptions
from .constants import ModelRequiredProperties, AllowedValues, Conditions


class SplunkDestinationConfiguration(Model):
    @Validator.validate(type=CloudWatchLoggingOptions, conditions=Conditions.CLOUDWATCH_LOGGING_OPTIONS)
    def CloudWatchLoggingOptions(self, cw_logging_opts: CloudWatchLoggingOptions):
        return self._set_field(self.CloudWatchLoggingOptions.__name__, cw_logging_opts.__to_dict__())

    @Validator.validate(type=int, min_value=180, max_value=600)
    def HECAcknowledgmentTimeoutInSeconds(self, hec_ack_timeout_in_secs: int):
        return self._set_field(self.HECAcknowledgmentTimeoutInSeconds.__name__, hec_ack_timeout_in_secs)

    @Validator.validate(type=str)
    def HECEndpoint(self, hec_endpoint: str):
        return self._set_field(self.HECEndpoint.__name__, hec_endpoint)

    @Validator.validate(type=str, allowed_values=AllowedValues.SPLUNK_DESTINATION_CONFIGURATION_HEC_ENDPOINT_TYPE)
    def HECEndpointType(self, hec_endpoint_type: str):
        return self._set_field(self.HECEndpointType.__name__, hec_endpoint_type)

    @Validator.validate(type=str)
    def HECToken(self, hec_token: str):
        return self._set_field(self.HECToken.__name__, hec_token)

    @Validator.validate(type=ProcessingConfiguration)
    def ProcessingConfiguration(self, processing_conf: ProcessingConfiguration):
        return self._set_field(self.ProcessingConfiguration.__name__, processing_conf.__to_dict__())

    @Validator.validate(type=SplunkRetryOptions, required_properties=ModelRequiredProperties.SPLUNK_RETRY_OPTIONS)
    def RetryOptions(self, splunk_retry_options: SplunkRetryOptions):
        return self._set_field(self.RetryOptions.__name__, splunk_retry_options.__to_dict__())

    @Validator.validate(type=str, allowed_values=AllowedValues.SPLUNK_DESTINATION_CONFIGURATION_S3_BACKUP_MODE)
    def S3BackupMode(self, s3_backup_mode: str):
        return self._set_field(self.S3BackupMode.__name__, s3_backup_mode)

    @Validator.validate(type=S3DestinationConfiguration, required_properties=ModelRequiredProperties.S3_DESTINATION_CONFIGURATION)
    def S3Configuration(self, s3_conf: S3DestinationConfiguration):
        return self._set_field(self.S3Configuration.__name__, s3_conf.__to_dict__())
