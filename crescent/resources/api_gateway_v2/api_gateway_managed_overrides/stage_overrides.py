from crescent.core import Model
from crescent.resources.api_gateway_v2.common import AccessLogSettings, RouteSettings


class StageOverrides(Model):
    def __init__(self):
        super(StageOverrides, self).__init__()

    def AccessLogSettings(self, access_log_settings: AccessLogSettings):
        return self._set_field(self.AccessLogSettings.__name__, access_log_settings)

    def AutoDeploy(self, auto_deploy: bool):
        return self._set_field(self.AutoDeploy.__name__, auto_deploy)

    def DefaultRouteSettings(self, default_route_settings: RouteSettings):
        return self._set_field(self.DefaultRouteSettings.__name__, default_route_settings)

    def Description(self, description: str):
        return self._set_field(self.Description.__name__, description)

    def RouteSettings(self, route_settings: dict):
        return self._set_field(self.RouteSettings.__name__, route_settings)

    def StageVariables(self, stage_variables: dict):
        return self._set_field(self.StageVariables.__name__, stage_variables)
