from pyformation import PyformationResource, Tag
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


class Bucket(PyformationResource):
    __TYPE = "AWS::S3::Bucket"

    def __init__(self, id: str):
        super(Bucket, self).__init__(id, self.__TYPE)

    def AccelerateConfiguration(self, value: AccelerateConfiguration):
        return self._set_property(self.AccelerateConfiguration.__name__, value.__to_dict__())

    def AccessControl(self, value: str):
        return self._set_property(self.AccessControl.__name__, value)

    def AnalyticsConfigurations(self, *value: AnalyticsConfiguration):
        return self._set_property(self.AnalyticsConfigurations.__name__, [ac.__to_dict__() for ac in list(value)])

    def BucketEncryption(self, value: BucketEncryption):
        return self._set_property(self.BucketEncryption.__name__, value.__to_dict__())

    def BucketName(self, value: str):
        return self._set_property(self.BucketName.__name__, value)

    def CorsConfiguration(self, value: CorsConfiguration):
        return self._set_property(self.CorsConfiguration.__name__, value.__to_dict__())

    def InventoryConfigurations(self, *value: InventoryConfiguration):
        return self._set_property(self.InventoryConfigurations.__name__, [ic.__to_dict__() for ic in list(value)])

    def LifecycleConfiguration(self, value: LifecycleConfiguration):
        return self._set_property(self.LifecycleConfiguration.__name__, value.__to_dict__())

    def LoggingConfiguration(self, value: LoggingConfiguration):
        return self._set_property(self.LoggingConfiguration.__name__, value.__to_dict__())

    def MetricsConfigurations(self, *value: MetricsConfiguration):
        return self._set_property(self.MetricsConfigurations.__name__, [mc.__to_dict__() for mc in list(value)])

    def NotificationConfiguration(self, value: NotificationConfiguration):
        return self._set_property(self.NotificationConfiguration.__name__, value.__to_dict__())

    def ObjectLockConfiguration(self, value: ObjectLockConfiguration):
        return self._set_property(self.ObjectLockConfiguration.__name__, value.__to_dict__())

    def ObjectLockEnabled(self, value: bool):
        return self._set_property(self.ObjectLockEnabled.__name__, value)

    def PublicAccessBlockConfiguration(self, value: PublicAccessBlockConfiguration):
        return self._set_property(self.PublicAccessBlockConfiguration.__name__, value.__to_dict__())

    def ReplicationConfiguration(self, value: ReplicationConfiguration):
        return self._set_property(self.ReplicationConfiguration.__name__, value.__to_dict__())

    def VersioningConfiguration(self, value: VersioningConfiguration):
        return self._set_property(self.VersioningConfiguration.__name__, value.__to_dict__())

    def WebsiteConfiguration(self, value: WebsiteConfiguration):
        return self._set_property(self.WebsiteConfiguration.__name__, value.__to_dict__())

    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
