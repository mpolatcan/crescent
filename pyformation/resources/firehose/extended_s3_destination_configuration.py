from pyformation.core import Model, Validator
from .buffering_hints import BufferingHints
from .cloudwatch_logging_options import CloudwatchLoggingOptions
from .data_format_conversion_configuration import DataFormatConversionConfiguration
from .encryption_configuration import EncryptionConfiguration
from .processing_configuration import ProcessingConfiguration
from .s3_destination_configuration import S3DestinationConfiguration


class ExtendedS3DestinationConfiguration(Model):
    @Validator.validate(type=str)
    def BucketARN(self, value: str):
        return self._set_field(self.BucketARN.__name__, value)

    @Validator.validate(type=BufferingHints)
    def BufferingHints(self, value: BufferingHints):
        return self._set_field(self.BufferingHints.__name__, value.__to_dict__())

    @Validator.validate(type=CloudwatchLoggingOptions)
    def CloudwatchLoggingOptions(self, value: CloudwatchLoggingOptions):
        return self._set_field(self.CloudwatchLoggingOptions.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def CompressionFormat(self, value: str):
        return self._set_field(self.CompressionFormat.__name__, value)

    @Validator.validate(type=DataFormatConversionConfiguration)
    def DataFormatConversionConfiguration(self, value: DataFormatConversionConfiguration):
        return self._set_field(self.DataFormatConversionConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=EncryptionConfiguration)
    def EncryptionConfiguration(self, value: EncryptionConfiguration):
        return self._set_field(self.EncryptionConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def ErrorOutputPrefix(self, value: str):
        return self._set_field(self.ErrorOutputPrefix.__name__, value)

    @Validator.validate(type=str)
    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)

    @Validator.validate(type=ProcessingConfiguration)
    def ProcessingConfiguration(self, value: ProcessingConfiguration):
        return self._set_field(self.ProcessingConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)

    @Validator.validate(type=S3DestinationConfiguration)
    def S3BackupConfiguration(self, value: S3DestinationConfiguration):
        return self._set_field(self.S3BackupConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def S3BackupMode(self, value: str):
        return self._set_field(self.S3BackupMode.__name__, value)
