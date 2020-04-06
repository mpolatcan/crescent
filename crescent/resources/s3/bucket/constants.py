from crescent.core.constants import get_values


class StatusEnabledSuspended:
    ENABLED = "Enabled"
    SUSPENDED = "Suspended"

# -----------------------------------------


class StatusEnabledDisabled:
    ENABLED = "Enabled"
    DISABLED = "Disabled"

# -----------------------------------------


class AccessControlTranslationOwner:
    DESTINATION = "Destination"

# -----------------------------------------


class HttpMethod:
    GET = "GET"
    PUT = "PUT"
    HEAD = "HEAD"
    POST = "POST"
    DELETE = "DELETE"

# -----------------------------------------


class DataExportOutputSchemaVersion:
    V_1 = "V_1"

# -----------------------------------------


class DefaultRetentionMode:
    COMPLIANCE = "COMPLIANCE"
    GOVERNANCE = "GOVERNANCE"

# -----------------------------------------


class DestinationFormat:
    CSV = "CSV"

# -----------------------------------------


class FilterRuleName:
    PREFIX = "prefix"
    SUFFIX = "suffix"

# -----------------------------------------


class InventoryConfigurationIncludedObjectVersions:
    ALL = "All"
    CURRENT = "Current"

# -----------------------------------------


class InventoryConfigurationScheduleFrequency:
    DAILY = "Daily"
    WEEKLY = "Weekly"

# -----------------------------------------


class StorageClass:
    DEEP_ARCHIVE = "DEEP_ARCHIVE"
    GLACIER = "GLACIER"
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    ONEZONE_IA = "ONEZONE_IA"
    STANDARD = "STANDARD"
    STANDARD_IA = "STANDARD_IA"
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"

# -----------------------------------------


class Protocol:
    HTTP = "http"
    HTTPS = "https"

# -----------------------------------------


class SSEAlgorithm:
    AES_256 = "AES256"
    AWS_KMS = "aws:kms"

# -----------------------------------------


class _Property:
    class LifecycleConfiguration:
        RULES = "Rules"

    class Rule:
        ABORT_INCOMPLETE_MULTIPART_UPLOAD = "AbortIncompleteMultipartUpload"
        EXPIRATION_DATE = "ExpirationDate"
        EXPIRATION_IN_DAYS = "ExpirationInDays"
        NONCURRENT_VERSION_EXPIRATION_IN_DAYS = "NoncurrentVersionExpirationInDays"
        NONCURRENT_VERSION_TRANSITION = "NoncurrentVersionTransition"
        NONCURRENT_VERSION_TRANSITIONS = "NoncurrentVersionTransitions"
        TRANSITION = "Transition"
        TRANSITIONS = "Transitions"

    class RoutingRule:
        ROUTING_RULE_CONDITON = "RoutingRuleCondition"

    class RoutingRuleCondition:
        HTTP_ERROR_CODE_RETURNED_EQUALS = "HttpErrorCodeReturnedEquals"
        KEY_PREFIX_EQUALS = "KeyPrefixEquals"

    class RedirectRule:
        REPLACE_KEY_WITH = "ReplaceKeyWith"
        REPLACE_KEY_PREFIX_WITH = "ReplaceKeyPrefixWith"

# -----------------------------------------


