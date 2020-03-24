class DeliveryStreamType:
    DIRECT_PUT = "DirectPut"
    KINESIS_STREAM_AS_SOURCE = "KinesisStreamAsSource"

##########################################


class CompressionFormat:
    class __CompressionFormatS3:
        GZIP = "GZIP"
        SNAPPY = "Snappy"
        UNCOMPRESSED = "UNCOMPRESSED"
        ZIP = "ZIP"

    class __CompressionFormatExtendedS3:
        GZIP = "GZIP"
        SNAPPY = "Snappy"
        UNCOMPRESSED = "UNCOMPRESSED"
        ZIP = "ZIP"

    class __CompressionFormatOrc:
        NONE = "NONE"
        SNAPPY = "SNAPPY"
        ZLIB = "ZLIB"

    class __CompressionFormatParquet:
        GZIP = "GZIP"
        SNAPPY = "SNAPPY"
        UNCOMPRESSED = "UNCOMPRESSED"

    s3 = __CompressionFormatS3
    ext_s3 = __CompressionFormatExtendedS3
    orc = __CompressionFormatOrc
    parquet = __CompressionFormatParquet

##########################################


class S3BackupMode:
    class __S3BackupModeSplunk:
        ALL_EVENTS = "AllEvents"
        FAILED_EVENTS_ONLY = "FailedEventsOnly"

    class __S3BackupModeExtendedS3:
        DISABLED = "Disabled"
        ENABLED = "Enabled"

    class __S3BackupModeElasticsearch:
        ALL_DOCUMENTS = "AllDocuments"
        FAILED_DOCUMENTS_ONLY = "FailedDocumentsOnly"

    splunk = __S3BackupModeSplunk
    ext_s3 = __S3BackupModeExtendedS3
    es = __S3BackupModeElasticsearch

##########################################


class ElasticsearchDestinationIndexRotationPeriod:
    NO_ROTATION = "NoRotation"
    ONE_DAY = "OneDay"
    ONE_HOUR = "OneHour"
    ONE_MONTH = "OneMonth"
    ONE_WEEK = "OneWeek"

##########################################


class OrcSerDeFormatVersion:
    V0_11 = "V0_11"
    V0_12 = "V0_12"

##########################################


class ParquetSerDeWriterVersion:
    V1 = "V1"
    V2 = "V2"

##########################################


class ProcessorParameterName:
    BUFFER_INTERVAL_IN_SECONDS = "BufferIntervalInSeconds"
    BUFFER_SIZE_IN_MBS = "BufferSizeInMBs"
    LAMBDA_ARN = "LambdaArn"
    NUMBER_OF_RETRIES = "NumberOfRetries"
    ROLE_ARN = "RoleArn"

##########################################


class SplunkDestinationHECEndpointType:
    EVENT = "Event"
    RAW = "Raw"

##########################################


class ProcessorType:
    LAMBDA = "Lambda"

##########################################


