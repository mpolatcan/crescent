class StatusEnabledSuspended:
    ENABLED = "Enabled"
    SUSPENDED = "Suspended"

##########################################


class StatusEnabledDisabled:
    ENABLED = "Enabled"
    DISABLED = "Disabled"

##########################################


class AccessControlTranslationOwner:
    DESTINATION = "Destination"

##########################################


class HttpMethod:
    GET = "GET"
    PUT = "PUT"
    HEAD = "HEAD"
    POST = "POST"
    DELETE = "DELETE"

##########################################


class DataExportOutputSchemaVersion:
    V_1 = "V_1"

##########################################


class DefaultRetentionMode:
    COMPLIANCE = "COMPLIANCE"
    GOVERNANCE = "GOVERNANCE"

##########################################


class DestinationFormat:
    CSV = "CSV"

##########################################


class FilterRuleName:
    PREFIX = "prefix"
    SUFFIX = "suffix"

##########################################


class InventoryConfigurationIncludedObjectVersions:
    ALL = "All"
    CURRENT = "Current"

##########################################


class InventoryConfigurationScheduleFrequency:
    DAILY = "Daily"
    WEEKLY = "Weekly"

##########################################


class StorageClass:
    DEEP_ARCHIVE = "DEEP_ARCHIVE"
    GLACIER = "GLACIER"
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    ONEZONE_IA = "ONEZONE_IA"
    STANDARD = "STANDARD"
    STANDARD_IA = "STANDARD_IA"
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"

##########################################


class Protocol:
    HTTP = "http"
    HTTPS = "https"

##########################################


class SSEAlgorithm:
    AES_256 = "AES256"
    AWS_KMS = "aws:kms"

##########################################


class Property:
    ACCELERATE_CONFIGURATION_ACCELERATION_STATUS = "AccelerationStatus"
    ANALYTICS_CONFIGURATION_ID = "Id"
    ANALYTICS_CONFIGURATION_STORAGE_CLASS_ANALYSIS = "StorageClassAnalysis"
    BUCKET_ENCRYPTION_SERVER_SIDE_ENCRYPTION_CONFIGURATION = "ServerSideEncryptionConfiguration"
    CORS_CONFIGURATION_CORS_RULES = "CorsRules"
    INVENTORY_CONFIGURATION_DESTINATION = "Destination"
    INVENTORY_CONFIGURATION_ENABLED = "Enabled"
    INVENTORY_CONFIGURATION_ID = "Id"
    INVENTORY_CONFIGURATION_DESTINATION_INCLUDED_OBJECT_VERSIONS = "IncludedObjectVersions"
    INVENTORY_CONFIGURATION_DESTINATION_SCHEDULE_FREQUENCY = "ScheduleFrequency"
    LIFECYCLE_CONFIGURATION_RULES = "Rules"
    METRICS_CONFIGURATION_ID = "Id"
    REPLICATION_CONFIGURATION_ROLE = "Role"
    REPLICATION_CONFIGURATION_RULES = "Rules"
    VERSIONING_CONFIGURATION_STATUS = "Status"
    DATA_EXPORT_DESTINATION = "Destination"
    DATA_EXPORT_OUTPUT_SCHEMA_VERSION = "OutputSchemaVersion"
    DESTINATION_BUCKET_ARN = "BucketArn"
    DESTINATION_BUCKET_FORMAT = "Format"
    TAG_FILTER_KEY = "Key"
    TAG_FILTER_VALUE = "Value"
    SERVER_SIDE_ENCRYPTION_BY_DEFAULT_SSE_ALGORITHM = "SSEAlgorithm"
    CORS_RULE_ALLOWED_METHODS = "AllowedMethods"
    CORS_RULE_ALLOWED_ORIGINS = "AllowedOrigins"
    RULE_STATUS = "Status"
    RULE_ABORT_INCOMPLETE_MULTIPART_UPLOAD = "AbortIncompleteMultipartUpload"
    RULE_EXPIRATION_DATE = "ExpirationDate"
    RULE_EXPIRATION_IN_DAYS = "ExpirationInDays"
    RULE_NONCURRENT_VERSION_EXPIRATION_IN_DAYS = "NoncurrentVersionExpirationInDays"
    RULE_NONCURRENT_VERSION_TRANSITION = "NoncurrentVersionTransition"
    RULE_NONCURRENT_VERSION_TRANSITIONS = "NoncurrentVersionTransitions"
    RULE_TRANSITION = "Transition"
    RULE_TRANSITIONS = "Transitions"
    NONCURRENT_VERSION_TRANSITION_STORAGE_CLASS = "StorageClass"
    NONCURRENT_VERSION_TRANSITION_TRANSITION_IN_DAYS = "TransitionInDays"
    TRANSITION_STORAGE_CLASS = "StorageClass"
    ABORT_INCOMPLETE_MULTIPART_UPLOAD_DAYS_AFTER_INITIATION = "DaysAfterInitiation"
    LAMBDA_CONFIGURATION_EVENT = "Event"
    LAMBDA_CONFIGURATION_FUNCTION = "Function"
    QUEUE_CONFIGURATION_EVENT = "Event"
    QUEUE_CONFIGURATION_QUEUE = "Queue"
    TOPIC_CONFIGURATION_EVENT = "Event"
    TOPIC_CONFIGURATION_TOPIC = "Topic"
    NOTIFICATION_FILTER_S3_KEY = "S3Key"
    S3_KEY_FILTER_RULES = "Rules"
    FILTER_RULE_NAME = "Name"
    FILTER_RULE_VALUE = "Value"
    REPLICATION_RULE_DESTINATION = "Destination"
    REPLICATION_RULE_PREFIX = "Prefix"
    REPLICATION_RULE_STATUS = "Status"
    REPLICATION_DESTINATION_BUCKET = "Bucket"
    ACCESS_CONTROL_TRANSLATION_OWNER = "Owner"
    ENCRYPTION_CONFIGURATION_REPLICA_KMS_KEY_ID = "ReplicaKmsKeyID"
    SOURCE_SELECTION_CRITERIA_SSE_KMS_ENCRYPTED_OBJECTS = "SseKmsEncryptedObjects"
    SSE_KMS_ENCRYPTED_OBJECTS_STATUS = "Status"
    REDIRECT_ALL_REQUEST_TO_HOST_NAME = "HostName"
    REDIRECT_ALL_REQUEST_TO_PROTOCOL = "Protocol"
    ROUTING_RULE_REDIRECT_RULE = "RedirectRule"
    ROUTING_RULE_CONDITON = "RoutingRuleCondition"
    ROUTING_RULE_CONDITION_HTTP_ERROR_CODE_RETURNED_EQUALS = "HttpErrorCodeReturnedEquals"
    ROUTING_RULE_CONDITION_KEY_PREFIX_EQUALS = "KeyPrefixEquals"
    REDIRECT_RULE = "RedirectRule"
    REDIRECT_RULE_REPLACE_KEY_WITH = "ReplaceKeyWith"
    REDIRECT_RULE_REPLACE_KEY_PREFIX_WITH = "ReplaceKeyPrefixWith"

