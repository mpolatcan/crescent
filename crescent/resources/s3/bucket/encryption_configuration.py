from crescent.core import Model, Validator


class EncryptionConfiguration(Model):
    @Validator.validate(type=str)
    def ReplicaKmsKeyID(self, value: str):
        return self._set_field(self.ReplicaKmsKeyID.__name__, value)
