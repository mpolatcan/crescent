from crescent.core import Resource
from .constants import ResourceRequiredProperties, AllowedValues


class Route(Resource):
    __TYPE = "AWS::ApiGatewayV2::Route"

    def __init__(self, id: str):
        super(Route, self).__init__(
            id=id,
            type=self.__TYPE,
            allowed_values={self.AuthorizationType.__name__: AllowedValues.AUTHORIZATION_TYPE},
            required_properties=ResourceRequiredProperties.ROUTE
        )

    def ApiId(self, api_id: str):
        return self._set_property(self.ApiId.__name__, api_id)

    def ApiKeyRequired(self, api_key_required: bool):
        return self._set_property(self.ApiKeyRequired.__name__, api_key_required)

    def AuthorizationScopes(self, *authorization_scopes: str):
        return self._set_property(self.AuthorizationScopes.__name__, list(authorization_scopes))

    def AuthorizationType(self, authorization_type: str):
        return self._set_property(self.AuthorizationType.__name__, authorization_type)

    def AuthorizerId(self, authorizer_id: str):
        return self._set_property(self.AuthorizerId.__name__, authorizer_id)

    def ModelSelectionExpression(self, model_selection_expr: str):
        return self._set_property(self.ModelSelectionExpression.__name__, model_selection_expr)

    def OperationName(self, operation_name: str):
        return self._set_property(self.OperationName.__name__, operation_name)

    def RequestModels(self, request_models: dict):
        return self._set_property(self.RequestModels.__name__, request_models)

    def RequestParameters(self, request_parameters: dict):
        return self._set_property(self.RequestParameters.__name__, request_parameters)

    def RouteKey(self, route_key: str):
        return self._set_property(self.RouteKey.__name__, route_key)

    def RouteResponseSelectionExpression(self, route_response_selection_expr: str):
        return self._set_property(self.RouteResponseSelectionExpression.__name__, route_response_selection_expr)

    def Target(self, target: str):
        return self._set_property(self.Target.__name__, target)