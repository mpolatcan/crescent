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
    def AccelerateConfiguration(self, value: AccelerateConfiguration):
        return self._set_property(self.AccelerateConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def AccessControl(self, value: str):
        return self._set_property(self.AccessControl.__name__, value)

    @Validator.validate(type=AnalyticsConfiguration, required_properties=ModelRequiredProperties.ANALYTICS_CONFIGURATION)
    def AnalyticsConfigurations(self, *value: AnalyticsConfiguration):
        return self._set_property(self.AnalyticsConfigurations.__name__, [ac.__to_dict__() for ac in list(value)])

    @Validator.validate(type=BucketEncryption, required_properties=ModelRequiredProperties.BUCKET_ENCRYPTION)
    def BucketEncryption(self, value: BucketEncryption):
        return self._set_property(self.BucketEncryption.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def BucketName(self, value: str):
        return self._set_property(self.BucketName.__name__, value)

    @Validator.validate(type=CorsConfiguration, required_properties=ModelRequiredProperties.CORS_CONFIGURATION)
    def CorsConfiguration(self, value: CorsConfiguration):
        return self._set_property(self.CorsConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=InventoryConfiguration, required_properties=ModelRequiredProperties.INVENTORY_CONFIGURATION)
    def InventoryConfigurations(self, *value: InventoryConfiguration):
        return self._set_property(self.InventoryConfigurations.__name__, [ic.__to_dict__() for ic in list(value)])

    @Validator.validate(type=LifecycleConfiguration, required_properties=ModelRequiredProperties.LIFECYCLE_CONFIGURATION)
    def LifecycleConfiguration(self, value: LifecycleConfiguration):
        return self._set_property(self.LifecycleConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=LoggingConfiguration)
    def LoggingConfiguration(self, value: LoggingConfiguration):
        return self._set_property(self.LoggingConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=MetricsConfiguration, required_properties=ModelRequiredProperties.METRICS_CONFIGURATION)
    def MetricsConfigurations(self, *value: MetricsConfiguration):
        return self._set_property(self.MetricsConfigurations.__name__, [mc.__to_dict__() for mc in list(value)])

    @Validator.validate(type=NotificationConfiguration)
    def NotificationConfiguration(self, value: NotificationConfiguration):
        return self._set_property(self.NotificationConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=ObjectLockConfiguration)
    def ObjectLockConfiguration(self, value: ObjectLockConfiguration):
        return self._set_property(self.ObjectLockConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=bool)
    def ObjectLockEnabled(self, value: bool):
        return self._set_property(self.ObjectLockEnabled.__name__, value)

    @Validator.validate(type=PublicAccessBlockConfiguration)
    def PublicAccessBlockConfiguration(self, value: PublicAccessBlockConfiguration):
        return self._set_property(self.PublicAccessBlockConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=ReplicationConfiguration, required_properties=ModelRequiredProperties.REPLICATION_CONFIGURATION)
    def ReplicationConfiguration(self, value: ReplicationConfiguration):
        return self._set_property(self.ReplicationConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=VersioningConfiguration, required_properties=ModelRequiredProperties.VERSIONING_CONFIGURATION)
    def VersioningConfiguration(self, value: VersioningConfiguration):
        return self._set_property(self.VersioningConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=WebsiteConfiguration)
    def WebsiteConfiguration(self, value: WebsiteConfiguration):
        return self._set_property(self.WebsiteConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=Tag)
    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
