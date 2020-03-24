from .delivery_stream import DeliveryStream
from .buffering_hints import BufferingHints
from .cloudwatch_logging_options import CloudWatchLoggingOptions
from .copy_command import CopyCommand
from .data_format_conversion_configuration import DataFormatConversionConfiguration
from .deserializer import Deserializer
from .elasticsearch_buffering_hints import ElasticsearchBufferingHints
from .elasticsearch_destination_configuration import ElasticsearchDestinationConfiguration
from .elasticsearch_retry_options import ElasticsearchRetryOptions
from .encryption_configuration import EncryptionConfiguration
from .extended_s3_destination_configuration import ExtendedS3DestinationConfiguration
from .hive_json_ser_de import HiveJsonSerDe
from .input_format_configuration import InputFormatConfiguration
from .kinesis_stream_source_configuration import KinesisStreamSourceConfiguration
from .lambda_processor import LambdaProcessor
from .kms_encryption_config import KMSEncryptionConfig
from .openx_json_ser_de import OpenXJsonSerDe
from .orc_ser_de import OrcSerDe
from .output_format_configuration import OutputFormatConfiguration
from .parquet_ser_de import ParquetSerDe
from .processing_configuration import ProcessingConfiguration
from .processor import Processor
from .processor_parameter import ProcessorParameter
from .redshift_destination_configuration import RedshiftDestinationConfiguration
from .s3_destination_configuration import S3DestinationConfiguration
from .schema_configuration import SchemaConfiguration
from .serializer import Serializer
from .splunk_destination_configuration import SplunkDestinationConfiguration
from .splunk_retry_options import SplunkRetryOptions
from .constants import (
    DeliveryStreamType,
    S3BackupMode,
    CompressionFormat,
    ProcessorParameterName,
    ProcessorType,
    OrcSerDeFormatVersion,
    ParquetSerDeWriterVersion,
    ElasticsearchDestinationIndexRotationPeriod,
    SplunkDestinationHECEndpointType
)


class FirehoseFactory:
    class __DeliveryStreamFactory:
        type = DeliveryStreamType
        s3_backup_mode = S3BackupMode
        compression = CompressionFormat
        orc_version = OrcSerDeFormatVersion
        parquet_version = ParquetSerDeWriterVersion
        es_ir_period = ElasticsearchDestinationIndexRotationPeriod
        processor_param = ProcessorParameterName
        processor_type = ProcessorType

        @staticmethod
        def DeliveryStream(id: str):
            return DeliveryStream(id)

        @staticmethod
        def BufferingHints():
            return BufferingHints()

        @staticmethod
        def CloudWatchLoggingOptions():
            return CloudWatchLoggingOptions()

        @staticmethod
        def CopyCommand():
            return CopyCommand()

        @staticmethod
        def DataFormatConversionConfiguration():
            return DataFormatConversionConfiguration()

        @staticmethod
        def Deserializer():
            return Deserializer()

        @staticmethod
        def ElasticsearchBufferingHints():
            return ElasticsearchBufferingHints()

        @staticmethod
        def ElasticsearchDestinationConfiguration():
            return ElasticsearchDestinationConfiguration()

        @staticmethod
        def ElasticsearchRetryOptions():
            return ElasticsearchRetryOptions()

        @staticmethod
        def EncryptionConfiguration():
            return EncryptionConfiguration()

        @staticmethod
        def ExtendedS3DestinationConfiguration():
            return ExtendedS3DestinationConfiguration()

        @staticmethod
        def HiveJsonSerDe():
            return HiveJsonSerDe()

        @staticmethod
        def InputFormatConfiguration():
            return InputFormatConfiguration()

        @staticmethod
        def KinesisStreamSourceConfiguration():
            return KinesisStreamSourceConfiguration()

        @staticmethod
        def KMSEncryptionConfig():
            return KMSEncryptionConfig()

        @staticmethod
        def OpenXJsonSerDe():
            return OpenXJsonSerDe()

        @staticmethod
        def OrcSerDe():
            return OrcSerDe()

        @staticmethod
        def OutputFormatConfiguration():
            return OutputFormatConfiguration()

        @staticmethod
        def ParquetSerDe():
            return ParquetSerDe()

        @staticmethod
        def ProcessingConfiguration():
            return ProcessingConfiguration()

        @staticmethod
        def Processor():
            return Processor()

        @staticmethod
        def LambdaProcessor():
            return LambdaProcessor()

        @staticmethod
        def ProcessorParameter():
            return ProcessorParameter()

        @staticmethod
        def RedshiftDestinationConfiguration():
            return RedshiftDestinationConfiguration()

        @staticmethod
        def S3DestinationConfiguration():
            return S3DestinationConfiguration()

        @staticmethod
        def SchemaConfiguration():
            return SchemaConfiguration()

        @staticmethod
        def Serializer():
            return Serializer()

        @staticmethod
        def SplunkDestinationConfiguration():
            return SplunkDestinationConfiguration()

        @staticmethod
        def SplunkRetryOptions():
            return SplunkRetryOptions()

    delivery_stream = __DeliveryStreamFactory


firehose = FirehoseFactory
firehose_delivery_stream = firehose.delivery_stream


__all__ = [
    "firehose",
    "firehose_delivery_stream"
]