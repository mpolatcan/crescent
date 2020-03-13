from pyformation.core import Model, Validator
from .cloudwatch_logging_options import CloudwatchLoggingOptions
from .processing_configuration import ProcessingConfiguration
from .s3_destination_configuration import S3DestinationConfiguration
from .splunk_retry_options import SplunkRetryOptions


class SplunkDestinationConfiguration(Model):
    __PROPERTY_S3_CONFIGURATION = "S3Configuration"

    @Validator.validate(type=CloudwatchLoggingOptions)
    def CloudwatchLoggingOptions(self, value: CloudwatchLoggingOptions):
        return self._set_field(self.CloudwatchLoggingOptions.__name__, value.__to_dict__())

    @Validator.validate(type=int)
    def HECAcknowledgmentTimeoutInSeconds(self, value: int):
        return self._set_field(self.HECAcknowledgmentTimeoutInSeconds.__name__, value)

    @Validator.validate(type=str)
    def HECEndpoint(self, value: str):
        return self._set_field(self.HECEndpoint.__name__, value)

    @Validator.validate(type=str)
    def HECEndpointType(self, value: str):
        return self._set_field(self.HECEndpointType.__name__, value)

    @Validator.validate(type=str)
    def HECToken(self, value: str):
        return self._set_field(self.HECToken.__name__, value)

    @Validator.validate(type=ProcessingConfiguration)
    def ProcessingConfiguration(self, value: ProcessingConfiguration):
        return self._set_field(self.ProcessingConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=SplunkRetryOptions)
    def RetryOptions(self, value: SplunkRetryOptions):
        return self._set_field(self.RetryOptions.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def S3BackupMode(self, value: str):
        return self._set_field(self.S3BackupMode.__name__, value)

    @Validator.validate(type=S3DestinationConfiguration)
    def S3Configuration(self, value: S3DestinationConfiguration):
        return self._set_field(self.S3Configuration.__name__, value.__to_dict__())
