from crescent.core import Resource
from .constants import ResourceRequiredProperties


class ApiMapping(Resource):
    __TYPE = "AWS::ApiGatewayV2::ApiMapping"

    def __init__(self, id: str):
        super(ApiMapping, self).__init__(
            id=id,
            type=self.__TYPE,
            required_properties=ResourceRequiredProperties.API_MAPPING
        )

    def ApiId(self, api_id: str):
        return self._set_property(self.ApiId.__name__, api_id)

    def ApiMappingKey(self, api_mapping_key: str):
        return self._set_property(self.ApiMappingKey.__name__, api_mapping_key)

    def DomainName(self, domain_name: str):
        return self._set_property(self.DomainName.__name__, domain_name)

    def Stage(self, stage: str):
        return self._set_property(self.Stage.__name__, stage)