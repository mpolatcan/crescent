from crescent.core import Resource
from .constants import ResourceRequiredProperties


class RouteResponse(Resource):
    __TYPE = "AWS::ApiGatewayV2::RouteResponse"

    def __init__(self, id: str):
        super(RouteResponse, self).__init__(
            id=id,
            type=self.__TYPE,
            required_properties=ResourceRequiredProperties.ROUTE_RESPONSE
        )

    def ApiId(self, api_id: str):
        return self._set_property(self.ApiId.__name__, api_id)

    def ModelSelectionExpression(self, model_selection_expr: str):
        return self._set_property(self.ModelSelectionExpression.__name__, model_selection_expr)

    def ResponseModels(self, response_models: dict):
        return self._set_property(self.ResponseModels.__name__, response_models)

    def ResponseParameters(self, response_parameters: dict):
        return self._set_property(self.ResponseParameters.__name__, response_parameters)

    def RouteId(self, route_id: str):
        return self._set_property(self.RouteId.__name__, route_id)

    def RouteResponseKey(self, route_response_key: str):
        return self._set_property(self.RouteResponseKey.__name__, route_response_key)
