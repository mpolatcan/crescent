from crescent.core import Resource
from .constants import ResourceRequiredProperties
from crescent.resources.api_gateway_v2.integration.constants import AllowedValues


class IntegrationResponse(Resource):
    __TYPE = "AWS::ApiGatewayV2::IntegrationResponse"

    def __init__(self, id: str):
        super(IntegrationResponse, self).__init__(
            id=id,
            type=self.__TYPE,
            required_properties=ResourceRequiredProperties.INTEGRATION_RESPONSE,
            allowed_values={self.ContentHandlingStrategy.__name__: AllowedValues.CONTENT_HANDLING_STRATEGY}
        )

    def ApiId(self, api_id: str):
        return self._set_property(self.ApiId.__name__, api_id)

    def ContentHandlingStrategy(self, content_handling_strategy: str):
        return self._set_property(self.ContentHandlingStrategy.__name__, content_handling_strategy)

    def IntegrationId(self, integration_id: str):
        return self._set_property(self.IntegrationId.__name__, integration_id)

    def IntegrationResponseKey(self, integration_response_key: str):
        return self._set_property(self.IntegrationResponseKey.__name__, integration_response_key)

    def ResponseParameters(self, response_parameters: dict):
        return self._set_property(self.ResponseParameters.__name__, response_parameters)

    def ResponseTemplates(self, response_templates: dict):
        return self._set_property(self.ResponseTemplates.__name__, response_templates)

    def TemplateSelectionExpression(self, template_selection_expr: str):
        return self._set_property(self.TemplateSelectionExpression.__name__, template_selection_expr)


