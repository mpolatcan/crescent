from resources.shared import BaseModel
from resources.firehose import (
    CloudwatchLoggingOptions,
    CopyCommand,
    ProcessingConfiguration,
    S3DestinationConfiguration
)


class RedshiftDestinationConfiguration(BaseModel):
    __PROPERTY_CLOUDWATCH_LOGGING_OPTIONS = "CloudwatchLoggingOptions"
    __PROPERTY_CLUSTER_JDBC_URL = "ClusterJDBCURL"
    __PROPERTY_COPY_COMMAND = "CopyCommand"
    __PROPERTY_PASSWORD = "Password"
    __PROPERTY_PROCESSING_CONFIGURATION = "ProcessingConfiguration"
    __PROPERTY_ROLE_ARN = "RoleARN"
    __PROPERTY_S3_CONFIGURATION = "S3Configuration"
    __PROPERTY_USERNAME = "Username"

    def cloudwatch_logging_options(self, value: CloudwatchLoggingOptions):
        return self._add_field(self.__PROPERTY_CLOUDWATCH_LOGGING_OPTIONS, value.create())

    def cluster_jdbc_url(self, value: str):
        return self._add_field(self.__PROPERTY_CLUSTER_JDBC_URL, value)

    def copy_command(self, value: CopyCommand):
        return self._add_field(self.__PROPERTY_COPY_COMMAND, value.create())

    def password(self, value: str):
        return self._add_field(self.__PROPERTY_PASSWORD, value)

    def processing_configuration(self, value: ProcessingConfiguration):
        return self._add_field(self.__PROPERTY_PROCESSING_CONFIGURATION, value.create())

    def role_arn(self, value: str):
        return self._add_field(self.__PROPERTY_ROLE_ARN, value)

    def s3_configuration(self, value: S3DestinationConfiguration):
        return self._add_field(self.__PROPERTY_S3_CONFIGURATION, value.create())

    def username(self, value: str):
        return self._add_field(self.__PROPERTY_USERNAME, value)
