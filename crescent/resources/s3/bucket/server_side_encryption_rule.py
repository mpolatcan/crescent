from crescent.core import Model
from .server_side_encryption_by_default import ServerSideEncryptionByDefault


class ServerSideEncryptionRule(Model):
    def ServerSideEncryptionByDefault(self, server_side_encryption_by_default: ServerSideEncryptionByDefault):
        return self._set_field(self.ServerSideEncryptionByDefault.__name__, server_side_encryption_by_default)