##########################################


class RequiredProperties:
    ACCELERATE_CONFIGURATION = [
        Property.ACCELERATE_CONFIGURATION_ACCELERATION_STATUS
    ]
    ANALYTICS_CONFIGURATION = [
        Property.ANALYTICS_CONFIGURATION_ID,
        Property.ANALYTICS_CONFIGURATION_STORAGE_CLASS_ANALYSIS
    ]
    BUCKET_ENCRYPTION = [
        Property.BUCKET_ENCRYPTION_SERVER_SIDE_ENCRYPTION_CONFIGURATION
    ]
    CORS_CONFIGURATION = [
        Property.CORS_CONFIGURATION_CORS_RULES
    ]
    INVENTORY_CONFIGURATION = [
        Property.INVENTORY_CONFIGURATION_DESTINATION,
        Property.INVENTORY_CONFIGURATION_DESTINATION_INCLUDED_OBJECT_VERSIONS,
        Property.INVENTORY_CONFIGURATION_ID,
        Property.INVENTORY_CONFIGURATION_ENABLED,
        Property.INVENTORY_CONFIGURATION_DESTINATION_SCHEDULE_FREQUENCY
    ]
    LIFECYCLE_CONFIGURATION = [
        Property.LIFECYCLE_CONFIGURATION_RULES
    ]
    METRICS_CONFIGURATION = [
        Property.METRICS_CONFIGURATION_ID
    ]
    REPLICATION_CONFIGURATION = [
        Property.REPLICATION_CONFIGURATION_ROLE,
        Property.REPLICATION_CONFIGURATION_RULES
    ]
    VERSIONING_CONFIGURATION = [
        Property.VERSIONING_CONFIGURATION_STATUS
    ]
    DATA_EXPORT = [
        Property.DATA_EXPORT_DESTINATION,
        Property.DATA_EXPORT_OUTPUT_SCHEMA_VERSION
    ]
    DESTINATION = [
        Property.DESTINATION_BUCKET_ARN,
        Property.DESTINATION_BUCKET_FORMAT
    ]
    TAG_FILTER = [
        Property.TAG_FILTER_KEY,
        Property.TAG_FILTER_VALUE
    ]
    SERVER_SIDE_ENCRYPTION_BY_DEFAULT = [
        Property.SERVER_SIDE_ENCRYPTION_BY_DEFAULT_SSE_ALGORITHM
    ]
    CORS_RULE = [
        Property.CORS_RULE_ALLOWED_METHODS,
        Property.CORS_RULE_ALLOWED_ORIGINS
    ]
    RULE = [
        Property.RULE_STATUS
    ]
    NONCURRENT_VERSION_TRANSITION = [
        Property.NONCURRENT_VERSION_TRANSITION_STORAGE_CLASS,
        Property.NONCURRENT_VERSION_TRANSITION_TRANSITION_IN_DAYS
    ]
    TRANSITION = [
        Property.TRANSITION_STORAGE_CLASS
    ]
    ABORT_INCOMPLETE_MULTIPART_UPLOAD = [
        Property.ABORT_INCOMPLETE_MULTIPART_UPLOAD_DAYS_AFTER_INITIATION
    ]
    LAMBDA_CONFIGURATION = [
        Property.LAMBDA_CONFIGURATION_EVENT,
        Property.LAMBDA_CONFIGURATION_FUNCTION
    ]
    QUEUE_CONFIGURATION = [
        Property.QUEUE_CONFIGURATION_EVENT,
        Property.QUEUE_CONFIGURATION_QUEUE
    ]
    TOPIC_CONFIGURATION = [
        Property.TOPIC_CONFIGURATION_EVENT,
        Property.TOPIC_CONFIGURATION_TOPIC
    ]
    NOTIFICATION_FILTER = [
        Property.NOTIFICATION_FILTER_S3_KEY
    ]
    S3_KEY_FILTER = [
        Property.S3_KEY_FILTER_RULES
    ]
    FILTER_RULE = [
        Property.FILTER_RULE_NAME,
        Property.FILTER_RULE_VALUE
    ]
    REPLICATION_RULE = [
        Property.REPLICATION_RULE_DESTINATION,
        Property.REPLICATION_RULE_PREFIX,
        Property.REPLICATION_RULE_STATUS
    ]
    REPLICATION_DESTINATION = [
        Property.REPLICATION_DESTINATION_BUCKET
    ]
    ACCESS_CONTROL_TRANSLATION = [
        Property.ACCESS_CONTROL_TRANSLATION_OWNER
    ]
    ENCRYPTION_CONFIGURATION = [
        Property.ENCRYPTION_CONFIGURATION_REPLICA_KMS_KEY_ID
    ]
    SOURCE_SELECTION_CRITERIA = [
        Property.SOURCE_SELECTION_CRITERIA_SSE_KMS_ENCRYPTED_OBJECTS
    ]
    SSE_KMS_ENCRYPTED_OBJECTS = [
        Property.SSE_KMS_ENCRYPTED_OBJECTS_STATUS
    ]
    REDIRECT_ALL_REQUEST_TO = [
        Property.REDIRECT_ALL_REQUEST_TO_HOST_NAME,
        Property.REDIRECT_ALL_REQUEST_TO_PROTOCOL
    ]
    ROUTING_RULE = [
        Property.ROUTING_RULE_REDIRECT_RULE
    ]

