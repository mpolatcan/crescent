from pyformation.resources.shared import BaseCloudFormationResourceModel


class AccessKey(BaseCloudFormationResourceModel):
    __TYPE = "AWS::IAM::AccessKey"
    __PROPERTY_SERIAL = "Serial"
    __PROPERTY_STATUS = "Status"
    __PROPERTY_USERNAME = "UserName"

    def __init__(self):
        super(AccessKey, self).__init__(type=self.__TYPE)

    def serial(self, value: int):
        return self._add_property_field(self.__PROPERTY_SERIAL, value)

    def status(self, value: str):
        return self._add_property_field(self.__PROPERTY_STATUS, value)

    def username(self, value: str):
        return self._add_property_field(self.__PROPERTY_USERNAME, value)
