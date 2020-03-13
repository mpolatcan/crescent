from pyformation.core import Model, Validator
from .cloudwatch_logging_options import CloudwatchLoggingOptions
from .copy_command import CopyCommand
from .processing_configuration import ProcessingConfiguration
from .s3_destination_configuration import S3DestinationConfiguration


class RedshiftDestinationConfiguration(Model):
    @Validator.validate(type=CloudwatchLoggingOptions)
    def CloudwatchLoggingOptions(self, value: CloudwatchLoggingOptions):
        return self._set_field(self.CloudwatchLoggingOptions.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def ClusterJDBCURL(self, value: str):
        return self._set_field(self.ClusterJDBCURL.__name__, value)

    @Validator.validate(type=CopyCommand)
    def CopyCommand(self, value: CopyCommand):
        return self._set_field(self.CopyCommand.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def Password(self, value: str):
        return self._set_field(self.Password.__name__, value)

    @Validator.validate(type=ProcessingConfiguration)
    def ProcessingConfiguration(self, value: ProcessingConfiguration):
        return self._set_field(self.ProcessingConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)

    @Validator.validate(type=S3DestinationConfiguration)
    def S3Configuration(self, value: S3DestinationConfiguration):
        return self._set_field(self.S3Configuration.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def Username(self, value: str):
        return self._set_field(self.Username.__name__, value)
