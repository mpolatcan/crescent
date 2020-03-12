from pyformation import PyformationResource


class DBSecurityGroupIngress(PyformationResource):
    __TYPE = "AWS::RDS::DBSecurityGroupIngress"

    def __init__(self, id: str):
        super(DBSecurityGroupIngress, self).__init__(id, self.__TYPE)

    def CIDRIP(self, value: str):
        return self._set_property(self.CIDRIP.__name__, value)

    def DBSecurityGroupName(self, value: str):
        return self._set_property(self.DBSecurityGroupName.__name__, value)

    def EC2SecurityGroupId(self, value: str):
        return self._set_property(self.EC2SecurityGroupId.__name__, value)

    def EC2SecurityGroupName(self, value: str):
        return self._set_property(self.EC2SecurityGroupName.__name__, value)

    def EC2SecurityGroupOwnerId(self, value: str):
        return self._set_property(self.EC2SecurityGroupOwnerId.__name__, value)
