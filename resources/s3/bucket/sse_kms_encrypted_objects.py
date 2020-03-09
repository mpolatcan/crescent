from resources.shared import BaseModel


class SseKmsEncryptedObjects(BaseModel):
    __PROPERTY_STATUS = "Status"

    def status(self, value: str):
        return self._add_field(self.__PROPERTY_STATUS, value)
