from pyformation import PyformationModel


class EncryptionConfiguration(PyformationModel):
    def ReplicaKmsKeyId(self, value: str):
        return self._set_field(self.ReplicaKmsKeyId.__name__, value)
