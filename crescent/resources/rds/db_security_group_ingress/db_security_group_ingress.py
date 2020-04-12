from crescent.core import Resource
from crescent.functions import AnyFn
from .constants import ResourceRequiredProperties
from typing import Union


class DBSecurityGroupIngress(Resource):
    __TYPE = "AWS::RDS::DBSecurityGroupIngress"

    def __init__(self, id: str):
        super(DBSecurityGroupIngress, self).__init__(
            id=id,
            type=self.__TYPE,
            required_properties=ResourceRequiredProperties.DB_SECURITY_GROUP_INGRESS
        )

    def CIDRIP(self, cidrip: Union[str, AnyFn]):
        return self._set_property(self.CIDRIP.__name__, cidrip)

    def DBSecurityGroupName(self, db_security_group_name: Union[str, AnyFn]):
        return self._set_property(self.DBSecurityGroupName.__name__, db_security_group_name)

    def EC2SecurityGroupId(self, ec2_security_group_id: Union[str, AnyFn]):
        return self._set_property(self.EC2SecurityGroupId.__name__, ec2_security_group_id)

    def EC2SecurityGroupName(self, ec2_security_group_name: Union[str, AnyFn]):
        return self._set_property(self.EC2SecurityGroupName.__name__, ec2_security_group_name)

    def EC2SecurityGroupOwnerId(self, ec2_security_group_owner_id: Union[str, AnyFn]):
        return self._set_property(self.EC2SecurityGroupOwnerId.__name__, ec2_security_group_owner_id)
