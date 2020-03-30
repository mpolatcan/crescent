from crescent.core import Model, Validator


class EncryptionConfiguration(Model):
    @Validator.validate(type=str)
    def ReplicaKmsKeyID(self, replica_kms_key_id: str):
        return self._set_field(self.ReplicaKmsKeyID.__name__, replica_kms_key_id)
