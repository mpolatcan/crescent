from crescent.core import Model, Validator
from .buffering_hints import BufferingHints
from .cloudwatch_logging_options import CloudWatchLoggingOptions
from .data_format_conversion_configuration import DataFormatConversionConfiguration
from .encryption_configuration import EncryptionConfiguration
from .processing_configuration import ProcessingConfiguration
from .s3_destination_configuration import S3DestinationConfiguration
from .constants import ModelRequiredProperties, AllowedValues, Conditions


class ExtendedS3DestinationConfiguration(Model):
    @Validator.validate(type=str, min_length=1, max_length=2048, pattern=r"arn:.*")
    def BucketARN(self, value: str):
        return self._set_field(self.BucketARN.__name__, value)

    @Validator.validate(type=BufferingHints, required_properties=ModelRequiredProperties.BUFFERING_HINTS)
    def BufferingHints(self, value: BufferingHints):
        return self._set_field(self.BufferingHints.__name__, value.__to_dict__())

    @Validator.validate(type=CloudWatchLoggingOptions, conditions=Conditions.CLOUDWATCH_LOGGING_OPTIONS)
    def CloudWatchLoggingOptions(self, value: CloudWatchLoggingOptions):
        return self._set_field(self.CloudWatchLoggingOptions.__name__, value.__to_dict__())

    @Validator.validate(type=str, allowed_values=AllowedValues.EXTENDED_S3_DESTINATION_CONFIGURATION_COMPRESSION_FORMAT)
    def CompressionFormat(self, value: str):
        return self._set_field(self.CompressionFormat.__name__, value)

    @Validator.validate(type=DataFormatConversionConfiguration, required_properties=ModelRequiredProperties.DATA_FORMAT_CONVERSION_CONFIGURATION)
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

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"arn:.*")
    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)

    @Validator.validate(type=S3DestinationConfiguration, required_properties=ModelRequiredProperties.S3_DESTINATION_CONFIGURATION)
    def S3BackupConfiguration(self, value: S3DestinationConfiguration):
        return self._set_field(self.S3BackupConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=str, allowed_values=AllowedValues.EXTENDED_S3_DESTINATION_CONFIGURATION_S3_BACKUP_MODE)
    def S3BackupMode(self, value: str):
        return self._set_field(self.S3BackupMode.__name__, value)
