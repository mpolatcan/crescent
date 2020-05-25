from .api import ApiFactory
from .api_gateway_managed_overrides import ApiGatewayManagedOverridesFactory
from .api_mapping import ApiMappingFactory
from .authorizer import AuthorizerFactory
from .deployment import DeploymentFactory
from .domain_name import DomainNameFactory
from .integration import IntegrationFactory
from .integration_response import IntegrationResponseFactory
from .model import ModelFactory
from .route import RouteFactory
from .route_response import RouteResponseFactory
from .stage import StageFactory
from .vpc_link import VpcLinkFactory


class ApiGatewayV2:
    Api = ApiFactory
    ApiGatewayManagedOverrides = ApiGatewayManagedOverridesFactory
    ApiMapping = ApiMappingFactory
    Authorizer = AuthorizerFactory
    Deployment = DeploymentFactory
    DomainName = DomainNameFactory
    Integration = IntegrationFactory
    IntegrationResponse = IntegrationResponseFactory
    Model = ModelFactory
    Route = RouteFactory
    RouteResponse = RouteResponseFactory
    Stage = StageFactory
    VpcLink = VpcLinkFactory


__all__ = ["ApiGatewayV2"]
