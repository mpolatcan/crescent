from pyformation.resources.shared import BaseModel


class RedirectAllRequestTo(BaseModel):
    __PROPERTY_HOST_NAME = "HostName"
    __PROPERTY_PROTOCOL = "Protocol"

    def hostname(self, value: str):
        return self._add_field(self.__PROPERTY_HOST_NAME, value)

    def protocol(self, value: str):
        return self._add_field(self.__PROPERTY_PROTOCOL, value)