class _RequiredProperties:
    class AccelerateConfiguration:
        ACCELERATION_STATUS = "AccelerationStatus"

    class AnalyticsConfiguration:
        ID = "Id"
        STORAGE_CLASS_ANALYSIS = "StorageClassAnalysis"

    class BucketEncryption:
        SERVER_SIDE_ENCRYPTION_CONFIGURATION = "ServerSideEncryptionConfiguration"

    class CorsConfiguration:
        CORS_RULES = "CorsRules"

    class InventoryConfiguration:
        DESTINATION = "Destination"
        ENABLED = "Enabled"
        ID = "Id"
        INCLUDED_OBJECT_VERSIONS = "IncludedObjectVersions"
        SCHEDULE_FREQUENCY = "ScheduleFrequency"

    class LifecycleConfiguration:
        RULES = "Rules"

    class MetricsConfiguration:
        ID = "Id"

    class ReplicationConfiguration:
        ROLE = "Role"
        RULES = "Rules"

    class VersioningConfiguration:
        STATUS = "Status"

    class DataExport:
        DESTINATION = "Destination"
        OUTPUT_SCHEMA_VERSION = "OutputSchemaVersion"

    class Destination:
        BUCKET_ARN = "BucketArn"
        FORMAT = "Format"

    class TagFilter:
        KEY = "Key"
        VALUE = "Value"

    class ServerSideEncryptionByDefault:
        SSE_ALGORITHM = "SSEAlgorithm"

    class CorsRule:
        ALLOWED_METHODS = "AllowedMethods"
        ALLOWED_ORIGINS = "AllowedOrigins"

    class Rule:
        STATUS = "Status"

    class NoncurrentVersionTransition:
        STORAGE_CLASS = "StorageClass"
        TRANSITION_IN_DAYS = "TransitionInDays"

    class Transition:
        STORAGE_CLASS = "StorageClass"

    class AbortIncompleteMultipartUpload:
        DAYS_AFTER_INITIATION = "DaysAfterInitiation"

    class LambdaConfiguration:
        EVENT = "Event"
        FUNCTION = "Function"

    class QueueConfiguration:
        EVENT = "Event"
        QUEUE = "Queue"

    class TopicConfiguration:
        EVENT = "Event"
        QUEUE = "Queue"

    class NotificationFilter:
        S3_KEY = "S3Key"

    class S3KeyFilter:
        RULES = "Rules"

    class FilterRule:
        NAME = "Name"
        VALUE = "Value"

    class ReplicationRule:
        DESTINATION = "Destination"
        PREFIX = "Prefix"
        STATUS = "Status"

    class ReplicationDestination:
        BUCKET = "Bucket"

    class AccessControlTranslation:
        OWNER = "Owner"

    class EncryptionConfiguration:
        REPLICA_KMS_KEY_ID = "ReplicaKmsKeyID"

    class SourceSelectionCriteria:
        SSE_KMS_ENCRYPTED_OBJECTS = "SseKmsEncryptedObjects"

    class SseKmsEncryptedObjects:
        STATUS = "Status"

    class RedirectAllRequestTo:
        HOST_NAME = "HostName"
        PROTOCOL = "Protocol"

    class RoutingRule:
        REDIRECT_RULE = "RedirectRule"


# -----------------------------------------


class ModelRequiredProperties:
    ACCELERATE_CONFIGURATION = get_values(_RequiredProperties.AccelerateConfiguration)
    ANALYTICS_CONFIGURATION = get_values(_RequiredProperties.AnalyticsConfiguration)
    BUCKET_ENCRYPTION = get_values(_RequiredProperties.BucketEncryption)
    CORS_CONFIGURATION = get_values(_RequiredProperties.CorsConfiguration)
    INVENTORY_CONFIGURATION = get_values(_RequiredProperties.InventoryConfiguration)
    LIFECYCLE_CONFIGURATION = get_values(_RequiredProperties.LifecycleConfiguration)
    METRICS_CONFIGURATION = get_values(_RequiredProperties.MetricsConfiguration)
    REPLICATION_CONFIGURATION = get_values(_RequiredProperties.ReplicationConfiguration)
    VERSIONING_CONFIGURATION = get_values(_RequiredProperties.VersioningConfiguration)
    TAG_FILTER = get_values(_RequiredProperties.TagFilter)
    CORS_RULE = get_values(_RequiredProperties.CorsRule)
    DESTINATION = get_values(_RequiredProperties.Destination)
    NOTIFICATION_FILTER = get_values(_RequiredProperties.NotificationFilter)
    RULE = get_values(_RequiredProperties.Rule)
    LAMBDA_CONFIGURATION = get_values(_RequiredProperties.LambdaConfiguration)
    QUEUE_CONFIGURATION = get_values(_RequiredProperties.QueueConfiguration)
    TOPIC_CONFIGURATION = get_values(_RequiredProperties.TopicConfiguration)
    S3_KEY_FILTER = get_values(_RequiredProperties.S3KeyFilter)
    REPLICATION_RULE = get_values(_RequiredProperties.ReplicationRule)
    ACCESS_CONTROL_TRANSLATION = get_values(_RequiredProperties.AccessControlTranslation)
    ENCRYPTION_CONFIGURATION = get_values(_RequiredProperties.EncryptionConfiguration)
    REPLICATION_DESTINATION = get_values(_RequiredProperties.ReplicationDestination)
    SOURCE_SELECTION_CRITERIA = get_values(_RequiredProperties.SourceSelectionCriteria)
    ABORT_INCOMPLETE_MULTIPART_UPLOAD = get_values(_RequiredProperties.AbortIncompleteMultipartUpload)
    NONCURRENT_VERSION_TRANSITION = get_values(_RequiredProperties.NoncurrentVersionTransition)
    TRANSITION = get_values(_RequiredProperties.Transition)
    FILTER_RULE = get_values(_RequiredProperties.FilterRule)
    SERVER_SIDE_ENCRYPTION_BY_DEFAULT = get_values(_RequiredProperties.ServerSideEncryptionByDefault)
    SSE_KMS_ENCRYPTED_OBJECTS = get_values(_RequiredProperties.SseKmsEncryptedObjects)
    DATA_EXPORT = get_values(_RequiredProperties.DataExport)
    REDIRECT_ALL_REQUEST_TO = get_values(_RequiredProperties.RedirectAllRequestTo)
    ROUTING_RULE = get_values(_RequiredProperties.RoutingRule)
