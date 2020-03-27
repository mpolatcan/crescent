from crescent.core.constants import get_values


class DeliveryStreamType:
    DIRECT_PUT = "DirectPut"
    KINESIS_STREAM_AS_SOURCE = "KinesisStreamAsSource"

# ------------------------------------------


class CompressionFormat:
    class S3:
        GZIP = "GZIP"
        SNAPPY = "Snappy"
        UNCOMPRESSED = "UNCOMPRESSED"
        ZIP = "ZIP"

    class ExtendedS3:
        GZIP = "GZIP"
        SNAPPY = "Snappy"
        UNCOMPRESSED = "UNCOMPRESSED"
        ZIP = "ZIP"

    class OrcSerDe:
        NONE = "NONE"
        SNAPPY = "SNAPPY"
        ZLIB = "ZLIB"

    class ParquetSerDe:
        GZIP = "GZIP"
        SNAPPY = "SNAPPY"
        UNCOMPRESSED = "UNCOMPRESSED"

# ------------------------------------------


class S3BackupMode:
    class Splunk:
        ALL_EVENTS = "AllEvents"
        FAILED_EVENTS_ONLY = "FailedEventsOnly"

    class ExtendedS3:
        DISABLED = "Disabled"
        ENABLED = "Enabled"

    class Elasticsearch:
        ALL_DOCUMENTS = "AllDocuments"
        FAILED_DOCUMENTS_ONLY = "FailedDocumentsOnly"

# ------------------------------------------


class ElasticsearchDestinationIndexRotationPeriod:
    NO_ROTATION = "NoRotation"
    ONE_DAY = "OneDay"
    ONE_HOUR = "OneHour"
    ONE_MONTH = "OneMonth"
    ONE_WEEK = "OneWeek"

# --------------------------------------------------


class OrcSerDeFormatVersion:
    V0_11 = "V0_11"
    V0_12 = "V0_12"

# --------------------------------------------------


class ParquetSerDeWriterVersion:
    V1 = "V1"
    V2 = "V2"

# -------------------------------------------------


class ProcessorParameterName:
    BUFFER_INTERVAL_IN_SECONDS = "BufferIntervalInSeconds"
    BUFFER_SIZE_IN_MBS = "BufferSizeInMBs"
    LAMBDA_ARN = "LambdaArn"
    NUMBER_OF_RETRIES = "NumberOfRetries"
    ROLE_ARN = "RoleArn"

# -----------------------------------------------


class SplunkDestinationHECEndpointType:
    EVENT = "Event"
    RAW = "Raw"

# -----------------------------------------------


class ProcessorType:
    LAMBDA = "Lambda"


# -----------------------------------------------


class _Property:
    class CloudWatchLoggingOptions:
        ENABLED = "Enabled"
        LOG_GROUP_NAME = "LogGroupName"
        LOG_STREAM_NAME = "LogStreamName"

# ----------------------------------------------


class _RequiredProperties:
    class ElasticsearchDestinationConfiguration:
        BUFFERING_HINTS = "BufferingHints"
        DOMAIN_ARN = "DomainARN"
        INDEX_NAME = "IndexName"
        INDEX_ROTATION_PERIOD = "IndexRotationPeriod"
        RETRY_OPTIONS = "RetryOptions"
        ROLE_ARN = "RoleARN"
        S3_BACKUP_MODE = "S3BackupMode"
        S3_CONFIGURATION = "S3Configuration"
        TYPE_NAME = "TypeName"

    class ExtendedS3DestinationConfiguration:
        BUCKET_ARN = "BucketARN"
        BUFFERING_HINTS = "BufferingHints"
        COMPRESSION_FORMAT = "CompressionFormat"
        ROLE_ARN = "RoleARN"

    class KinesisStreamSourceConfiguration:
        KINESIS_STREAM_ARN = "KinesisStreamARN"
        ROLE_ARN = "RoleARN"

    class RedshiftDestinationConfiguration:
        CLUSTER_JDBC_URL = "ClusterJDBCURL"
        COPY_COMMAND = "CopyCommand"
        PASSWORD = "Password"
        ROLE_ARN = "RoleARN"
        S3_CONFIGURATION = "S3Configuration"
        USERNAME = "Username"

    class S3DestinationConfiguration:
        BUCKET_ARN = "BucketARN"
        BUFFERING_HINTS = "BufferingHints"
        COMPRESSION_FORMAT = "CompressionFormat"
        ROLE_ARN = "RoleARN"

    class SplunkDestinationConfiguration:
        HEC_ENDPOINT = "HECEndpoint"
        HEC_ENDPOINT_TYPE = "HECEndpointType"
        HEC_TOKEN = "HECToken"
        S3_CONFIGURATION = "S3Configuration"

    class BufferingHints:
        INTERVAL_IN_SECONDS = "IntervalInSeconds"
        SIZE_IN_MBS = "SizeInMBs"

    class CloudwatchLoggingOptions:
        ENABLED = "Enabled"
        LOG_GROUP_NAME = "LogGroupName"
        LOG_STREAM_NAME = "LogStreamName"

    class DataFormatConversionConfiguration:
        ENABLED = "Enabled"
        INPUT_FORMAT_CONFIGURATION = "InputFormatConfiguration"
        OUTPUT_FORMAT_CONFIGURATION = "OutputFormatConfiguration"
        SCHEMA_CONFIGURATION = "SchemaConfiguration"

    class ElasticsearchRetryOptions:
        DURATION_IN_SECONDS = "DurationInSeconds"

    class CopyCommand:
        DATA_TABLE_NAME = "DataTableName"

    class SplunkRetryOptions:
        DURATION_IN_SECONDS = "DurationInSeconds"

    class KmsEncryptionConfig:
        AWS_KMS_KEY_ARN = "AWSKMSKeyARN"

    class InputFormatConfiguration:
        DESERIALIZER = "Deserializer"

    class OutputFormatConfiguration:
        SERIALIZER = "Serializer"

    class SchemaConfiguration:
        CATALOG_ID = "CatalogId"
        DATABASE_NAME = "DatabaseName"
        REGION = "Region"
        ROLE_ARN = "RoleARN"
        TABLE_NAME = "TableName"
        VERSION_ID = "VersionId"


