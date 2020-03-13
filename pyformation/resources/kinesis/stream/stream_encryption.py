from pyformation.core import Model, Validator


class StreamEncryption(Model):
    @Validator.validate(type=str)
    def EncryptionType(self, value: str):
        return self._set_field(self.EncryptionType.__name__, value)

    @Validator.validate(type=str)
    def KeyId(self, value: str):
        return self._set_field(self.KeyId.__name__, value)
