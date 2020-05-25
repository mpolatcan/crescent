from crescent.core import Resource
from .jwt_configuration import JWTConfiguration
from .constants import AllowedValues, ResourceRequiredProperties


class Authorizer(Resource):
    __TYPE = "AWS::ApiGatewayV2::Authorizer"

    def __init__(self, id: str):
        super(Authorizer, self).__init__(
            id=id,
            type=self.__TYPE,
            allowed_values={self.AuthorizerType.__name__: AllowedValues.AUTHORIZER_TYPE},
            required_properties=ResourceRequiredProperties.AUTHORIZER
        )

    def ApiId(self, api_id: str):
        return self._set_property(self.ApiId.__name__, api_id)

    # FIXME Add correct arn type to function definition
    def AuthorizerCredentialsArn(self, authorizer_credentials_arn: str):
        return self._set_property(self.AuthorizerCredentialsArn.__name__, authorizer_credentials_arn)

    def AuthorizerResultTtlInSeconds(self, authorizer_result_ttl_in_secs: int):
        return self._set_property(self.AuthorizerResultTtlInSeconds.__name__, authorizer_result_ttl_in_secs)

    def AuthorizerType(self, authorizer_type: str):
        return self._set_property(self.AuthorizerType.__name__, authorizer_type)

    def AuthorizerUri(self, authorizer_uri: str):
        return self._set_property(self.AuthorizerUri.__name__, authorizer_uri)

    def IdentitySource(self, *identity_source: str):
        return self._set_property(self.IdentitySource.__name__, list(identity_source))

    def IdentityValidationExpression(self, identity_validation_expr: str):
        return self._set_property(self.IdentityValidationExpression.__name__, identity_validation_expr)

    def JwtConfiguration(self, jwt_configuration: JWTConfiguration):
        return self._set_property(self.JwtConfiguration.__name__, jwt_configuration)

    def Name(self, name: str):
        return self._set_property(self.Name.__name__, name)