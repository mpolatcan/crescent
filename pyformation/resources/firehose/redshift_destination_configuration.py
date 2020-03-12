from pyformation import PyformationModel
from .cloudwatch_logging_options import CloudwatchLoggingOptions
from .copy_command import CopyCommand
from .processing_configuration import ProcessingConfiguration
from .s3_destination_configuration import S3DestinationConfiguration


class RedshiftDestinationConfiguration(PyformationModel):
    def CloudwatchLoggingOptions(self, value: CloudwatchLoggingOptions):
        return self._set_field(self.CloudwatchLoggingOptions.__name__, value.__to_dict__())

    def ClusterJDBCURL(self, value: str):
        return self._set_field(self.ClusterJDBCURL.__name__, value)

    def CopyCommand(self, value: CopyCommand):
        return self._set_field(self.CopyCommand.__name__, value.__to_dict__())

    def Password(self, value: str):
        return self._set_field(self.Password.__name__, value)

    def ProcessingConfiguration(self, value: ProcessingConfiguration):
        return self._set_field(self.ProcessingConfiguration.__name__, value.__to_dict__())

    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)

    def S3Configuration(self, value: S3DestinationConfiguration):
        return self._set_field(self.S3Configuration.__name__, value.__to_dict__())

    def Username(self, value: str):
        return self._set_field(self.Username.__name__, value)
