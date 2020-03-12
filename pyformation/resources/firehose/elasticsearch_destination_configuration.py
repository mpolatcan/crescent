from pyformation import PyformationModel
from .elasticsearch_buffering_hints import ElasticsearchBufferingHints
from .cloudwatch_logging_options import CloudwatchLoggingOptions
from .processing_configuration import ProcessingConfiguration
from .elasticsearch_retry_options import ElasticsearchRetryOptions
from .s3_destination_configuration import S3DestinationConfiguration


class ElasticsearchDestinationConfiguration(PyformationModel):
    def BufferingHints(self, value: ElasticsearchBufferingHints):
        return self._set_field(self.BufferingHints.__name__, value.__to_dict__())

    def CloudwatchLoggingOptions(self, value: CloudwatchLoggingOptions):
        return self._set_field(self.CloudwatchLoggingOptions.__name__, value.__to_dict__())

    def DomainARN(self, value: str):
        return self._set_field(self.DomainARN.__name__, value)

    def IndexName(self, value: str):
        return self._set_field(self.IndexName.__name__, value)

    def IndexRotationPeriod(self, value: str):
        return self._set_field(self.IndexRotationPeriod.__name__, value)

    def ProcessingConfiguration(self, value: ProcessingConfiguration):
        return self._set_field(self.ProcessingConfiguration.__name__, value.__to_dict__())

    def RetryOptions(self, value: ElasticsearchRetryOptions):
        return self._set_field(self.RetryOptions.__name__, value.__to_dict__())

    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)

    def S3BackupMode(self, value: str):
        return self._set_field(self.S3BackupMode.__name__, value)

    def S3Configuration(self, value: S3DestinationConfiguration):
        return self._set_field(self.S3Configuration.__name__, value.__to_dict__())

    def TypeName(self, value: str):
        return self._set_field(self.TypeName.__name__, value)
