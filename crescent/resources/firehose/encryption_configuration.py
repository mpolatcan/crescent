from crescent.core import Model, Validator
from .kms_encryption_config import KMSEncryptionConfig
from .constants import ModelRequiredProperties


class EncryptionConfiguration(Model):
    @Validator.validate(type=KMSEncryptionConfig, required_properties=ModelRequiredProperties.KMS_ENCRYPTION_CONFIG)
    def KMSEncryptionConfig(self, value: KMSEncryptionConfig):
        return self._set_field(self.KMSEncryptionConfig.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def NoEncryptionConfig(self, value: str):
        return self._set_field(self.NoEncryptionConfig.__name__, value)
