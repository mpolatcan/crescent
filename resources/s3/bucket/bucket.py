from typing import List
from resources.shared import BaseCloudFormationResourceModel, Tag
from resources.s3.bucket import (
    AccelerateConfiguration,
    AnalyticsConfiguration,
    BucketEncryption,
    CorsConfiguration,
    InventoryConfiguration,
    LifecycleConfiguration,
    LoggingConfiguration,
    MetricsConfiguration,
    NotificationConfiguration,
    ObjectLockConfiguration,
    PublicAccessBlockConfiguration,
    ReplicationConfiguration
)


class Bucket(BaseCloudFormationResourceModel):
    __TYPE = "AWS::S3::Bucket"
    __PROPERTY_ACCELERATE_CONFIGURATION = "AccelerateConfiguration"
    __PROPERTY_ACCESS_CONTROL = "AccessControl"
    __PROPERTY_ANALYTICS_CONFIGURATIONS = "AnalyticsConfigurations"
    __PROPERTY_BUCKET_ENCRYPTION = "BucketEncryption"
    __PROPERTY_BUCKET_NAME = "BucketName"
    __PROPERTY_CORS_CONFIGURATION = "CorsConfiguration"
    __PROPERTY_INVENTORY_CONFIGURATIONS = "InventoryConfigurations"
    __PROPERTY_LIFECYCLE_CONFIGURATION = "LifecycleConfiguration"
    __PROPERTY_LOGGING_CONFIGURATION = "LoggingConfiguration"
    __PROPERTY_METRICS_CONFIGURATIONS = "MetricsConfigurations"
    __PROPERTY_NOTIFICATION_CONFIGURATION = "NotificationConfiguration"
    __PROPERTY_OBJECT_LOCK_CONFIGURATION = "ObjectLockConfiguration"
    __PROPERTY_OBJECT_LOCK_ENABLED = "ObjectLockEnabled"
    __PROPERTY_PUBLIC_ACCESS_BLOCK_CONFIGURATION = "PublicAccessBlockConfiguration"
    __PROPERTY_REPLICATION_CONFIGURATION = "ReplicationConfiguration"
    __PROPERTY_TAGS = "Tags"
    __PROPERTY_VERSIONING_CONFIGURATION = "VersioningConfiguration"
    __PROPERTY_WEBSITE_CONFIGURATION = "WebsiteConfiguration"

    def __init__(self):
        super(Bucket, self).__init__(type=self.__TYPE)

    def accelerate_configuration(self, value: AccelerateConfiguration):
        return self._add_property_field(self.__PROPERTY_ACCELERATE_CONFIGURATION, value.create())

    def access_control(self, value: str):
        return self._add_property_field(self.__PROPERTY_ACCESS_CONTROL, value)

    def analytics_configurations(self, value: List[AnalyticsConfiguration]):
        return self._add_property_field(self.__PROPERTY_ANALYTICS_CONFIGURATIONS, [conf.create() for conf in value])

    def bucket_encryption(self, value: BucketEncryption):
        return self._add_property_field(self.__PROPERTY_BUCKET_ENCRYPTION, value.create())

    def bucket_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_BUCKET_NAME, value)

    def cors_configuration(self, value: CorsConfiguration):
        return self._add_property_field(self.__PROPERTY_CORS_CONFIGURATION, value.create())

    def inventory_configurations(self, value: List[InventoryConfiguration]):
        return self._add_property_field(self.__PROPERTY_INVENTORY_CONFIGURATIONS, [conf.create() for conf in value])

    def lifecycle_configuration(self, value: LifecycleConfiguration):
        return self._add_property_field(self.__PROPERTY_LIFECYCLE_CONFIGURATION, value.create())

    def logging_configuration(self, value: LoggingConfiguration):
        return self._add_property_field(self.__PROPERTY_LOGGING_CONFIGURATION, value.create())

    def metrics_configurations(self, value: List[MetricsConfiguration]):
        return self._add_property_field(self.__PROPERTY_METRICS_CONFIGURATIONS, [conf.create() for conf in value])

    def notification_configuration(self, value: NotificationConfiguration):
        return self._add_property_field(self.__PROPERTY_NOTIFICATION_CONFIGURATION, value.create())

    def object_lock_configuration(self, value: ObjectLockConfiguration):
        return self._add_property_field(self.__PROPERTY_OBJECT_LOCK_CONFIGURATION, value.create())

    def object_lock_enabled(self, value: bool):
        return self._add_property_field(self.__PROPERTY_OBJECT_LOCK_ENABLED, value)

    def public_access_block_configuration(self, value: PublicAccessBlockConfiguration):
        return self._add_property_field(self.__PROPERTY_PUBLIC_ACCESS_BLOCK_CONFIGURATION, value.create())

    def replication_configuration(self, value: ReplicationConfiguration):
        return self._add_property_field(self.__PROPERTY_REPLICATION_CONFIGURATION, value.create())

    def tags(self, value: List[Tag]):
        return self._add_property_field(self.__PROPERTY_TAGS, [tag.create() for tag in value])
