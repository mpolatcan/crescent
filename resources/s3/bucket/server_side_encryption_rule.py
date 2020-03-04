from resources.shared.base_model import BaseModel
from resources.s3.bucket.server_side_encryption_by_default import ServerSideEncryptionByDefault


class ServerSideEncryptionRule(BaseModel):
    __PROPERTY_SERVER_SIDE_ENCRYPTION_BY_DEFAULT = "ServerSideEncryptionByDefault"

    def server_side_encryption_by_default(self, value: ServerSideEncryptionByDefault):
        return self._add_field(self.__PROPERTY_SERVER_SIDE_ENCRYPTION_BY_DEFAULT, value.create())