# -----------------------------------------------------------------


class ModelRequiredProperties:
    ELASTICSEARCH_DESTINATION_CONFIGURATION = get_values(_RequiredProperties.ElasticsearchDestinationConfiguration)
    EXTENDED_S3_DESTINATION_CONFIGURATION = get_values(_RequiredProperties.ExtendedS3DestinationConfiguration)
    KINESIS_STREAM_SOURCE_CONFIGURATION = get_values(_RequiredProperties.KinesisStreamSourceConfiguration)
    REDSHIFT_DESTINATION_CONFIGURATION = get_values(_RequiredProperties.RedshiftDestinationConfiguration)
    S3_DESTINATION_CONFIGURATION = get_values(_RequiredProperties.S3DestinationConfiguration)
    SPLUNK_DESTINATION_CONFIGURATION = get_values(_RequiredProperties.SplunkDestinationConfiguration)
    ELASTICSEARCH_RETRY_OPTIONS = get_values(_RequiredProperties.ElasticsearchRetryOptions)
    ELASTICSEARCH_BUFFERING_HINTS = get_values(_RequiredProperties.BufferingHints)
    DATA_FORMAT_CONVERSION_CONFIGURATION = get_values(_RequiredProperties.DataFormatConversionConfiguration)
    BUFFERING_HINTS = get_values(_RequiredProperties.BufferingHints)
    COPY_COMMAND = get_values(_RequiredProperties.CopyCommand)
    SPLUNK_RETRY_OPTIONS = get_values(_RequiredProperties.SplunkRetryOptions)
    SCHEMA_CONFIGURATION = get_values(_RequiredProperties.SchemaConfiguration)
    OUTPUT_FORMAT_CONFIGURATION = get_values(_RequiredProperties.OutputFormatConfiguration)
    INPUT_FORMAT_CONFIGURATION = get_values(_RequiredProperties.InputFormatConfiguration)
    KMS_ENCRYPTION_CONFIG = get_values(_RequiredProperties.KmsEncryptionConfig)

# ----------------------------------------------------------------


class AllowedValues:
    DELIVERY_STREAM_TYPE = get_values(DeliveryStreamType)
    ELASTICSEARCH_DESTINATION_CONFIGURATION_INDEX_ROTATION_PERIOD = get_values(ElasticsearchDestinationIndexRotationPeriod)
    ELASTICSEARCH_DESTINATION_CONFIGURATION_S3_BACKUP_MODE = get_values(S3BackupMode.Elasticsearch)
    EXTENDED_S3_DESTINATION_CONFIGURATION_COMPRESSION_FORMAT = get_values(CompressionFormat.ExtendedS3)
    EXTENDED_S3_DESTINATION_CONFIGURATION_S3_BACKUP_MODE = get_values(S3BackupMode.ExtendedS3)
    S3_DESTINATION_CONFIGURATION_COMPRESSION_FORMAT = get_values(CompressionFormat.S3)
    SPLUNK_DESTINATION_CONFIGURATION_HEC_ENDPOINT_TYPE = get_values(SplunkDestinationHECEndpointType)
    SPLUNK_DESTINATION_CONFIGURATION_S3_BACKUP_MODE = get_values(S3BackupMode.Splunk)
    ORC_SER_DE_COMPRESSION = get_values(CompressionFormat.OrcSerDe)
    ORC_SER_DE_FORMAT_VERSION = get_values(OrcSerDeFormatVersion)
    PARQUET_SER_DE_COMPRESSION = get_values(CompressionFormat.ParquetSerDe)
    PARQUET_SER_DE_WRITER_VERSION = get_values(ParquetSerDeWriterVersion)
    PROCESSOR_TYPE = get_values(ProcessorType)
    PROCESSOR_PARAMETER_NAME = get_values(ProcessorParameterName)


# ------------------------------------------------------------


class Conditions:
    CLOUDWATCH_LOGGING_OPTIONS = [
        (
            [_Property.CloudWatchLoggingOptions.ENABLED],
            lambda cw_l_opts:
                True if cw_l_opts.get(_Property.CloudWatchLoggingOptions.ENABLED, None) is False or (
                    cw_l_opts.get(_Property.CloudWatchLoggingOptions.ENABLED, None) is True and
                    cw_l_opts.get(_Property.CloudWatchLoggingOptions.LOG_GROUP_NAME, None) is not None and
                    cw_l_opts.get(_Property.CloudWatchLoggingOptions.LOG_STREAM_NAME, None) is not None
                ) else Exception("You need to specify property \"Enabled\" at least!") if cw_l_opts.get(_Property.CloudWatchLoggingOptions.ENABLED, None) is None
                else Exception("When property \"Enabled\" is True you need to specify \"LogStreamName\" and \"LogGroupName\" properties!")
        )
    ]
