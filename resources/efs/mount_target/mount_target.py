from typing import List
from resources.shared.base_cf_resource_model import BaseCloudFormationResourceModel


class MountTarget(BaseCloudFormationResourceModel):
    __TYPE = "AWS::EFS::MountTarget"
    __PROPERTY_FILE_SYSTEM_ID = "FileSystemId"
    __PROPERTY_IP_ADDRESS = "IpAddress"
    __PROPERTY_SECURITY_GROUPS = "SecurityGroups"
    __PROPERTY_SUBNET_ID = "SubnetId"

    def file_system_id(self, value: str):
        return self._add_property_field(self.__PROPERTY_FILE_SYSTEM_ID, value)

    def ip_address(self, value: str):
        return self._add_property_field(self.__PROPERTY_IP_ADDRESS, value)

    def security_groups(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_SECURITY_GROUPS, value)

    def subnet_id(self, value: str):
        return self._add_property_field(self.__PROPERTY_SUBNET_ID, value)