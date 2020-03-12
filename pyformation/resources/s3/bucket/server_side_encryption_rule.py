from pyformation import PyformationModel
from .server_side_encryption_by_default import ServerSideEncryptionByDefault


class ServerSideEncryptionRule(PyformationModel):
    def ServerSideEncryptionByDefault(self, value: ServerSideEncryptionByDefault):
        return self._set_field(self.ServerSideEncryptionByDefault.__name__, value.__to_dict__())
