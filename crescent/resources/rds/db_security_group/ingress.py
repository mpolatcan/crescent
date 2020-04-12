from crescent.core import Model
from crescent.functions import AnyFn
from typing import Union


class Ingress(Model):
    def CIDRIP(self, cidrip: Union[str, AnyFn]):
        return self._set_field(self.CIDRIP.__name__, cidrip)

    def EC2SecurityGroupId(self, ec2_security_group_id: Union[str, AnyFn]):
        return self._set_field(self.EC2SecurityGroupId.__name__, ec2_security_group_id)

    def EC2SecurityGroupName(self, ec2_security_group_name: Union[str, AnyFn]):
        return self._set_field(self.EC2SecurityGroupName.__name__, ec2_security_group_name)

    def EC2SecurityGroupOwnerId(self, ec2_security_group_owner_id: Union[str, AnyFn]):
        return self._set_field(self.EC2SecurityGroupOwnerId.__name__, ec2_security_group_owner_id)
