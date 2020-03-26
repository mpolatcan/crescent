from .access_point import *
from .bucket import *
from .bucket_policy import *


class S3:
    class AccessPoint:
        @staticmethod
        def Create(id: str):
            return AccessPoint(id)

        @staticmethod
        def PublicAccessBlockConfiguration():
            return PublicAccessBlockConfiguration()

        @staticmethod
        def VpcConfiguration():
            return VpcConfiguration()

    class Bucket:
        AccelerationStatus = StatusEnabledSuspended
        AccessControlTranslationOwner = AccessControlTranslationOwner
        HttpMethod = HttpMethod
        DefaultRetentionMode = DefaultRetentionMode
        DestinationFormat = DestinationFormat
        DataExportOutputSchemaVersion = DataExportOutputSchemaVersion
        StorageClass = StorageClass
        InventoryConfigurationScheduleFrequency = InventoryConfigurationScheduleFrequency
        InventoryConfigurationIncludedObjectVersions = InventoryConfigurationIncludedObjectVersions
        Protocol = Protocol
        ReplicationRuleStatus = StatusEnabledDisabled
        RuleStatus = StatusEnabledDisabled
        SSEAlgorithm = SSEAlgorithm
        SseKmsEncryptedObjectsStatus = StatusEnabledDisabled
        VersioningConfigurationStatus = StatusEnabledSuspended
        FilterRuleName = FilterRuleName

        @staticmethod
        def Create(id: str):
            return Bucket(id)

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
            return PublicAccessBlockConfiguration()

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

    class BucketPolicy:
        @staticmethod
        def Create(id: str):
            return BucketPolicy(id)


__all__ = [
    "S3"
]
