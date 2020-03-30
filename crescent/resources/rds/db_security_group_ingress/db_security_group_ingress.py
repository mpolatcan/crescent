from crescent.core import Resource, Validator


class DBSecurityGroupIngress(Resource):
    __TYPE = "AWS::RDS::DBSecurityGroupIngress"

    @Validator.validate(type=str)
    def __init__(self, id: str):
        super(DBSecurityGroupIngress, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def CIDRIP(self, cidrip: str):
        return self._set_property(self.CIDRIP.__name__, cidrip)

    @Validator.validate(type=str)
    def DBSecurityGroupName(self, db_security_group_name: str):
        return self._set_property(self.DBSecurityGroupName.__name__, db_security_group_name)

    @Validator.validate(type=str)
    def EC2SecurityGroupId(self, ec2_security_group_id: str):
        return self._set_property(self.EC2SecurityGroupId.__name__, ec2_security_group_id)

    @Validator.validate(type=str)
    def EC2SecurityGroupName(self, ec2_security_group_name: str):
        return self._set_property(self.EC2SecurityGroupName.__name__, ec2_security_group_name)

    @Validator.validate(type=str)
    def EC2SecurityGroupOwnerId(self, ec2_security_group_owner_id: str):
        return self._set_property(self.EC2SecurityGroupOwnerId.__name__, ec2_security_group_owner_id)
