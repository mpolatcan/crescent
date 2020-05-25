from crescent.core import Model
from crescent.functions import AnyFn
from .elasticsearch_buffering_hints import ElasticsearchBufferingHints
from .cloudwatch_logging_options import CloudWatchLoggingOptions
from .processing_configuration import ProcessingConfiguration
from .elasticsearch_retry_options import ElasticsearchRetryOptions
from .s3_destination_configuration import S3DestinationConfiguration
from .constants import ModelRequiredProperties, AllowedValues
from typing import Union


class ElasticsearchDestinationConfiguration(Model):
    def __init__(self):
        super(ElasticsearchDestinationConfiguration, self).__init__(
            min_length={self.DomainARN.__name__: 1,
                        self.IndexName.__name__: 1,
                        self.RoleARN.__name__: 1,
                        self.TypeName.__name__: 0},
            max_length={self.DomainARN.__name__: 512,
                        self.IndexName.__name__: 80,
                        self.RoleARN.__name__: 512,
                        self.TypeName.__name__: 100},
            pattern={self.DomainARN.__name__: r"arn:.*",
                     self.RoleARN.__name__: r"arn:.*"},
            allowed_values={self.IndexRotationPeriod.__name__: AllowedValues.ELASTICSEARCH_DESTINATION_CONFIGURATION_INDEX_ROTATION_PERIOD,
                            self.S3BackupMode.__name__: AllowedValues.ELASTICSEARCH_DESTINATION_CONFIGURATION_S3_BACKUP_MODE},
            required_properties=ModelRequiredProperties.ELASTICSEARCH_DESTINATION_CONFIGURATION
        )

    def BufferingHints(self, buffering_hints: ElasticsearchBufferingHints):
        return self._set_field(self.BufferingHints.__name__, buffering_hints)

    def CloudWatchLoggingOptions(self, cw_logging_opts: CloudWatchLoggingOptions):
        return self._set_field(self.CloudWatchLoggingOptions.__name__, cw_logging_opts)

    def DomainARN(self, domain_arn: Union[str, AnyFn]):
        return self._set_field(self.DomainARN.__name__, domain_arn)

    def IndexName(self, index_name: Union[str, AnyFn]):
        return self._set_field(self.IndexName.__name__, index_name)

    def IndexRotationPeriod(self, index_rotation_period: Union[str, AnyFn]):
        return self._set_field(self.IndexRotationPeriod.__name__, index_rotation_period)

    def ProcessingConfiguration(self, processing_conf: ProcessingConfiguration):
        return self._set_field(self.ProcessingConfiguration.__name__, processing_conf)

    def RetryOptions(self, elasticsearch_retry_opts: ElasticsearchRetryOptions):
        return self._set_field(self.RetryOptions.__name__, elasticsearch_retry_opts)

    def RoleARN(self, role_arn: Union[str, AnyFn]):
        return self._set_field(self.RoleARN.__name__, role_arn)

    def S3BackupMode(self, s3_backup_mode: Union[str, AnyFn]):
        return self._set_field(self.S3BackupMode.__name__, s3_backup_mode)

    def S3Configuration(self, s3_conf: S3DestinationConfiguration):
        return self._set_field(self.S3Configuration.__name__, s3_conf)

    def TypeName(self, type_name: Union[str, AnyFn]):
        return self._set_field(self.TypeName.__name__, type_name)
