from crescent.core import Model, Validator


class Ingress(Model):
    @Validator.validate(type=str)
    def CIDRIP(self, cidrip: str):
        return self._set_field(self.CIDRIP.__name__, cidrip)

    @Validator.validate(type=str)
    def EC2SecurityGroupId(self, ec2_security_group_id: str):
        return self._set_field(self.EC2SecurityGroupId.__name__, ec2_security_group_id)

    @Validator.validate(type=str)
    def EC2SecurityGroupName(self, ec2_security_group_name: str):
        return self._set_field(self.EC2SecurityGroupName.__name__, ec2_security_group_name)

    @Validator.validate(type=str)
    def EC2SecurityGroupOwnerId(self, ec2_security_group_owner_id: str):
        return self._set_field(self.EC2SecurityGroupOwnerId.__name__, ec2_security_group_owner_id)
