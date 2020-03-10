from pyformation.resources.shared import BaseModel


class EncryptionConfiguration(BaseModel):
    __PROPERTY_REPLICA_KMS_KEY_ID = "ReplicaKmsKeyId"

    def replica_kms_key_id(self, value: str):
        return self._add_field(self.__PROPERTY_REPLICA_KMS_KEY_ID, value)
