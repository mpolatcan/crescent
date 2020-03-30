from crescent.core import Resource, Tag, Validator
from .ingress import Ingress


class DBSecurityGroup(Resource):
    __TYPE = "AWS::RDS::DBSecurityGroup"

    def __init__(self, id: str):
        super(DBSecurityGroup, self).__init__(id, self.__TYPE)

    @Validator.validate(type=Ingress)
    def DBSecurityGroupIngress(self, *db_security_group_ingress: Ingress):
        return self._set_property(self.DBSecurityGroupIngress.__name__, [ing.__to_dict__() for ing in list(db_security_group_ingress)])

    @Validator.validate(type=str)
    def EC2VpcId(self, ec2_vpc_id: str):
        return self._set_property(self.EC2VpcId.__name__, ec2_vpc_id)

    @Validator.validate(type=str)
    def GroupDescription(self, group_description: str):
        return self._set_property(self.GroupDescription.__name__, group_description)

    @Validator.validate(type=Tag)
    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
