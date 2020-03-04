from resources.shared.base_cf_resource_model import BaseCloudFormationResourceModel
from typing import List


class ManagedPolicy(BaseCloudFormationResourceModel):
    __TYPE = "AWS::IAM::ManagedPolicy"
    __PROPERTY_DESCRIPTION = "Description"
    __PROPERTY_GROUPS = "Groups"
    __PROPERTY_MANAGED_POLICY_NAME = "ManagedPolicyName"
    __PROPERTY_PATH = "Path"
    __PROPERTY_POLICY_DOCUMENT = "PolicyDocument"
    __PROPERTY_ROLES = "Roles"
    __PROPERTY_USERS = "Users"

    def __init__(self):
        super(ManagedPolicy, self).__init__(type=self.__TYPE)

    def description(self, value: str):
        return self._add_property_field(self.__PROPERTY_DESCRIPTION, value)

    def groups(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_GROUPS, value)

    def managed_policy_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_MANAGED_POLICY_NAME, value)

    def path(self, value: str):
        return self._add_property_field(self.__PROPERTY_PATH, value)

    def roles(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_ROLES, value)

    def users(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_USERS, value)
