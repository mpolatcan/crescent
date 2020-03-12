from pyformation import PyformationModel
from .buffering_hints import BufferingHints
from .cloudwatch_logging_options import CloudwatchLoggingOptions
from .data_format_conversion_configuration import DataFormatConversionConfiguration
from .encryption_configuration import EncryptionConfiguration
from .processing_configuration import ProcessingConfiguration
from .s3_destination_configuration import S3DestinationConfiguration


class ExtendedS3DestinationConfiguration(PyformationModel):
    def BucketARN(self, value: str):
        return self._set_field(self.BucketARN.__name__, value)

    def BufferingHints(self, value: BufferingHints):
        return self._set_field(self.BufferingHints.__name__, value.__to_dict__())

    def CloudwatchLoggingOptions(self, value: CloudwatchLoggingOptions):
        return self._set_field(self.CloudwatchLoggingOptions.__name__, value.__to_dict__())

    def CompressionFormat(self, value: str):
        return self._set_field(self.CompressionFormat.__name__, value)

    def DataFormatConversionConfiguration(self, value: DataFormatConversionConfiguration):
        return self._set_field(self.DataFormatConversionConfiguration.__name__, value.__to_dict__())

    def EncryptionConfiguration(self, value: EncryptionConfiguration):
        return self._set_field(self.EncryptionConfiguration.__name__, value.__to_dict__())

    def ErrorOutputPrefix(self, value: str):
        return self._set_field(self.ErrorOutputPrefix.__name__, value)

    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)

    def ProcessingConfiguration(self, value: ProcessingConfiguration):
        return self._set_field(self.ProcessingConfiguration.__name__, value.__to_dict__())

    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)

    def S3BackupConfiguration(self, value: S3DestinationConfiguration):
        return self._set_field(self.S3BackupConfiguration.__name__, value.__to_dict__())

    def S3BackupMode(self, value: str):
        return self._set_field(self.S3BackupMode.__name__, value)
