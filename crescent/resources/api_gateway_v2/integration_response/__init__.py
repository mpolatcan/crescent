from .integration_response import IntegrationResponse
from crescent.resources.api_gateway_v2.integration.constants import ContentHandlingStrategy


class IntegrationResponseFactory:
    ContentHandlingStrategy = ContentHandlingStrategy

    @staticmethod
    def Create(id: str): return IntegrationResponse(id)


__all__ = ["IntegrationResponseFactory"]
