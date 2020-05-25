from crescent.core import Model
from crescent.functions import AnyFn
from .constants import ModelRequiredProperties
from typing import Union


class KMSEncryptionConfig(Model):
    def __init__(self):
        super(KMSEncryptionConfig, self).__init__(
            min_length={self.AWSKMSKeyARN.__name__: 1},
            max_length={self.AWSKMSKeyARN.__name__: 512},
            pattern={self.AWSKMSKeyARN.__name__: r"arn:.*"},
            required_properties=ModelRequiredProperties.KMS_ENCRYPTION_CONFIG
        )

    def AWSKMSKeyARN(self, aws_kms_key_arn: Union[str, AnyFn]):
        return self._set_field(self.AWSKMSKeyARN.__name__, aws_kms_key_arn)
