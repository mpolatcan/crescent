from typing import List
from resources.shared import BaseCloudFormationResourceModel


class Policy(BaseCloudFormationResourceModel):
    __TYPE = "AWS::IAM::Policy"
    __PROPERTY_GROUPS = "Groups"
    __PROPERTY_POLICY_DOCUMENT = "PolicyDocument"
    __PROPERTY_POLICY_NAME = "PolicyName"
    __PROPERTY_ROLES = "Roles"
    __PROPERTY_USERS = "Users"

    def __init__(self):
        super(Policy, self).__init__(type=self.__TYPE)

    def groups(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_GROUPS, value)

    def policy_document(self, value: dict):
        return self._add_property_field(self.__PROPERTY_POLICY_DOCUMENT, value)

    def policy_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_POLICY_NAME, value)

    def roles(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_ROLES, value)

    def users(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_USERS, value)
