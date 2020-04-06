from crescent.core import Model
from .server_side_encryption_rule import ServerSideEncryptionRule
from .constants import ModelRequiredProperties


class BucketEncryption(Model):
    def __init__(self):
        super(BucketEncryption, self).__init__(required_properties=ModelRequiredProperties.BUCKET_ENCRYPTION)

    def ServerSideEncryptionConfiguration(self, *server_side_encryption_rules: ServerSideEncryptionRule):
        return self._set_field(self.ServerSideEncryptionConfiguration.__name__, list(server_side_encryption_rules))
