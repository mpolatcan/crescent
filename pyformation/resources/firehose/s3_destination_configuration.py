from pyformation import PyformationModel
from .buffering_hints import BufferingHints
from .cloudwatch_logging_options import CloudwatchLoggingOptions
from .encryption_configuration import EncryptionConfiguration


class S3DestinationConfiguration(PyformationModel):
    def BucketARN(self, value: str):
        return self._set_field(self.BucketARN.__name__, value)

    def BufferingHints(self, value: BufferingHints):
        return self._set_field(self.BufferingHints.__name__, value.__to_dict__())

    def CloudwatchLoggingOptions(self, value: CloudwatchLoggingOptions):
        return self._set_field(self.CloudwatchLoggingOptions.__name__, value.__to_dict__())

    def CompressionFormat(self, value: str):
        return self._set_field(self.CompressionFormat.__name__, value)

    def EncryptionConfiguration(self, value: EncryptionConfiguration):
        return self._set_field(self.EncryptionConfiguration.__name__, value.__to_dict__())

    def ErrorOutputPrefix(self, value: str):
        return self._set_field(self.ErrorOutputPrefix.__name__, value)

    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)

    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)
