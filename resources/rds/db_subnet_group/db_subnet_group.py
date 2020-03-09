from typing import List
from resources.shared import BaseCloudFormationResourceModel, Tag


class DBSubnetGroup(BaseCloudFormationResourceModel):
    __TYPE = "AWS::RDS::DBSubnetGroup"
    __PROPERTY_DB_SUBNET_GROUP_DESCRIPTION = "DBSubnetGroupDescription"
    __PROPERTY_DB_SUBNET_GROUP_NAME = "DBSubnetGroupName"
    __PROPERTY_SUBNET_IDS = "SubnetIds"
    __PROPERTY_TAGS = "Tags"

    def __init__(self):
        super(DBSubnetGroup, self).__init__(type=self.__TYPE)

    def db_subnet_group_description(self, value: str):
        return self._add_property_field(self.__PROPERTY_DB_SUBNET_GROUP_DESCRIPTION, value)

    def db_subnet_group_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_DB_SUBNET_GROUP_NAME, value)

    def subnet_ids(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_SUBNET_IDS, value)

    def tags(self, value: List[Tag]):
        return self._add_property_field(self.__PROPERTY_TAGS, [
            tag.create() for tag in value
        ])
