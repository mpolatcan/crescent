from pyformation.core import Model, Validator
from .server_side_encryption_rule import ServerSideEncryptionRule


class BucketEncryption(Model):
    __PROPERTY_SERVER_SIDE_ENCRYPTION_CONFIGURATION = "ServerSideEncryptionConfiguration"

    @Validator.validate(type=ServerSideEncryptionRule)
    def server_side_encryption_configuration(self, *value: ServerSideEncryptionRule):
        return self._set_field(self.__PROPERTY_SERVER_SIDE_ENCRYPTION_CONFIGURATION, [sser.__to_dict__() for sser in list(value)])
