from pyformation.resources.shared import BaseModel


class VersioningConfiguration(BaseModel):
    __PROPERTY_STATUS = "Status"

    def status(self, value: str):
        return self._add_field(self.__PROPERTY_STATUS, value)