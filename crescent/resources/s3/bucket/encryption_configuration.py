from crescent.core import Model, Validator


class EncryptionConfiguration(Model):
    @Validator.validate(type=str)
    def ReplicaKmsKeyId(self, value: str):
        return self._set_field(self.ReplicaKmsKeyId.__name__, value)
