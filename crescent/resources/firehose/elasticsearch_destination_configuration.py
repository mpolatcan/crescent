from crescent.core import Model, Validator
from .elasticsearch_buffering_hints import ElasticsearchBufferingHints
from .cloudwatch_logging_options import CloudWatchLoggingOptions
from .processing_configuration import ProcessingConfiguration
from .elasticsearch_retry_options import ElasticsearchRetryOptions
from .s3_destination_configuration import S3DestinationConfiguration
from .constants import ModelRequiredProperties, AllowedValues, Conditions


class ElasticsearchDestinationConfiguration(Model):
    @Validator.validate(type=ElasticsearchBufferingHints, required_properties=ModelRequiredProperties.ELASTICSEARCH_BUFFERING_HINTS)
    def BufferingHints(self, buffering_hints: ElasticsearchBufferingHints):
        return self._set_field(self.BufferingHints.__name__, buffering_hints.__to_dict__())

    @Validator.validate(type=CloudWatchLoggingOptions, conditions=Conditions.CLOUDWATCH_LOGGING_OPTIONS)
    def CloudWatchLoggingOptions(self, cw_logging_opts: CloudWatchLoggingOptions):
        return self._set_field(self.CloudWatchLoggingOptions.__name__, cw_logging_opts.__to_dict__())

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"arn:.*")
    def DomainARN(self, domain_arn: str):
        return self._set_field(self.DomainARN.__name__, domain_arn)

    @Validator.validate(type=str, min_length=1, max_length=80)
    def IndexName(self, index_name: str):
        return self._set_field(self.IndexName.__name__, index_name)

    @Validator.validate(type=str, allowed_values=AllowedValues.ELASTICSEARCH_DESTINATION_CONFIGURATION_INDEX_ROTATION_PERIOD)
    def IndexRotationPeriod(self, index_rotation_period: str):
        return self._set_field(self.IndexRotationPeriod.__name__, index_rotation_period)

    @Validator.validate(type=ProcessingConfiguration)
    def ProcessingConfiguration(self, processing_conf: ProcessingConfiguration):
        return self._set_field(self.ProcessingConfiguration.__name__, processing_conf.__to_dict__())

    @Validator.validate(type=ElasticsearchRetryOptions, required_properties=ModelRequiredProperties.ELASTICSEARCH_RETRY_OPTIONS)
    def RetryOptions(self, elasticsearch_retry_opts: ElasticsearchRetryOptions):
        return self._set_field(self.RetryOptions.__name__, elasticsearch_retry_opts.__to_dict__())

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"arn:.*")
    def RoleARN(self, role_arn: str):
        return self._set_field(self.RoleARN.__name__, role_arn)

    @Validator.validate(type=str, allowed_values=AllowedValues.ELASTICSEARCH_DESTINATION_CONFIGURATION_S3_BACKUP_MODE)
    def S3BackupMode(self, s3_backup_mode: str):
        return self._set_field(self.S3BackupMode.__name__, s3_backup_mode)

    @Validator.validate(type=S3DestinationConfiguration, required_properties=ModelRequiredProperties.S3_DESTINATION_CONFIGURATION)
    def S3Configuration(self, s3_conf: S3DestinationConfiguration):
        return self._set_field(self.S3Configuration.__name__, s3_conf.__to_dict__())

    @Validator.validate(type=str, min_length=0, max_length=100)
    def TypeName(self, type_name: str):
        return self._set_field(self.TypeName.__name__, type_name)
