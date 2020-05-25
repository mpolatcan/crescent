from crescent.core import Resource
from crescent.resources.api_gateway_v2.common import AccessLogSettings, RouteSettings
from .constants import ResourceRequiredProperties


class Stage(Resource):
    __TYPE = "AWS::ApiGatewayV2::Stage"

    def __init__(self, id: str):
        super(Stage, self).__init__(
            id=id,
            type=self.__TYPE,
            required_properties=ResourceRequiredProperties.STAGE
        )

    def AccessLogSettings(self, access_log_settings: AccessLogSettings):
        return self._set_property(self.AccessLogSettings.__name__, access_log_settings)

    def ApiId(self, api_id: str):
        return self._set_property(self.ApiId.__name__, api_id)

    def AutoDeploy(self, auto_deploy: bool):
        return self._set_property(self.AutoDeploy.__name__, auto_deploy)

    def ClientCertificateId(self, client_certificate_id: str):
        return self._set_property(self.ClientCertificateId.__name__, client_certificate_id)

    def DefaultRouteSettings(self, default_route_settings: RouteSettings):
        return self._set_property(self.DefaultRouteSettings.__name__, default_route_settings)

    def DeploymentId(self, deployment_id: str):
        return self._set_property(self.DeploymentId.__name__, deployment_id)

    def Description(self, description: str):
        return self._set_property(self.Description.__name__, description)

    def RouteSettings(self, route_settings: dict):
        return self._set_property(self.RouteSettings.__name__, route_settings)

    def StageName(self, stage_name: str):
        return self._set_property(self.StageName.__name__, stage_name)

    def StageVariables(self, stage_variables: dict):
        return self._set_property(self.StageVariables.__name__, stage_variables)

    def Tags(self, tags: dict):
        return self._set_property(self.Tags.__name__, tags)
