from crescent.core import Resource
from .body_s3_location import BodyS3Location
from .cors import Cors
from .constants import AllowedValues
from crescent.resources.iam import UserArn


class Api(Resource):
    __TYPE = "AWS::ApiGatewayV2::Api"

    def __init__(self, id: str):
        super(Api, self).__init__(
            id=id,
            type=self.__TYPE,
            allowed_values={self.BasePath.__name__: AllowedValues.BASE_PATH}
        )

    def ApiKeySelectionExpression(self, api_key_selection_expr: str):
        return self._set_property(self.ApiKeySelectionExpression.__name__, api_key_selection_expr)

    def BasePath(self, base_path: str):
        return self._set_property(self.BasePath.__name__, base_path)

    def Body(self, body: dict):
        return self._set_property(self.Body.__name__, body)

    def BodyS3Location(self, body_s3_location: BodyS3Location):
        return self._set_property(self.BodyS3Location.__name__, body_s3_location)

    def CorsConfiguration(self, cors_configuration: Cors):
        return self._set_property(self.CorsConfiguration.__name__, cors_configuration)

    def CredentialsArn(self, credentials_arn: UserArn):
        return self._set_property(self.CredentialsArn.__name__, credentials_arn)

    def Description(self, description: str):
        return self._set_property(self.Description.__name__, description)

    def DisableExecuteApiEndpoint(self, disable_execute_api_endpoint: bool):
        return self._set_property(self.DisableExecuteApiEndpoint.__name__, disable_execute_api_endpoint)

    def DisableSchemaValidation(self, disable_schema_validation: bool):
        return self._set_property(self.DisableSchemaValidation.__name__, disable_schema_validation)

    def FailOnWarnings(self, fail_on_warnings: bool):
        return self._set_property(self.FailOnWarnings.__name__, fail_on_warnings)

    def Name(self, name: str):
        return self._set_property(self.Name.__name__, name)

    def ProtocolType(self, protocol_type: str):
        return self._set_property(self.ProtocolType.__name__, protocol_type)

    def RouteKey(self, route_key: str):
        return self._set_property(self.RouteKey.__name__, route_key)

    def RouteSelectionExpression(self, route_selection_expr: str):
        return self._set_property(self.RouteSelectionExpression.__name__, route_selection_expr)

    def Tags(self, tags: dict):
        return self._set_property(self.Tags.__name__, tags)

    def Target(self, target: str):
        return self._set_property(self.Target.__name__, target)

    def Version(self, version: str):
        return self._set_property(self.Version.__name__, version)