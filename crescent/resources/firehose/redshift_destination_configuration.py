from crescent.core import Model
from .cloudwatch_logging_options import CloudWatchLoggingOptions
from .copy_command import CopyCommand
from .processing_configuration import ProcessingConfiguration
from .s3_destination_configuration import S3DestinationConfiguration
from .constants import ModelRequiredProperties


class RedshiftDestinationConfiguration(Model):
    def __init__(self):
        super(RedshiftDestinationConfiguration, self).__init__(
            min_length={self.ClusterJDBCURL.__name__: 1,
                        self.Password.__name__: 6,
                        self.RoleARN.__name__: 1,
                        self.Username.__name__: 1},
            max_length={self.RoleARN.__name__: 512},
            pattern={self.ClusterJDBCURL.__name__: r"jdbc:(redshift|postgresql)://((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+redshift\.([a-zA-Z0-9\.]+):\d{1,5}/[a-zA-Z0-9_$]+",
                     self.RoleARN.__name__: r"arn:.*"},
            required_properties=ModelRequiredProperties.REDSHIFT_DESTINATION_CONFIGURATION
        )

    def CloudWatchLoggingOptions(self, cw_logging_opts: CloudWatchLoggingOptions):
        return self._set_field(self.CloudWatchLoggingOptions.__name__, cw_logging_opts)

    def ClusterJDBCURL(self, cluster_jdbc_url: str):
        return self._set_field(self.ClusterJDBCURL.__name__, cluster_jdbc_url)

    def CopyCommand(self, copy_command: CopyCommand):
        return self._set_field(self.CopyCommand.__name__, copy_command)

    def Password(self, password: str):
        return self._set_field(self.Password.__name__, password)

    def ProcessingConfiguration(self, processing_conf: ProcessingConfiguration):
        return self._set_field(self.ProcessingConfiguration.__name__, processing_conf)

    def RoleARN(self, role_arn: str):
        return self._set_field(self.RoleARN.__name__, role_arn)

    def S3Configuration(self, s3_conf: S3DestinationConfiguration):
        return self._set_field(self.S3Configuration.__name__, s3_conf)

    def Username(self, username: str):
        return self._set_field(self.Username.__name__, username)