class Property:
    ELASTICSEARCH_DESTINATION_CONFIGURATION_BUFFERING_HINTS = "BufferingHints"
    ELASTICSEARCH_DESTINATION_CONFIGURATION_DOMAIN_ARN = "DomainARN"
    ELASTICSEARCH_DESTINATION_CONFIGURATION_INDEX_NAME = "IndexName"
    ELASTICSEARCH_DESTINATION_CONFIGURATION_INDEX_ROTATION_PERIOD = "IndexRotationPeriod"
    ELASTICSEARCH_DESTINATION_CONFIGURATION_RETRY_OPTIONS = "RetryOptions"
    ELASTICSEARCH_DESTINATION_CONFIGURATION_ROLE_ARN = "RoleARN"
    ELASTICSEARCH_DESTINATION_CONFIGURATION_S3_BACKUP_MODE = "S3BackupMode"
    ELASTICSEARCH_DESTINATION_CONFIGURATION_S3_CONFIGURATION = "S3Configuration"
    ELASTICSEARCH_DESTINATION_CONFIGURATION_TYPE_NAME = "TypeName"
    EXTENDED_S3_DESTINATION_CONFIGURATION_BUCKET_ARN = "BucketARN"
    EXTENDED_S3_DESTINATION_CONFIGURATION_BUFFERING_HINTS = "BufferingHints"
    EXTENDED_S3_DESTINATION_CONFIGURATION_COMPRESSION_FORMAT = "CompressionFormat"
    EXTENDED_S3_DESTINATION_CONFIGURATION_ROLE_ARN = "RoleARN"
    KINESIS_STREAM_SOURCE_CONFIGURATION_KINESIS_STREAM_ARN = "KinesisStreamARN"
    KINESIS_STREAM_SOURCE_CONFIGURATION_ROLE_ARN = "RoleARN"
    REDSHIFT_DESTINATION_CONFIGURATION_CLUSTER_JDBC_URL = "ClusterJDBCURL"
    REDSHIFT_DESTINATION_CONFIGURATION_COPY_COMMAND = "CopyCommand"
    REDSHIFT_DESTINATION_CONFIGURATION_PASSWORD = "Password"
    REDSHIFT_DESTINATION_CONFIGURATION_ROLE_ARN = "RoleARN"
    REDSHIFT_DESTINATION_CONFIGURATION_S3_CONFIGURATION = "S3Configuration"
    REDSHIFT_DESTINATION_CONFIGURATION_USERNAME = "Username"
    S3_DESTINATION_CONFIGURATION_BUCKET_ARN = "BucketARN"
    S3_DESTINATION_CONFIGURATION_BUFFERING_HINTS = "BufferingHints"
    S3_DESTINATION_CONFIGURATION_COMPRESSION_FORMAT = "CompressionFormat"
    S3_DESTINATION_CONFIGURATION_ROLE_ARN = "RoleARN"
    SPLUNK_DESTINATION_CONFIGURATION_HEC_ENDPOINT = "HECEndpoint"
    SPLUNK_DESTINATION_CONFIGURATION_HEC_ENDPOINT_TYPE = "HECEndpointType"
    SPLUNK_DESTINATION_CONFIGURATION_HEC_TOKEN = "HECToken"
    SPLUNK_DESTINATION_CONFIGURATION_S3_CONFIGURATION = "S3Configuration"
    BUFFERING_HINTS_INTERVAL_IN_SECONDS = "IntervalInSeconds"
    BUFFERING_HINTS_SIZE_IN_MBS = "SizeInMBs"
    CLOUDWATCH_LOGGING_OPTIONS = "CloudWatchLoggingOptions"
    CLOUDWATCH_LOGGING_OPTIONS_ENABLED = "Enabled"
    CLOUDWATCH_LOGGING_OPTIONS_LOG_GROUP_NAME = "LogGroupName"
    CLOUDWATCH_LOGGING_OPTIONS_LOG_STREAM_NAME = "LogStreamName"
    DATA_FORMAT_CONVERSION_CONFIGURATION = "DataFormatConversionConfiguration"
    DATA_FORMAT_CONVERSION_CONFIGURATION_ENABLED = "Enabled"
    DATA_FORMAT_CONVERSION_CONFIGURATION_INPUT_FORMAT_CONFIGURATION = "InputFormatConfiguration"
    DATA_FORMAT_CONVERSION_CONFIGURATION_OUTPUT_FORMAT_CONFIGURATION = "OutputFormatConfiguration"
    DATA_FORMAT_CONVERSION_CONFIGURATION_SCHEMA_CONFIGURATION = "SchemaConfiguration"
    ELASTICSEARCH_RETRY_OPTIONS_DURATION_IN_SECONDS = "DurationInSeconds"
    COPY_COMMAND_DATA_TABLE_NAME = "DataTableName"
    SPLUNK_RETRY_OPTIONS_DURATION_IN_SECONDS = "DurationInSeconds"
    KMS_ENCRYPTION_CONFIG_AWS_KMS_KEY_ARN = "AWSKMSKeyARN"
    INPUT_FORMAT_CONFIGURATION_DESERIALIZER = "Deserializer"
    OUTPUT_FORMAT_CONFIGURATION_SERIALIZER = "Serializer"
    SCHEMA_CONFIGURATION_CATALOG_ID = "CatalogId"
    SCHEMA_CONFIGURATION_DATABASE_NAME = "DatabaseName"
    SCHEMA_CONFIGURATION_REGION = "Region"
    SCHEMA_CONFIGURATION_ROLE_ARN = "RoleARN"
    SCHEMA_CONFIGURATION_TABLE_NAME = "TableName"
    SCHEMA_CONFIGURATION_VERSION_ID = "VersionId"

# -----------------------------------------------------------