##########################################


class AllowedValues:
    ACCELERATION_STATUS = [StatusEnabledSuspended.ENABLED, StatusEnabledSuspended.SUSPENDED]
    OWNER = [AccessControlTranslationOwner.DESTINATION]
    ALLOWED_METHODS = [HttpMethod.GET, HttpMethod.PUT, HttpMethod.HEAD, HttpMethod.POST, HttpMethod.DELETE]
    OUTPUT_SCHEMA_VERSION = [DataExportOutputSchemaVersion.V_1]
    MODE = [DefaultRetentionMode.COMPLIANCE, DefaultRetentionMode.GOVERNANCE]
    FORMAT = [DestinationFormat.CSV]
    NAME = [FilterRuleName.PREFIX, FilterRuleName.SUFFIX]
    INCLUDED_OBJECT_VERSIONS = [
        InventoryConfigurationIncludedObjectVersions.ALL,
        InventoryConfigurationIncludedObjectVersions.CURRENT
    ]
    SCHEDULE_FREQUENCY = [
        InventoryConfigurationScheduleFrequency.DAILY,
        InventoryConfigurationScheduleFrequency.WEEKLY
    ]
    NONCURRENT_VERSION_TRANSITION_SC = [
        StorageClass.DEEP_ARCHIVE,
        StorageClass.GLACIER,
        StorageClass.INTELLIGENT_TIERING,
        StorageClass.ONEZONE_IA,
        StorageClass.STANDARD_IA
    ]
    REDIRECT_ALL_REQUEST_TO_PROTOCOL = [Protocol.HTTP, Protocol.HTTPS]
    REDIRECT_RULE_PROTOCOL = [Protocol.HTTP, Protocol.HTTPS]
    REPLICATION_DESTINATION_SC = [
        StorageClass.DEEP_ARCHIVE,
        StorageClass.GLACIER,
        StorageClass.INTELLIGENT_TIERING,
        StorageClass.ONEZONE_IA,
        StorageClass.REDUCED_REDUNDANCY,
        StorageClass.STANDARD,
        StorageClass.STANDARD_IA
    ]
    REPLICATION_RULE_STATUS = [StatusEnabledDisabled.ENABLED, StatusEnabledDisabled.DISABLED]
    RULE_STATUS = [StatusEnabledDisabled.ENABLED, StatusEnabledDisabled.DISABLED]
    SSE_BY_DEFAULT_SSE_ALGORITHM = [SSEAlgorithm.AES_256, SSEAlgorithm.AWS_KMS]
    SSE_KMS_ENCRYPED_OBJECTS_STATUS = [StatusEnabledDisabled.ENABLED, StatusEnabledDisabled.DISABLED]
    TRANSITION_SC = [
        StorageClass.DEEP_ARCHIVE,
        StorageClass.GLACIER,
        StorageClass.INTELLIGENT_TIERING,
        StorageClass.ONEZONE_IA,
        StorageClass.STANDARD_IA
    ]
    VERSIONING_CONFIGURATION_STATUS = [StatusEnabledSuspended.ENABLED, StatusEnabledSuspended.SUSPENDED]

