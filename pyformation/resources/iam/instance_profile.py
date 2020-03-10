from pyformation.resources.shared import BaseCloudFormationResourceModel


class InstanceProfile(BaseCloudFormationResourceModel):
    __TYPE = "AWS::IAM::InstanceProfile"
    __PROPERTY_INSTANCE_PROFILE_NAME = "InstanceProfileName"
    __PROPERTY_PATH = "Path"
    __PROPERTY_ROLES = "Roles"

    def __init__(self):
        super(InstanceProfile, self).__init__(type=self.__TYPE)

    def instance_profile_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_INSTANCE_PROFILE_NAME, value)

    def path(self, value: str):
        return self._add_property_field(self.__PROPERTY_PATH, value)

    def roles(self, *value: str):
        return self._add_property_field(self.__PROPERTY_ROLES, list(value))
