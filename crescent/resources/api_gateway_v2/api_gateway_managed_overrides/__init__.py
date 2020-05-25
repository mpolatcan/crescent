from .integration_overrides import IntegrationOverrides
from .route_overrides import RouteOverrides
from .stage_overrides import StageOverrides
from crescent.resources.api_gateway_v2.common import (
    AccessLogSettings, RouteSettings, LoggingLevel
)
from .api_gateway_managed_overrides import ApiGatewayManagedOverrides


class ApiGatewayManagedOverridesFactory:
    LoggingLevel = LoggingLevel

    @staticmethod
    def Create(id: str): return ApiGatewayManagedOverrides(id)

    @staticmethod
    def AccessLogSettings(): return AccessLogSettings()

    @staticmethod
    def IntegrationOverrides(): return IntegrationOverrides()

    @staticmethod
    def RouteOverrides(): return RouteOverrides()

    @staticmethod
    def RouteSettings(): return RouteSettings()

    @staticmethod
    def StageOverrides(): return StageOverrides()


__all__ = ["ApiGatewayManagedOverridesFactory"]
