from pyformation import PyformationModel
from .server_side_encryption_rule import ServerSideEncryptionRule


class BucketEncryption(PyformationModel):
    __PROPERTY_SERVER_SIDE_ENCRYPTION_CONFIGURATION = "ServerSideEncryptionConfiguration"

    def server_side_encryption_configuration(self, *value: ServerSideEncryptionRule):
        return self._set_field(self.__PROPERTY_SERVER_SIDE_ENCRYPTION_CONFIGURATION, [sser.__to_dict__() for sser in list(value)])
