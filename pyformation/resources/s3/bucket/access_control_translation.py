from pyformation.resources.shared import BaseModel


class AccessControlTranslation(BaseModel):
    __PROPERTY_OWNER = "Owner"

    def owner(self, value: str):
        return self._add_field(self.__PROPERTY_OWNER, value)