# -----------------------------------------


class AllowedValues:
    ACCELERATION_STATUS = get_values(StatusEnabledSuspended)
    OWNER = get_values(AccessControlTranslationOwner)
    ALLOWED_METHODS = get_values(HttpMethod)
    OUTPUT_SCHEMA_VERSION = get_values(DataExportOutputSchemaVersion)
    MODE = get_values(DefaultRetentionMode)
    FORMAT = get_values(DestinationFormat)
    NAME = get_values(FilterRuleName)
    INCLUDED_OBJECT_VERSIONS = get_values(InventoryConfigurationIncludedObjectVersions)
    SCHEDULE_FREQUENCY = get_values(InventoryConfigurationScheduleFrequency)
    NONCURRENT_VERSION_TRANSITION_SC = [
        StorageClass.DEEP_ARCHIVE, StorageClass.GLACIER, StorageClass.INTELLIGENT_TIERING,
        StorageClass.ONEZONE_IA, StorageClass.STANDARD_IA
    ]
    REDIRECT_ALL_REQUEST_TO_PROTOCOL = get_values(Protocol)
    REDIRECT_RULE_PROTOCOL = get_values(Protocol)
    REPLICATION_DESTINATION_SC = [
        StorageClass.DEEP_ARCHIVE, StorageClass.GLACIER, StorageClass.INTELLIGENT_TIERING,
        StorageClass.ONEZONE_IA, StorageClass.REDUCED_REDUNDANCY, StorageClass.STANDARD,
        StorageClass.STANDARD_IA
    ]
    REPLICATION_RULE_STATUS = get_values(StatusEnabledDisabled)
    RULE_STATUS = get_values(StatusEnabledDisabled)
    SSE_BY_DEFAULT_SSE_ALGORITHM = get_values(SSEAlgorithm)
    SSE_KMS_ENCRYPED_OBJECTS_STATUS = get_values(StatusEnabledDisabled)
    TRANSITION_SC = [
        StorageClass.DEEP_ARCHIVE, StorageClass.GLACIER, StorageClass.INTELLIGENT_TIERING,
        StorageClass.ONEZONE_IA, StorageClass.STANDARD_IA
    ]
    VERSIONING_CONFIGURATION_STATUS = get_values(StatusEnabledSuspended)

# -----------------------------------------


class Conditions:
    RULE_STATUS = [
        (
            get_values(_Property.Rule),
            lambda *properties:
                dict(is_valid=True) if len([property for property in list(properties) if property]) > 0
                else dict(
                    is_valid=False,
                    error="You must specify at least one of the following properties of Rule: \n\t* {properties}".format(
                        properties="\n\t* ".join(get_values(_Property.Rule))
                    )
                )
        )
    ]
    ROUTING_RULE_CONDITION_KEY_PREFIX_EQUALS = [
        (
            [_Property.RoutingRuleCondition.HTTP_ERROR_CODE_RETURNED_EQUALS],
            lambda property:
                dict(is_valid=True) if not property
                else dict(
                    is_valid=False,
                    error=("RoutingRuleCondition's property KeyPrefixEquals can't specified due to "
                           "you have specified HttpErrorCodeReturnedEquals property!")
                )
        )
    ]
    ROUTING_RULE_CONDITION_HTTP_ERROR_CODE_RETURNED_EQUALS = [
        (
            [_Property.RoutingRuleCondition.KEY_PREFIX_EQUALS],
            lambda property:
                dict(is_valid=True) if not property
                else dict(
                    is_valid=False,
                    error=("RoutingRuleCondition's property HttpErrorCodeReturnedEquals can't specified due to "
                           "you have specified KeyPrefixEquals property!")
                )
        )
    ]
    REDIRECT_RULE_REPLACE_KEY_WITH = [
        (
            [_Property.RedirectRule.REPLACE_KEY_PREFIX_WITH],
            lambda property:
                dict(is_valid=True) if not property
                else dict(
                    is_valid=False,
                    error=("RedirectRule's property ReplaceKeyWith can't specified due to you "
                           "have specified ReplaceKeyPrefixWith property!")
                )
        )
    ]
    REDIRECT_RULE_REPLACE_KEY_PREFIX_WITH = [
        (
            [_Property.RedirectRule.REPLACE_KEY_WITH],
            lambda property: dict(is_valid=True) if not property
            else dict(
                is_valid=False,
                error=("RedirectRule's property ReplaceKeyPrefixWith can't specified due to you "
                       "have specified ReplaceKeyWith property!")
            )
        )
    ]
