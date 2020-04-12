from crescent.core import Resource, Tag
from crescent.functions import AnyFn
from .accelerate_configuration import AccelerateConfiguration
from .analytics_configuration import AnalyticsConfiguration
from .bucket_encryption import BucketEncryption
from .cors_configuration import CorsConfiguration
from .inventory_configuration import InventoryConfiguration
from .lifecycle_configuration import LifecycleConfiguration
from .logging_configuration import LoggingConfiguration
from .metrics_configuration import MetricsConfiguration
from .notification_configuration import NotificationConfiguration
from .object_lock_configuration import ObjectLockConfiguration
from .public_access_block_configuration import PublicAccessBlockConfiguration
from .replication_configuration import ReplicationConfiguration
from .versioning_configuration import VersioningConfiguration
from .website_configuration import WebsiteConfiguration
from typing import Union


class Bucket(Resource):
    __TYPE = "AWS::S3::Bucket"

    def __init__(self, id: str):
        super(Bucket, self).__init__(id, self.__TYPE)

    def AccelerateConfiguration(self, accelerate_conf: AccelerateConfiguration):
        return self._set_property(self.AccelerateConfiguration.__name__, accelerate_conf)

    def AccessControl(self, access_control: Union[str, AnyFn]):
        return self._set_property(self.AccessControl.__name__, access_control)

    def AnalyticsConfigurations(self, *analytics_confs: AnalyticsConfiguration):
        return self._set_property(self.AnalyticsConfigurations.__name__, list(analytics_confs))

    def BucketEncryption(self, bucket_encryption: BucketEncryption):
        return self._set_property(self.BucketEncryption.__name__, bucket_encryption)

    def BucketName(self, bucket_name: Union[str, AnyFn]):
        return self._set_property(self.BucketName.__name__, bucket_name)

    def CorsConfiguration(self, cors_conf: CorsConfiguration):
        return self._set_property(self.CorsConfiguration.__name__, cors_conf)

    def InventoryConfigurations(self, *inventory_confs: InventoryConfiguration):
        return self._set_property(self.InventoryConfigurations.__name__, list(inventory_confs))

    def LifecycleConfiguration(self, lifecycle_conf: LifecycleConfiguration):
        return self._set_property(self.LifecycleConfiguration.__name__, lifecycle_conf)

    def LoggingConfiguration(self, logging_conf: LoggingConfiguration):
        return self._set_property(self.LoggingConfiguration.__name__, logging_conf)

    def MetricsConfigurations(self, *metrics_confs: MetricsConfiguration):
        return self._set_property(self.MetricsConfigurations.__name__, list(metrics_confs))

    def NotificationConfiguration(self, notification_conf: NotificationConfiguration):
        return self._set_property(self.NotificationConfiguration.__name__, notification_conf)

    def ObjectLockConfiguration(self, object_lock_conf: ObjectLockConfiguration):
        return self._set_property(self.ObjectLockConfiguration.__name__, object_lock_conf)

    def ObjectLockEnabled(self, object_lock_enabled: Union[bool, AnyFn]):
        return self._set_property(self.ObjectLockEnabled.__name__, object_lock_enabled)

    def PublicAccessBlockConfiguration(self, public_access_block_conf: PublicAccessBlockConfiguration):
        return self._set_property(self.PublicAccessBlockConfiguration.__name__, public_access_block_conf)

    def ReplicationConfiguration(self, replication_conf: ReplicationConfiguration):
        return self._set_property(self.ReplicationConfiguration.__name__, replication_conf)

    def VersioningConfiguration(self, versioning_conf: VersioningConfiguration):
        return self._set_property(self.VersioningConfiguration.__name__, versioning_conf)

    def WebsiteConfiguration(self, website_conf: WebsiteConfiguration):
        return self._set_property(self.WebsiteConfiguration.__name__, website_conf)

    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