class RequiredProperties:
    ELASTICSEARCH_DESTINATION_CONFIGURATION = [
        Property.ELASTICSEARCH_DESTINATION_CONFIGURATION_BUFFERING_HINTS,
        Property.ELASTICSEARCH_DESTINATION_CONFIGURATION_DOMAIN_ARN,
        Property.ELASTICSEARCH_DESTINATION_CONFIGURATION_INDEX_NAME,
        Property.ELASTICSEARCH_DESTINATION_CONFIGURATION_INDEX_ROTATION_PERIOD,
        Property.ELASTICSEARCH_DESTINATION_CONFIGURATION_RETRY_OPTIONS,
        Property.ELASTICSEARCH_DESTINATION_CONFIGURATION_ROLE_ARN,
        Property.ELASTICSEARCH_DESTINATION_CONFIGURATION_S3_BACKUP_MODE,
        Property.ELASTICSEARCH_DESTINATION_CONFIGURATION_S3_CONFIGURATION,
        Property.ELASTICSEARCH_DESTINATION_CONFIGURATION_TYPE_NAME
    ]
    EXTENDED_S3_DESTINATION_CONFIGURATION = [
        Property.EXTENDED_S3_DESTINATION_CONFIGURATION_BUCKET_ARN,
        Property.EXTENDED_S3_DESTINATION_CONFIGURATION_BUFFERING_HINTS,
        Property.EXTENDED_S3_DESTINATION_CONFIGURATION_COMPRESSION_FORMAT,
        Property.EXTENDED_S3_DESTINATION_CONFIGURATION_ROLE_ARN
    ]
    KINESIS_STREAM_SOURCE_CONFIGURATION = [
        Property.KINESIS_STREAM_SOURCE_CONFIGURATION_KINESIS_STREAM_ARN,
        Property.KINESIS_STREAM_SOURCE_CONFIGURATION_ROLE_ARN
    ]
    REDSHIFT_DESTINATION_CONFIGURATION = [
        Property.REDSHIFT_DESTINATION_CONFIGURATION_CLUSTER_JDBC_URL,
        Property.REDSHIFT_DESTINATION_CONFIGURATION_COPY_COMMAND,
        Property.REDSHIFT_DESTINATION_CONFIGURATION_PASSWORD,
        Property.REDSHIFT_DESTINATION_CONFIGURATION_ROLE_ARN,
        Property.REDSHIFT_DESTINATION_CONFIGURATION_S3_CONFIGURATION,
        Property.REDSHIFT_DESTINATION_CONFIGURATION_USERNAME
    ]
    S3_DESTINATION_CONFIGURATION = [
        Property.S3_DESTINATION_CONFIGURATION_BUCKET_ARN,
        Property.S3_DESTINATION_CONFIGURATION_BUFFERING_HINTS,
        Property.S3_DESTINATION_CONFIGURATION_COMPRESSION_FORMAT,
        Property.S3_DESTINATION_CONFIGURATION_ROLE_ARN
    ]
    SPLUNK_DESTINATION_CONFIGURATION = [
        Property.SPLUNK_DESTINATION_CONFIGURATION_HEC_ENDPOINT,
        Property.SPLUNK_DESTINATION_CONFIGURATION_HEC_ENDPOINT_TYPE,
        Property.SPLUNK_DESTINATION_CONFIGURATION_HEC_TOKEN,
        Property.SPLUNK_DESTINATION_CONFIGURATION_S3_CONFIGURATION
    ]
    ELASTICSEARCH_RETRY_OPTIONS = [
        Property.ELASTICSEARCH_RETRY_OPTIONS_DURATION_IN_SECONDS
    ]
    ELASTICSEARCH_BUFFERING_HINTS = [
        Property.BUFFERING_HINTS_INTERVAL_IN_SECONDS,
        Property.BUFFERING_HINTS_SIZE_IN_MBS
    ]
    DATA_FORMAT_CONVERSION_CONFIGURATION = [
        Property.DATA_FORMAT_CONVERSION_CONFIGURATION_ENABLED,
        Property.DATA_FORMAT_CONVERSION_CONFIGURATION_INPUT_FORMAT_CONFIGURATION,
        Property.DATA_FORMAT_CONVERSION_CONFIGURATION_OUTPUT_FORMAT_CONFIGURATION,
        Property.DATA_FORMAT_CONVERSION_CONFIGURATION_SCHEMA_CONFIGURATION
    ]
    BUFFERING_HINTS = [
        Property.BUFFERING_HINTS_SIZE_IN_MBS,
        Property.BUFFERING_HINTS_INTERVAL_IN_SECONDS
    ]
    COPY_COMMAND = [
        Property.COPY_COMMAND_DATA_TABLE_NAME
    ]
    SPLUNK_RETRY_OPTIONS = [
        Property.SPLUNK_RETRY_OPTIONS_DURATION_IN_SECONDS
    ]
    SCHEMA_CONFIGURATION = [
        Property.SCHEMA_CONFIGURATION_CATALOG_ID,
        Property.SCHEMA_CONFIGURATION_DATABASE_NAME,
        Property.SCHEMA_CONFIGURATION_REGION,
        Property.SCHEMA_CONFIGURATION_ROLE_ARN,
        Property.SCHEMA_CONFIGURATION_TABLE_NAME,
        Property.SCHEMA_CONFIGURATION_VERSION_ID
    ]
    OUTPUT_FORMAT_CONFIGURATION = [
        Property.OUTPUT_FORMAT_CONFIGURATION_SERIALIZER
    ]
    INPUT_FORMAT_CONFIGURATION = [
        Property.INPUT_FORMAT_CONFIGURATION_DESERIALIZER
    ]
    KMS_ENCRYPTION_CONFIG = [
        Property.KMS_ENCRYPTION_CONFIG_AWS_KMS_KEY_ARN
    ]

