from crescent.core import Model, Validator
from .server_side_encryption_rule import ServerSideEncryptionRule


class BucketEncryption(Model):
    @Validator.validate(type=ServerSideEncryptionRule)
    def ServerSideEncryptionConfiguration(self, *server_side_encryption_rules: ServerSideEncryptionRule):
        return self._set_field(self.ServerSideEncryptionConfiguration.__name__, [sser.__to_dict__() for sser in list(server_side_encryption_rules)])
