from crescent.core import Resource
from .integration_overrides import IntegrationOverrides
from .route_overrides import RouteOverrides
from .stage_overrides import StageOverrides


class ApiGatewayManagedOverrides(Resource):
    __TYPE = "AWS::ApiGatewayV2::ApiGatewayManagedOverrides"

    def __init__(self, id: str):
        super(ApiGatewayManagedOverrides, self).__init__(id=id, type=self.__TYPE)

    def ApiId(self, api_id: str):
        return self._set_property(self.ApiId.__name__, api_id)

    def Integration(self, integration: IntegrationOverrides):
        return self._set_property(self.Integration.__name__, integration)

    def Route(self, route: RouteOverrides):
        return self._set_property(self.Route.__name__, route)

    def Stage(self, stage: StageOverrides):
        return self._set_property(self.Stage.__name__, stage)