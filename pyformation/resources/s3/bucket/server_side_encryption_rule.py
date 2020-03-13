from pyformation.core import Model, Validator
from .server_side_encryption_by_default import ServerSideEncryptionByDefault


class ServerSideEncryptionRule(Model):
    @Validator.validate(type=ServerSideEncryptionByDefault)
    def ServerSideEncryptionByDefault(self, value: ServerSideEncryptionByDefault):
        return self._set_field(self.ServerSideEncryptionByDefault.__name__, value.__to_dict__())
