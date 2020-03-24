from zepyhrus.core import Model, Validator
from .cloudwatch_logging_options import CloudWatchLoggingOptions
from .copy_command import CopyCommand
from .processing_configuration import ProcessingConfiguration
from .s3_destination_configuration import S3DestinationConfiguration
from .constants import RequiredProperties, Conditions


class RedshiftDestinationConfiguration(Model):
    @Validator.validate(type=CloudWatchLoggingOptions, conditions=Conditions.CLOUDWATCH_LOGGING_OPTIONS)
    def CloudWatchLoggingOptions(self, value: CloudWatchLoggingOptions):
        return self._set_field(self.CloudWatchLoggingOptions.__name__, value.__to_dict__())

    @Validator.validate(type=str, min_length=1, pattern=r"jdbc:(redshift|postgresql)://((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+redshift\.([a-zA-Z0-9\.]+):\d{1,5}/[a-zA-Z0-9_$]+")
    def ClusterJDBCURL(self, value: str):
        return self._set_field(self.ClusterJDBCURL.__name__, value)

    @Validator.validate(type=CopyCommand, required_properties=RequiredProperties.COPY_COMMAND)
    def CopyCommand(self, value: CopyCommand):
        return self._set_field(self.CopyCommand.__name__, value.__to_dict__())

    @Validator.validate(type=str, min_length=6)
    def Password(self, value: str):
        return self._set_field(self.Password.__name__, value)

    @Validator.validate(type=ProcessingConfiguration)
    def ProcessingConfiguration(self, value: ProcessingConfiguration):
        return self._set_field(self.ProcessingConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"arn:.*")
    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)

    @Validator.validate(type=S3DestinationConfiguration, required_properties=RequiredProperties.S3_DESTINATION_CONFIGURATION)
    def S3Configuration(self, value: S3DestinationConfiguration):
        return self._set_field(self.S3Configuration.__name__, value.__to_dict__())

    @Validator.validate(type=str, min_length=1)
    def Username(self, value: str):
        return self._set_field(self.Username.__name__, value)
