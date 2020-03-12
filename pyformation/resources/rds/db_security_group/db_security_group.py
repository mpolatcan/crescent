from pyformation import PyformationResource, Tag
from .ingress import Ingress


class DBSecurityGroup(PyformationResource):
    __TYPE = "AWS::RDS::DBSecurityGroup"

    def __init__(self, id: str):
        super(DBSecurityGroup, self).__init__(id, self.__TYPE)

    def DBSecurityGroupIngress(self, *value: Ingress):
        return self._set_property(self.DBSecurityGroupIngress.__name__, [ing.__to_dict__() for ing in list(value)])

    def EC2VpcId(self, value: str):
        return self._set_property(self.EC2VpcId.__name__, value)

    def GroupDescription(self, value: str):
        return self._set_property(self.GroupDescription.__name__, value)

    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