##########################################


class Conditions:
    RULE = [
        (
            [Property.LIFECYCLE_CONFIGURATION_RULES],
            lambda lc_rules:
            True if len([
                property
                for lc_rule in lc_rules
                for property in lc_rule.keys() if property in [
                    Property.RULE_ABORT_INCOMPLETE_MULTIPART_UPLOAD,
                    Property.RULE_EXPIRATION_DATE,
                    Property.RULE_EXPIRATION_IN_DAYS,
                    Property.RULE_NONCURRENT_VERSION_EXPIRATION_IN_DAYS,
                    Property.RULE_NONCURRENT_VERSION_TRANSITION,
                    Property.RULE_NONCURRENT_VERSION_TRANSITIONS,
                    Property.RULE_TRANSITION,
                    Property.RULE_TRANSITIONS
                ]
            ]) >= len(lc_rules)
            else Exception("""
                    You must specify at least one of the following properties: AbortIncompleteMultipartUpload,
                    ExpirationDate, ExpirationInDays, NoncurrentVersionExpirationInDays, NoncurrentVersionTransition,
                    NoncurrentVersionTransitions, Transition, or Transitions.
                """)
        )
    ]
    ROUTING_RULE_CONDITION = [
        (
            [Property.ROUTING_RULE_CONDITON],
            lambda rrc:
            True if (
                            rrc.get(Property.ROUTING_RULE_CONDITION_KEY_PREFIX_EQUALS, None) is not None and
                            rrc.get(Property.ROUTING_RULE_CONDITION_HTTP_ERROR_CODE_RETURNED_EQUALS, None) is None
                    ) or (
                            rrc.get(Property.ROUTING_RULE_CONDITION_KEY_PREFIX_EQUALS, None) is None and
                            rrc.get(Property.ROUTING_RULE_CONDITION_HTTP_ERROR_CODE_RETURNED_EQUALS, None) is not None
                    ) else Exception(
                "Only one property must be defined: KeyPrefixEquals or HttpErrorCoderReturnedEquals")
        )
    ]
    REPLACE_KEY_WITH = [
        (
            [Property.REDIRECT_RULE_REPLACE_KEY_PREFIX_WITH],
            lambda property: True if property is None else Exception(
                "Not required due to you have specified ReplaceKeyPrefixWith property!")
        )
    ]
    REPLACE_KEY_PREFIX_WITH = [
        (
            [Property.REDIRECT_RULE_REPLACE_KEY_WITH],
            lambda property: True if property is None else Exception(
                "Not required due to you have specified ReplaceKeyWith property!")
        )
    ]
