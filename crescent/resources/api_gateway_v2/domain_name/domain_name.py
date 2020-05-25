from crescent.core import Resource
from .constants import ResourceRequiredProperties
from .domain_name_configuration import DomainNameConfiguration


class DomainName(Resource):
    __TYPE = "AWS::ApiGatewayV2::DomainName"

    def __init__(self, id: str):
        super(DomainName, self).__init__(
            id=id,
            type=self.__TYPE,
            required_properties=ResourceRequiredProperties.DOMAIN_NAME
        )

    def DomainName(self, domain_name: str):
        return self._set_property(self.DomainName.__name__, domain_name)

    def DomainNameConfigurations(self, *domain_name_confs: DomainNameConfiguration):
        return self._set_property(self.DomainNameConfigurations.__name__, list(domain_name_confs))

    def Tags(self, tags: dict):
        return self._set_property(self.Tags.__name__, tags)
