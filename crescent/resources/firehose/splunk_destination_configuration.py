from crescent.core import Model, Validator
from .cloudwatch_logging_options import CloudWatchLoggingOptions
from .processing_configuration import ProcessingConfiguration
from .s3_destination_configuration import S3DestinationConfiguration
from .splunk_retry_options import SplunkRetryOptions
from .constants import RequiredProperties, AllowedValues, Conditions


class SplunkDestinationConfiguration(Model):
    @Validator.validate(type=CloudWatchLoggingOptions, conditions=Conditions.CLOUDWATCH_LOGGING_OPTIONS)
    def CloudWatchLoggingOptions(self, value: CloudWatchLoggingOptions):
        return self._set_field(self.CloudWatchLoggingOptions.__name__, value.__to_dict__())

    @Validator.validate(type=int, min_value=180, max_value=600)
    def HECAcknowledgmentTimeoutInSeconds(self, value: int):
        return self._set_field(self.HECAcknowledgmentTimeoutInSeconds.__name__, value)

    @Validator.validate(type=str)
    def HECEndpoint(self, value: str):
        return self._set_field(self.HECEndpoint.__name__, value)

    @Validator.validate(type=str, allowed_values=AllowedValues.SPLUNK_DESTINATION_CONFIGURATION_HEC_ENDPOINT_TYPE)
    def HECEndpointType(self, value: str):
        return self._set_field(self.HECEndpointType.__name__, value)

    @Validator.validate(type=str)
    def HECToken(self, value: str):
        return self._set_field(self.HECToken.__name__, value)

    @Validator.validate(type=ProcessingConfiguration)
    def ProcessingConfiguration(self, value: ProcessingConfiguration):
        return self._set_field(self.ProcessingConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=SplunkRetryOptions, required_properties=RequiredProperties.SPLUNK_RETRY_OPTIONS)
    def RetryOptions(self, value: SplunkRetryOptions):
        return self._set_field(self.RetryOptions.__name__, value.__to_dict__())

    @Validator.validate(type=str, allowed_values=AllowedValues.SPLUNK_DESTINATION_CONFIGURATION_S3_BACKUP_MODE)
    def S3BackupMode(self, value: str):
        return self._set_field(self.S3BackupMode.__name__, value)

    @Validator.validate(type=S3DestinationConfiguration, required_properties=RequiredProperties.S3_DESTINATION_CONFIGURATION)
    def S3Configuration(self, value: S3DestinationConfiguration):
        return self._set_field(self.S3Configuration.__name__, value.__to_dict__())
