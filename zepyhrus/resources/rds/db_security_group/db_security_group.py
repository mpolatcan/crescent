from zepyhrus.core import Resource, Tag, Validator
from .ingress import Ingress


class DBSecurityGroup(Resource):
    __TYPE = "AWS::RDS::DBSecurityGroup"

    def __init__(self, id: str):
        super(DBSecurityGroup, self).__init__(id, self.__TYPE)

    @Validator.validate(type=Ingress)
    def DBSecurityGroupIngress(self, *value: Ingress):
        return self._set_property(self.DBSecurityGroupIngress.__name__, [ing.__to_dict__() for ing in list(value)])

    @Validator.validate(type=str)
    def EC2VpcId(self, value: str):
        return self._set_property(self.EC2VpcId.__name__, value)

    @Validator.validate(type=str)
    def GroupDescription(self, value: str):
        return self._set_property(self.GroupDescription.__name__, value)

    @Validator.validate(type=Tag)
    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
