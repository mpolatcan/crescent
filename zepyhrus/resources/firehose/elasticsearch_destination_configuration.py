from zepyhrus.core import Model, Validator
from .elasticsearch_buffering_hints import ElasticsearchBufferingHints
from .cloudwatch_logging_options import CloudWatchLoggingOptions
from .processing_configuration import ProcessingConfiguration
from .elasticsearch_retry_options import ElasticsearchRetryOptions
from .s3_destination_configuration import S3DestinationConfiguration
from .constants import RequiredProperties, AllowedValues, Conditions


class ElasticsearchDestinationConfiguration(Model):
    @Validator.validate(type=ElasticsearchBufferingHints, required_properties=RequiredProperties.ELASTICSEARCH_BUFFERING_HINTS)
    def BufferingHints(self, value: ElasticsearchBufferingHints):
        return self._set_field(self.BufferingHints.__name__, value.__to_dict__())

    @Validator.validate(type=CloudWatchLoggingOptions, conditions=Conditions.CLOUDWATCH_LOGGING_OPTIONS)
    def CloudWatchLoggingOptions(self, value: CloudWatchLoggingOptions):
        return self._set_field(self.CloudWatchLoggingOptions.__name__, value.__to_dict__())

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"arn:.*")
    def DomainARN(self, value: str):
        return self._set_field(self.DomainARN.__name__, value)

    @Validator.validate(type=str, min_length=1, max_length=80)
    def IndexName(self, value: str):
        return self._set_field(self.IndexName.__name__, value)

    @Validator.validate(type=str, allowed_values=AllowedValues.ELASTICSEARCH_DESTINATION_CONFIGURATION_INDEX_ROTATION_PERIOD)
    def IndexRotationPeriod(self, value: str):
        return self._set_field(self.IndexRotationPeriod.__name__, value)

    @Validator.validate(type=ProcessingConfiguration)
    def ProcessingConfiguration(self, value: ProcessingConfiguration):
        return self._set_field(self.ProcessingConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=ElasticsearchRetryOptions, required_properties=RequiredProperties.ELASTICSEARCH_RETRY_OPTIONS)
    def RetryOptions(self, value: ElasticsearchRetryOptions):
        return self._set_field(self.RetryOptions.__name__, value.__to_dict__())

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"arn:.*")
    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)

    @Validator.validate(type=str, allowed_values=AllowedValues.ELASTICSEARCH_DESTINATION_CONFIGURATION_S3_BACKUP_MODE)
    def S3BackupMode(self, value: str):
        return self._set_field(self.S3BackupMode.__name__, value)

    @Validator.validate(type=S3DestinationConfiguration, required_properties=RequiredProperties.S3_DESTINATION_CONFIGURATION)
    def S3Configuration(self, value: S3DestinationConfiguration):
        return self._set_field(self.S3Configuration.__name__, value.__to_dict__())

    @Validator.validate(type=str, min_length=0, max_length=100)
    def TypeName(self, value: str):
        return self._set_field(self.TypeName.__name__, value)
