from resources.shared import BaseModel
from resources.rds.option_group import OptionSetting


class OptionConfiguration(BaseModel):
    __PROPERTY_DB_SECURITY_GROUP_MEMBERSHIPS = "DBSecurityGroupMemberships"
    __PROPERTY_OPTION_NAME = "OptionName"
    __PROPERTY_OPTION_SETTINGS = "OptionSettings"
    __PROPERTY_OPTION_VERSION = "OptionVersion"
    __PROPERTY_PORT = "Port"
    __PROPERTY_VPC_SECURITY_GROUP_MEMBERSHIPS = "VpcSecurityGroupMemberships"

    def db_security_group_memberships(self, *value: str):
        return self._add_field(self.__PROPERTY_DB_SECURITY_GROUP_MEMBERSHIPS, list(value))

    def option_name(self, value: str):
        return self._add_field(self.__PROPERTY_OPTION_NAME, value)

    def option_settings(self, *value: OptionSetting):
        return self._add_field(self.__PROPERTY_OPTION_SETTINGS, [
            option_setting.create() for option_setting in list(value)
        ])

    def option_version(self, value: str):
        return self._add_field(self.__PROPERTY_OPTION_VERSION, value)

    def port(self, value: int):
        return self._add_field(self.__PROPERTY_PORT, value)

    def vpc_security_group_memberships(self, *value: str):
        return self._add_field(self.__PROPERTY_VPC_SECURITY_GROUP_MEMBERSHIPS, list(value))
