from resources.shared import BaseModel


class Ingress(BaseModel):
    __PROPERTY_CIDRIP = "CIDRIP"
    __PROPERTY_EC2_SECURITY_GROUP_ID = "EC2SecurityGroupId"
    __PROPERTY_EC2_SECURITY_GROUP_NAME = "EC2SecurityGroupName"
    __PROPERTY_EC2_SECURITY_GROUP_OWNER_ID = "EC2SecurityGroupOwnerId"

    def cidrip(self, value: str):
        return self._add_field(self.__PROPERTY_CIDRIP, value)

    def ec2_security_group_id(self, value: str):
        return self._add_field(self.__PROPERTY_EC2_SECURITY_GROUP_ID , value)

    def ec2_security_group_name(self, value: str):
        return self._add_field(self.__PROPERTY_EC2_SECURITY_GROUP_NAME, value)

    def ec2_security_group_owner_id(self, value: str):
        return self._add_field(self.__PROPERTY_EC2_SECURITY_GROUP_OWNER_ID, value)
