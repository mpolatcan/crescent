from crescent.core import Model, Validator
from .server_side_encryption_by_default import ServerSideEncryptionByDefault
from .constants import ModelRequiredProperties


class ServerSideEncryptionRule(Model):
    @Validator.validate(type=ServerSideEncryptionByDefault, required_properties=ModelRequiredProperties.SERVER_SIDE_ENCRYPTION_BY_DEFAULT)
    def ServerSideEncryptionByDefault(self, value: ServerSideEncryptionByDefault):
        return self._set_field(self.ServerSideEncryptionByDefault.__name__, value.__to_dict__())
