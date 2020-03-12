from .access_point import (
    AccessPoint,
    PublicAccessBlockConfiguration,
    VpcConfiguration
)

from .bucket import (
    AbortIncompleteMultipartUpload,
    AccelerateConfiguration,
    AccessControlTranslation,
    AnalyticsConfiguration,
    Bucket,
    BucketEncryption,
    CorsConfiguration,
    CorsRule,
    DataExport,
    DefaultRetention,
    Destination,
    EncryptionConfiguration,
    FilterRule,
    InventoryConfiguration,
    LambdaConfiguration,
    LifecycleConfiguration,
    LoggingConfiguration,
    MetricsConfiguration,
    NoncurrentVersionTransition,
    NotificationConfiguration,
    NotificationFilter,
    ObjectLockConfiguration,
    ObjectLockRule,
    PublicAccessBlockConfiguration,
    QueueConfiguration,
    RedirectAllRequestTo,
    RedirectRule,
    ReplicationConfiguration,
    ReplicationDestination,
    ReplicationRule,
    RoutingRule,
    RoutingRuleCondition,
    Rule,
    S3KeyFilter,
    ServerSideEncryptionByDefault,
    ServerSideEncryptionRule,
    SourceSelectionCriteria,
    SseKmsEncryptedObjects,
    StorageClassAnalysis,
    TagFilter,
    TopicConfiguration,
    Transition,
    VersioningConfiguration,
    WebsiteConfiguration
)

from .bucket_policy import BucketPolicy


class S3Factory:
    @staticmethod
    def AccessPoint(id: str):
        return AccessPoint(id)

    @staticmethod
    def PublicAccessBlockConfiguration():
        return PublicAccessBlockConfiguration()

    @staticmethod
    def VpcConfiguration():
        return VpcConfiguration()

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

    @staticmethod
    def BucketPolicy(id: str):
        return BucketPolicy(id)


__all__ = [
    "S3Factory"
]
