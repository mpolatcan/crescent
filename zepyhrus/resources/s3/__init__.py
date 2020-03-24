from .access_point import *
from .bucket import *
from .bucket_policy import *


class S3Factory:
    class __AccessPointFactory:
        @staticmethod
        def AccessPoint(id: str):
            return AccessPoint(id)

        @staticmethod
        def PublicAccessBlockConfiguration():
            return PublicAccessBlockConfiguration()

        @staticmethod
        def VpcConfiguration():
            return VpcConfiguration()

    class __BucketFactory:
        acceleration_status = StatusEnabledSuspended
        access_control_translation_owner = AccessControlTranslationOwner
        http_method = HttpMethod
        default_retention_mode = DefaultRetentionMode
        destination_format = DestinationFormat
        data_export_output_schema_version = DataExportOutputSchemaVersion
        storage_class = StorageClass
        inventory_configuration_schedule_frequency = InventoryConfigurationScheduleFrequency
        inventory_configuration_included_object_versions = InventoryConfigurationIncludedObjectVersions
        protocol = Protocol
        replication_rule_status = StatusEnabledDisabled
        rule_status = StatusEnabledDisabled
        sse_algorithm = SSEAlgorithm
        sse_kms_encrypted_objects_status = StatusEnabledDisabled
        versioning_configuration_status = StatusEnabledSuspended
        filter_rule_name = FilterRuleName

        @staticmethod
        def AbortIncompleteMultipartUpload():
            return AbortIncompleteMultipartUpload()

        @staticmethod
        def AccelerateConfiguration():
            return AccelerateConfiguration()

        @staticmethod
        def AccessControlTranslation():
            return AccessControlTranslation()

        @staticmethod
        def AnalyticsConfiguration():
            return AnalyticsConfiguration()

        @staticmethod
        def Bucket(id: str):
            return Bucket(id)

        @staticmethod
        def BucketEncryption():
            return BucketEncryption()

        @staticmethod
        def CorsConfiguration():
            return CorsConfiguration()

        @staticmethod
        def CorsRule():
            return CorsRule()

        @staticmethod
        def DataExport():
            return DataExport()

        @staticmethod
        def DefaultRetention():
            return DefaultRetention()

        @staticmethod
        def Destination():
            return Destination()

        @staticmethod
        def EncryptionConfiguration():
            return EncryptionConfiguration()

        @staticmethod
        def FilterRule():
            return FilterRule()

        @staticmethod
        def InventoryConfiguration():
            return InventoryConfiguration()

        @staticmethod
        def LambdaConfiguration():
            return LambdaConfiguration()

        @staticmethod
        def LifecycleConfiguration():
            return LifecycleConfiguration()

        @staticmethod
        def LoggingConfiguration():
            return LoggingConfiguration()

        @staticmethod
        def MetricsConfiguration():
            return MetricsConfiguration()

        @staticmethod
        def NoncurrentVersionTransition():
            return NoncurrentVersionTransition()

        @staticmethod
        def NotificationConfiguration():
            return NotificationConfiguration()

        @staticmethod
        def NotificationFilter():
            return NotificationFilter()

        @staticmethod
        def ObjectLockConfiguration():
            return ObjectLockConfiguration()

        @staticmethod
        def ObjectLockRule():
            return ObjectLockRule()

        @staticmethod
        def QueueConfiguration():
            return QueueConfiguration()

        @staticmethod
        def PublicAccessBlockConfiguration():
            return BucketPublicAccessBlockConfiguration()

        @staticmethod
        def RedirectAllRequestTo():
            return RedirectAllRequestTo()

        @staticmethod
        def RedirectRule():
            return RedirectRule()

        @staticmethod
        def ReplicationConfiguration():
            return ReplicationConfiguration()

        @staticmethod
        def ReplicationDestination():
            return ReplicationDestination()

        @staticmethod
        def ReplicationRule():
            return ReplicationRule()

        @staticmethod
        def RoutingRule():
            return RoutingRule()

        @staticmethod
        def RoutingRuleCondition():
            return RoutingRuleCondition()

        @staticmethod
        def Rule():
            return Rule()

        @staticmethod
        def S3KeyFilter():
            return S3KeyFilter()

        @staticmethod
        def ServerSideEncryptionByDefault():
            return ServerSideEncryptionByDefault()

        @staticmethod
        def ServerSideEncryptionRule():
            return ServerSideEncryptionRule()

        @staticmethod
        def SourceSelectionCriteria():
            return SourceSelectionCriteria()

        @staticmethod
        def SseKmsEncryptedObjects():
            return SseKmsEncryptedObjects()

        @staticmethod
        def StorageClassAnalysis():
            return StorageClassAnalysis()

        @staticmethod
        def TagFilter():
            return TagFilter()

        @staticmethod
        def TopicConfiguration():
            return TopicConfiguration()

        @staticmethod
        def Transition():
            return Transition()

        @staticmethod
        def VersioningConfiguration():
            return VersioningConfiguration()

        @staticmethod
        def WebsiteConfiguration():
            return WebsiteConfiguration()

    class __BucketPolicyFactory:
        @staticmethod
        def BucketPolicy(id: str):
            return BucketPolicy(id)

    access_point = __AccessPointFactory
    bucket = __BucketFactory
    bucket_policy = __BucketPolicyFactory


s3 = S3Factory
s3_access_point = s3.access_point
s3_bucket = s3.bucket
s3_bucket_policy = s3.bucket_policy


__all__ = [
    "s3",
    "s3_bucket",
    "s3_access_point",
    "s3_bucket_policy"
]
