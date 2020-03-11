from pyformation.resources.shared import BaseCloudFormationResourceModel


class DBSecurityGroupIngress(BaseCloudFormationResourceModel):
    __TYPE = "AWS::RDS::DBSecurityGroupIngress"
    __PROPERTY_CIDRIP = "CIDRIP"
    __PROPERTY_DB_SECURITY_GROUP_NAME = "DBSecurityGroupName"
    __PROPERTY_EC2_SECURITY_GROUP_ID = "EC2SecurityGroupId"
    __PROPERTY_EC2_SECURITY_GROUP_NAME = "EC2SecurityGroupName"
    __PROPERTY_EC2_SECURITY_GROUP_OWNER_ID = "EC2SecurityGroupOwnerId"

    def __init__(self):
        super(DBSecurityGroupIngress, self).__init__(type=self.__TYPE)

    def cidrip(self, value: str):
        return self._add_property_field(self.__PROPERTY_CIDRIP, value)

    def db_security_group_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_DB_SECURITY_GROUP_NAME, value)

    def ec2_security_group_id(self, value: str):
        return self._add_property_field(self.__PROPERTY_EC2_SECURITY_GROUP_ID , value)

    def ec2_security_group_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_EC2_SECURITY_GROUP_NAME, value)

    def ec2_security_group_owner_id(self, value: str):
        return self._add_property_field(self.__PROPERTY_EC2_SECURITY_GROUP_OWNER_ID, value)
