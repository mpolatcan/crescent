from crescent.core import Model, Validator


class Ingress(Model):
    @Validator.validate(type=str)
    def CIDRIP(self, value: str):
        return self._set_field(self.CIDRIP.__name__, value)

    @Validator.validate(type=str)
    def EC2SecurityGroupId(self, value: str):
        return self._set_field(self.EC2SecurityGroupId.__name__, value)

    @Validator.validate(type=str)
    def EC2SecurityGroupName(self, value: str):
        return self._set_field(self.EC2SecurityGroupName.__name__, value)

    @Validator.validate(type=str)
    def EC2SecurityGroupOwnerId(self, value: str):
        return self._set_field(self.EC2SecurityGroupOwnerId.__name__, value)
