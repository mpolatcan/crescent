from zepyhrus.core import Resource, Validator


class DBSecurityGroupIngress(Resource):
    __TYPE = "AWS::RDS::DBSecurityGroupIngress"

    @Validator.validate(type=str)
    def __init__(self, id: str):
        super(DBSecurityGroupIngress, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def CIDRIP(self, value: str):
        return self._set_property(self.CIDRIP.__name__, value)

    @Validator.validate(type=str)
    def DBSecurityGroupName(self, value: str):
        return self._set_property(self.DBSecurityGroupName.__name__, value)

    @Validator.validate(type=str)
    def EC2SecurityGroupId(self, value: str):
        return self._set_property(self.EC2SecurityGroupId.__name__, value)

    @Validator.validate(type=str)
    def EC2SecurityGroupName(self, value: str):
        return self._set_property(self.EC2SecurityGroupName.__name__, value)

    @Validator.validate(type=str)
    def EC2SecurityGroupOwnerId(self, value: str):
        return self._set_property(self.EC2SecurityGroupOwnerId.__name__, value)
