from pyformation.core import Model, Validator


class StreamEncryption(Model):
    @Validator.validate(type=str, allowed_values=["KMS"])
    def EncryptionType(self, value: str):
        return self._set_field(self.EncryptionType.__name__, value)

    @Validator.validate(type=str, min_length=1, max_length=2048)
    def KeyId(self, value: str):
        return self._set_field(self.KeyId.__name__, value)
