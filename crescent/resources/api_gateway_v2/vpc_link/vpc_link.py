from crescent.core import Resource
from .constants import ResourceRequiredProperties


class VpcLink(Resource):
    __TYPE = "AWS::ApiGatewayV2::VpcLink"

    def __init__(self, id: str):
        super(VpcLink, self).__init__(
            id=id,
            type=self.__TYPE,
            required_properties=ResourceRequiredProperties.VPC_LINK
        )

    def Name(self, name: str):
        return self._set_property(self.Name.__name__, name)

    def SecurityGroupIds(self, *security_group_ids: str):
        return self._set_property(self.SecurityGroupIds.__name__, list(security_group_ids))

    def SubnetIds(self, *subnet_ids: str):
        return self._set_property(self.SubnetIds.__name__, list(subnet_ids))

    def Tags(self, tags: dict):
        return self._set_property(self.Tags.__name__, tags)
