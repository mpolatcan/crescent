from crescent.core import Model, Validator


class StreamEncryption(Model):
    @Validator.validate(type=str, allowed_values=["KMS"])
    def EncryptionType(self, encryption_type: str):
        return self._set_field(self.EncryptionType.__name__, encryption_type)

    @Validator.validate(type=str, min_length=1, max_length=2048)
    def KeyId(self, key_id: str):
        return self._set_field(self.KeyId.__name__, key_id)