# -----------------------------------------------------------


class Conditions:
    CLOUDWATCH_LOGGING_OPTIONS = [
        (
            [Property.CLOUDWATCH_LOGGING_OPTIONS],
            lambda cw_l_opts:
                True if cw_l_opts.get(Property.CLOUDWATCH_LOGGING_OPTIONS_ENABLED, None) is False or (
                    cw_l_opts.get(Property.CLOUDWATCH_LOGGING_OPTIONS_ENABLED, None) is True and
                    cw_l_opts.get(Property.CLOUDWATCH_LOGGING_OPTIONS_LOG_GROUP_NAME, None) is not None and
                    cw_l_opts.get(Property.CLOUDWATCH_LOGGING_OPTIONS_LOG_STREAM_NAME, None) is not None
                ) else Exception("You need to specify property \"Enabled\" at least!") if cw_l_opts.get(Property.CLOUDWATCH_LOGGING_OPTIONS_ENABLED, None) is None
                else Exception("When property \"Enabled\" is True you need to specify \"LogStreamName\" and \"LogGroupName\" properties!")
        )
    ]

# -----------------------------------------------------------


class AllowedValues:
    DELIVERY_STREAM_TYPE = [
        DeliveryStreamType.DIRECT_PUT,
        DeliveryStreamType.KINESIS_STREAM_AS_SOURCE
    ]
    ELASTICSEARCH_DESTINATION_CONFIGURATION_INDEX_ROTATION_PERIOD = [
        ElasticsearchDestinationIndexRotationPeriod.NO_ROTATION,
        ElasticsearchDestinationIndexRotationPeriod.ONE_DAY,
        ElasticsearchDestinationIndexRotationPeriod.ONE_HOUR,
        ElasticsearchDestinationIndexRotationPeriod.ONE_MONTH,
        ElasticsearchDestinationIndexRotationPeriod.ONE_WEEK
    ]
    ELASTICSEARCH_DESTINATION_CONFIGURATION_S3_BACKUP_MODE = [
        S3BackupMode.es.ALL_DOCUMENTS,
        S3BackupMode.es.FAILED_DOCUMENTS_ONLY
    ]
    EXTENDED_S3_DESTINATION_CONFIGURATION_COMPRESSION_FORMAT = [
        CompressionFormat.ext_s3.GZIP,
        CompressionFormat.ext_s3.SNAPPY,
        CompressionFormat.ext_s3.UNCOMPRESSED,
        CompressionFormat.ext_s3.ZIP
    ]
    EXTENDED_S3_DESTINATION_CONFIGURATION_S3_BACKUP_MODE = [
        S3BackupMode.ext_s3.ENABLED,
        S3BackupMode.ext_s3.DISABLED
    ]
    S3_DESTINATION_CONFIGURATION_COMPRESSION_FORMAT = [
        CompressionFormat.s3.GZIP,
        CompressionFormat.s3.SNAPPY,
        CompressionFormat.s3.UNCOMPRESSED,
        CompressionFormat.s3.ZIP
    ]
    SPLUNK_DESTINATION_CONFIGURATION_HEC_ENDPOINT_TYPE = [
        SplunkDestinationHECEndpointType.EVENT,
        SplunkDestinationHECEndpointType.RAW
    ]
    SPLUNK_DESTINATION_CONFIGURATION_S3_BACKUP_MODE = [
        S3BackupMode.splunk.ALL_EVENTS,
        S3BackupMode.splunk.FAILED_EVENTS_ONLY
    ]
    ORC_SER_DE_COMPRESSION = [
        CompressionFormat.orc.NONE,
        CompressionFormat.orc.SNAPPY,
        CompressionFormat.orc.ZLIB
    ]
    ORC_SER_DE_FORMAT_VERSION = [
        OrcSerDeFormatVersion.V0_11,
        OrcSerDeFormatVersion.V0_12
    ]
    PARQUET_SER_DE_COMPRESSION = [
        CompressionFormat.parquet.GZIP,
        CompressionFormat.parquet.SNAPPY,
        CompressionFormat.parquet.UNCOMPRESSED
    ]
    PARQUET_SER_DE_WRITER_VERSION = [
        ParquetSerDeWriterVersion.V1,
        ParquetSerDeWriterVersion.V2
    ]
    PROCESSOR_TYPE = [
        ProcessorType.LAMBDA
    ]
    PROCESSOR_PARAMETER_NAME = [
        ProcessorParameterName.BUFFER_INTERVAL_IN_SECONDS,
        ProcessorParameterName.BUFFER_SIZE_IN_MBS,
        ProcessorParameterName.LAMBDA_ARN,
        ProcessorParameterName.NUMBER_OF_RETRIES,
        ProcessorParameterName.ROLE_ARN
    ]