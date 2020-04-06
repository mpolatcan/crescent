from crescent.core import Resource, Tag
from .ingress import Ingress
from .constants import ResourceRequiredProperties


class DBSecurityGroup(Resource):
    __TYPE = "AWS::RDS::DBSecurityGroup"

    def __init__(self, id: str):
        super(DBSecurityGroup, self).__init__(
            id=id,
            type=self.__TYPE,
            required_properties=ResourceRequiredProperties.DB_SECURITY_GROUP
        )

    def DBSecurityGroupIngress(self, *db_security_group_ingress: Ingress):
        return self._set_property(self.DBSecurityGroupIngress.__name__, list(db_security_group_ingress))

    def EC2VpcId(self, ec2_vpc_id: str):
        return self._set_property(self.EC2VpcId.__name__, ec2_vpc_id)

    def GroupDescription(self, group_description: str):
        return self._set_property(self.GroupDescription.__name__, group_description)

    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
