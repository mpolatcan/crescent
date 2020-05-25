from crescent.core import Resource
from .tls_config import TlsConfig
from .constants import ResourceRequiredProperties, AllowedValues


class Integration(Resource):
    __TYPE = "AWS::ApiGatewayV2::Integration"

    def __init__(self, id: str):
        super(Integration, self).__init__(
            id=id,
            type=self.__TYPE,
            allowed_values={
                self.ContentHandlingStrategy.__name__: AllowedValues.CONTENT_HANDLING_STRATEGY,
                self.ConnectionType.__name__: AllowedValues.CONNECTION_TYPE,
                self.IntegrationType.__name__: AllowedValues.INTEGRATION_TYPE,
                self.PassthroughBehavior.__name__: AllowedValues.PASSTHROUGH_BEHAVIOR
            },
            required_properties=ResourceRequiredProperties.INTEGRATION
        )

    def ApiId(self, api_id: str):
        return self._set_property(self.ApiId.__name__, api_id)

    def ConnectionId(self, connection_id: str):
        return self._set_property(self.ConnectionId.__name__, connection_id)

    def ConnectionType(self, connection_type: str):
        return self._set_property(self.ConnectionType.__name__, connection_type)

    def ContentHandlingStrategy(self, content_handling_strategy):
        return self._set_property(self.ContentHandlingStrategy.__name__, content_handling_strategy)

    # FIXME Add correct arn type to function definition
    def CredentialsArn(self, credentials_arn: str):
        return self._set_property(self.CredentialsArn.__name__, credentials_arn)

    def Description(self, description: str):
        return self._set_property(self.Description.__name__, description)

    def IntegrationMethod(self, integration_method: str):
        return self._set_property(self.IntegrationMethod.__name__, integration_method)

    def IntegrationType(self, integration_type: str):
        return self._set_property(self.IntegrationType.__name__, integration_type)

    def IntegrationUri(self, integration_uri: str):
        return self._set_property(self.IntegrationUri.__name__, integration_uri)

    def PassthroughBehavior(self, passthrough_behavior: str):
        return self._set_property(self.PassthroughBehavior.__name__, passthrough_behavior)

    def PayloadFormatVersion(self, payload_format_version: str):
        return self._set_property(self.PayloadFormatVersion.__name__, payload_format_version)

    def RequestParameters(self, request_parameters: dict):
        return self._set_property(self.RequestParameters.__name__, request_parameters)

    def RequestTemplates(self, request_templates: dict):
        return self._set_property(self.RequestTemplates.__name__, request_templates)

    def TemplateSelectionExpression(self, template_selection_expr: str):
        return self._set_property(self.TemplateSelectionExpression.__name__, template_selection_expr)

    def TimeoutInMillis(self, timeout_in_millis):
        return self._set_property(self.TimeoutInMillis.__name__, timeout_in_millis)

    def TlsConfig(self, tls_config: TlsConfig):
        return self._set_property(self.TlsConfig.__name__, tls_config)
