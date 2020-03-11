from pyformation.resources.shared import BaseCloudFormationResourceModel, Tag
from pyformation.resources.rds.db_security_group import Ingress


class DBSecurityGroup(BaseCloudFormationResourceModel):
    __TYPE = "AWS::RDS::DBSecurityGroup"
    __PROPERTY_DB_SECURITY_GROUP_INGRESS = "DBSecurityGroupIngress"
    __PROPERTY_EC2_VPC_ID = "EC2VpcId"
    __PROPERTY_GROUP_DESCRIPTION = "GroupDescription"
    __PROPERTY_TAGS = "Tags"

    def __init__(self):
        super(DBSecurityGroup, self).__init__(type=self.__TYPE)

    def db_security_group_ingress(self, *value: Ingress):
        return self._add_property_field(self.__PROPERTY_DB_SECURITY_GROUP_INGRESS, [
            ingress for ingress in list(value)
        ])

    def ec2_vpc_id(self, value: str):
        return self._add_property_field(self.__PROPERTY_EC2_VPC_ID, value)

    def group_description(self, value: str):
        return self._add_property_field(self.__PROPERTY_GROUP_DESCRIPTION, value)

    def tags(self, *value: Tag):
        return self._add_property_field(self.__PROPERTY_TAGS, [
            tag for tag in list(value)
        ])
