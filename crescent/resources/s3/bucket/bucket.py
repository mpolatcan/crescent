from crescent.core import Resource, Tag, Validator
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
from .constants import ModelRequiredProperties


class Bucket(Resource):
    __TYPE = "AWS::S3::Bucket"

    def __init__(self, id: str):
        super(Bucket, self).__init__(id, self.__TYPE)

    @Validator.validate(type=AccelerateConfiguration, required_properties=ModelRequiredProperties.ACCELERATE_CONFIGURATION)
    def AccelerateConfiguration(self, accelerate_conf: AccelerateConfiguration):
        return self._set_property(self.AccelerateConfiguration.__name__, accelerate_conf.__to_dict__())

    @Validator.validate(type=str)
    def AccessControl(self, access_control: str):
        return self._set_property(self.AccessControl.__name__, access_control)

    @Validator.validate(type=AnalyticsConfiguration, required_properties=ModelRequiredProperties.ANALYTICS_CONFIGURATION)
    def AnalyticsConfigurations(self, *analytics_confs: AnalyticsConfiguration):
        return self._set_property(self.AnalyticsConfigurations.__name__, [ac.__to_dict__() for ac in list(analytics_confs)])

    @Validator.validate(type=BucketEncryption, required_properties=ModelRequiredProperties.BUCKET_ENCRYPTION)
    def BucketEncryption(self, bucket_encryption: BucketEncryption):
        return self._set_property(self.BucketEncryption.__name__, bucket_encryption.__to_dict__())

    @Validator.validate(type=str)
    def BucketName(self, bucket_name: str):
        return self._set_property(self.BucketName.__name__, bucket_name)

    @Validator.validate(type=CorsConfiguration, required_properties=ModelRequiredProperties.CORS_CONFIGURATION)
    def CorsConfiguration(self, cors_conf: CorsConfiguration):
        return self._set_property(self.CorsConfiguration.__name__, cors_conf.__to_dict__())

    @Validator.validate(type=InventoryConfiguration, required_properties=ModelRequiredProperties.INVENTORY_CONFIGURATION)
    def InventoryConfigurations(self, *inventory_confs: InventoryConfiguration):
        return self._set_property(self.InventoryConfigurations.__name__, [ic.__to_dict__() for ic in list(inventory_confs)])

    @Validator.validate(type=LifecycleConfiguration, required_properties=ModelRequiredProperties.LIFECYCLE_CONFIGURATION)
    def LifecycleConfiguration(self, lifecycle_conf: LifecycleConfiguration):
        return self._set_property(self.LifecycleConfiguration.__name__, lifecycle_conf.__to_dict__())

    @Validator.validate(type=LoggingConfiguration)
    def LoggingConfiguration(self, logging_conf: LoggingConfiguration):
        return self._set_property(self.LoggingConfiguration.__name__, logging_conf.__to_dict__())

    @Validator.validate(type=MetricsConfiguration, required_properties=ModelRequiredProperties.METRICS_CONFIGURATION)
    def MetricsConfigurations(self, *metrics_confs: MetricsConfiguration):
        return self._set_property(self.MetricsConfigurations.__name__, [mc.__to_dict__() for mc in list(metrics_confs)])

    @Validator.validate(type=NotificationConfiguration)
    def NotificationConfiguration(self, notification_conf: NotificationConfiguration):
        return self._set_property(self.NotificationConfiguration.__name__, notification_conf.__to_dict__())

    @Validator.validate(type=ObjectLockConfiguration)
    def ObjectLockConfiguration(self, object_lock_conf: ObjectLockConfiguration):
        return self._set_property(self.ObjectLockConfiguration.__name__, object_lock_conf.__to_dict__())

    @Validator.validate(type=bool)
    def ObjectLockEnabled(self, object_lock_enabled: bool):
        return self._set_property(self.ObjectLockEnabled.__name__, object_lock_enabled)

    @Validator.validate(type=PublicAccessBlockConfiguration)
    def PublicAccessBlockConfiguration(self, public_access_block_conf: PublicAccessBlockConfiguration):
        return self._set_property(self.PublicAccessBlockConfiguration.__name__, public_access_block_conf.__to_dict__())

    @Validator.validate(type=ReplicationConfiguration, required_properties=ModelRequiredProperties.REPLICATION_CONFIGURATION)
    def ReplicationConfiguration(self, replication_conf: ReplicationConfiguration):
        return self._set_property(self.ReplicationConfiguration.__name__, replication_conf.__to_dict__())

    @Validator.validate(type=VersioningConfiguration, required_properties=ModelRequiredProperties.VERSIONING_CONFIGURATION)
    def VersioningConfiguration(self, versioning_conf: VersioningConfiguration):
        return self._set_property(self.VersioningConfiguration.__name__, versioning_conf.__to_dict__())

    @Validator.validate(type=WebsiteConfiguration)
    def WebsiteConfiguration(self, website_conf: WebsiteConfiguration):
        return self._set_property(self.WebsiteConfiguration.__name__, website_conf.__to_dict__())

    @Validator.validate(type=Tag)
    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
