from typing import List
from resources.shared import BaseCloudFormationResourceModel


class UserToGroupAddition(BaseCloudFormationResourceModel):
    __TYPE = "AWS::IAM::UserToGroupAddition"
    __PROPERTY_GROUP_NAME = "GroupName"
    __PROPERTY_USERS = "Users"

    def __init__(self):
        super(UserToGroupAddition, self).__init__(type=self.__TYPE)

    def group_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_GROUP_NAME, value)

    def users(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_USERS, value)
