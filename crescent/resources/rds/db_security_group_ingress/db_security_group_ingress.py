from crescent.core import Resource
from .constants import ResourceRequiredProperties


class DBSecurityGroupIngress(Resource):
    __TYPE = "AWS::RDS::DBSecurityGroupIngress"

    def __init__(self, id: str):
        super(DBSecurityGroupIngress, self).__init__(
            id=id,
            type=self.__TYPE,
            required_properties=ResourceRequiredProperties.DB_SECURITY_GROUP_INGRESS
        )

    def CIDRIP(self, cidrip: str):
        return self._set_property(self.CIDRIP.__name__, cidrip)

    def DBSecurityGroupName(self, db_security_group_name: str):
        return self._set_property(self.DBSecurityGroupName.__name__, db_security_group_name)

    def EC2SecurityGroupId(self, ec2_security_group_id: str):
        return self._set_property(self.EC2SecurityGroupId.__name__, ec2_security_group_id)

    def EC2SecurityGroupName(self, ec2_security_group_name: str):
        return self._set_property(self.EC2SecurityGroupName.__name__, ec2_security_group_name)

    def EC2SecurityGroupOwnerId(self, ec2_security_group_owner_id: str):
        return self._set_property(self.EC2SecurityGroupOwnerId.__name__, ec2_security_group_owner_id)
