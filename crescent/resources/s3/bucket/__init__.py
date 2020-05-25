from .abort_incomplete_multipart_upload import AbortIncompleteMultipartUpload
from .accelerate_configuration import AccelerateConfiguration
from .access_control_translation import AccessControlTranslation
from .analytics_configuration import AnalyticsConfiguration
from .bucket import Bucket
from .bucket_encryption import BucketEncryption
from .cors_configuration import CorsConfiguration
from .cors_rule import CorsRule
from .data_export import DataExport
from .default_retention import DefaultRetention
from .destination import Destination
from .encryption_configuration import EncryptionConfiguration
from .filter_rule import FilterRule
from .inventory_configuration import InventoryConfiguration
from .lambda_configuration import LambdaConfiguration
from .lifecycle_configuration import LifecycleConfiguration
from .logging_configuration import LoggingConfiguration
from .metrics_configuration import MetricsConfiguration
from .noncurrent_version_transition import NoncurrentVersionTransition
from .notification_configuration import NotificationConfiguration
from .notification_filter import NotificationFilter
from .object_lock_configuration import ObjectLockConfiguration
from .object_lock_rule import ObjectLockRule
from .public_access_block_configuration import PublicAccessBlockConfiguration
from .queue_configuration import QueueConfiguration
from .redirect_all_request_to import RedirectAllRequestTo
from .redirect_rule import RedirectRule
from .replication_configuration import ReplicationConfiguration
from .replication_destination import ReplicationDestination
from .replication_rule import ReplicationRule
from .routing_rule import RoutingRule
from .routing_rule_condition import RoutingRuleCondition
from .rule import Rule
from .s3_key_filter import S3KeyFilter
from .server_side_encryption_by_default import ServerSideEncryptionByDefault
from .server_side_encryption_rule import ServerSideEncryptionRule
from .source_selection_criteria import SourceSelectionCriteria
from .sse_kms_encrypted_objects import SseKmsEncryptedObjects
from .storage_class_analysis import StorageClassAnalysis
from .tag_filter import TagFilter
from .topic_configuration import TopicConfiguration
from .transition import Transition
from .versioning_configuration import VersioningConfiguration
from .website_configuration import WebsiteConfiguration
from .constants import (StatusEnabledSuspended, StatusEnabledDisabled, AccessControlTranslationOwner,
                        HttpMethod, DataExportOutputSchemaVersion, DefaultRetentionMode,
                        DestinationFormat, FilterRuleName, InventoryConfigurationIncludedObjectVersions,
                        InventoryConfigurationScheduleFrequency, StorageClass, Protocol, SSEAlgorithm)


class BucketFactory:
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
    def Create(id: str): return Bucket(id)

    @staticmethod
    def AbortIncompleteMultipartUpload(): return AbortIncompleteMultipartUpload()

    @staticmethod
    def AccelerateConfiguration(): return AccelerateConfiguration()

    @staticmethod
    def AccessControlTranslation(): return AccessControlTranslation()

    @staticmethod
    def AnalyticsConfiguration(): return AnalyticsConfiguration()

    @staticmethod
    def BucketEncryption(): return BucketEncryption()

    @staticmethod
    def CorsConfiguration(): return CorsConfiguration()

    @staticmethod
    def CorsRule(): return CorsRule()

    @staticmethod
    def DataExport(): return DataExport()

    @staticmethod
    def DefaultRetention(): return DefaultRetention()

    @staticmethod
    def Destination(): return Destination()

    @staticmethod
    def EncryptionConfiguration(): return EncryptionConfiguration()

    @staticmethod
    def FilterRule(): return FilterRule()

    @staticmethod
    def InventoryConfiguration(): return InventoryConfiguration()

    @staticmethod
    def LambdaConfiguration(): return LambdaConfiguration()

    @staticmethod
    def LifecycleConfiguration(): return LifecycleConfiguration()

    @staticmethod
    def LoggingConfiguration(): return LoggingConfiguration()

    @staticmethod
    def MetricsConfiguration(): return MetricsConfiguration()

    @staticmethod
    def NoncurrentVersionTransition(): return NoncurrentVersionTransition()

    @staticmethod
    def NotificationConfiguration(): return NotificationConfiguration()

    @staticmethod
    def NotificationFilter(): return NotificationFilter()

    @staticmethod
    def ObjectLockConfiguration(): return ObjectLockConfiguration()

    @staticmethod
    def ObjectLockRule(): return ObjectLockRule()

    @staticmethod
    def QueueConfiguration(): return QueueConfiguration()

    @staticmethod
    def PublicAccessBlockConfiguration(): return PublicAccessBlockConfiguration()

    @staticmethod
    def RedirectAllRequestTo(): return RedirectAllRequestTo()

    @staticmethod
    def RedirectRule(): return RedirectRule()

    @staticmethod
    def ReplicationConfiguration(): return ReplicationConfiguration()

    @staticmethod
    def ReplicationDestination(): return ReplicationDestination()

    @staticmethod
    def ReplicationRule(): return ReplicationRule()

    @staticmethod
    def RoutingRule(): return RoutingRule()

    @staticmethod
    def RoutingRuleCondition(): return RoutingRuleCondition()

    @staticmethod
    def Rule(): return Rule()

    @staticmethod
    def S3KeyFilter(): return S3KeyFilter()

    @staticmethod
    def ServerSideEncryptionByDefault(): return ServerSideEncryptionByDefault()

    @staticmethod
    def ServerSideEncryptionRule(): return ServerSideEncryptionRule()

    @staticmethod
    def SourceSelectionCriteria(): return SourceSelectionCriteria()

    @staticmethod
    def SseKmsEncryptedObjects(): return SseKmsEncryptedObjects()

    @staticmethod
    def StorageClassAnalysis(): return StorageClassAnalysis()

    @staticmethod
    def TagFilter(): return TagFilter()

    @staticmethod
    def TopicConfiguration(): return TopicConfiguration()

    @staticmethod
    def Transition(): return Transition()

    @staticmethod
    def VersioningConfiguration(): return VersioningConfiguration()

    @staticmethod
    def WebsiteConfiguration(): return WebsiteConfiguration()


__all__ = ["BucketFactory"]
