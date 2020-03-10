from pyformation.resources.shared import BaseCloudFormationResourceModel, Tag
from pyformation.resources.s3.bucket import (
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
        return self._add_property_field(self.__PROPERTY_ACCELERATE_CONFIGURATION, value)

    def access_control(self, value: str):
        return self._add_property_field(self.__PROPERTY_ACCESS_CONTROL, value)

    def analytics_configurations(self, *value: AnalyticsConfiguration):
        return self._add_property_field(self.__PROPERTY_ANALYTICS_CONFIGURATIONS, [conf for conf in list(value)])

    def bucket_encryption(self, value: BucketEncryption):
        return self._add_property_field(self.__PROPERTY_BUCKET_ENCRYPTION, value)

    def bucket_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_BUCKET_NAME, value)

    def cors_configuration(self, value: CorsConfiguration):
        return self._add_property_field(self.__PROPERTY_CORS_CONFIGURATION, value)

    def inventory_configurations(self, *value: InventoryConfiguration):
        return self._add_property_field(self.__PROPERTY_INVENTORY_CONFIGURATIONS, [conf for conf in list(value)])

    def lifecycle_configuration(self, value: LifecycleConfiguration):
        return self._add_property_field(self.__PROPERTY_LIFECYCLE_CONFIGURATION, value)

    def logging_configuration(self, value: LoggingConfiguration):
        return self._add_property_field(self.__PROPERTY_LOGGING_CONFIGURATION, value)

    def metrics_configurations(self, *value: MetricsConfiguration):
        return self._add_property_field(self.__PROPERTY_METRICS_CONFIGURATIONS, [conf for conf in list(value)])

    def notification_configuration(self, value: NotificationConfiguration):
        return self._add_property_field(self.__PROPERTY_NOTIFICATION_CONFIGURATION, value)

    def object_lock_configuration(self, value: ObjectLockConfiguration):
        return self._add_property_field(self.__PROPERTY_OBJECT_LOCK_CONFIGURATION, value)

    def object_lock_enabled(self, value: bool):
        return self._add_property_field(self.__PROPERTY_OBJECT_LOCK_ENABLED, value)

    def public_access_block_configuration(self, value: PublicAccessBlockConfiguration):
        return self._add_property_field(self.__PROPERTY_PUBLIC_ACCESS_BLOCK_CONFIGURATION, value)

    def replication_configuration(self, value: ReplicationConfiguration):
        return self._add_property_field(self.__PROPERTY_REPLICATION_CONFIGURATION, value)

    def tags(self, *value: Tag):
        return self._add_property_field(self.__PROPERTY_TAGS, [tag for tag in list(value)])