from .tls_config import TlsConfig
from .integration import Integration
from .constants import ConnectionType, ContentHandlingStrategy, IntegrationType, PassthroughBehavior


class IntegrationFactory:
    ConnectionType = ConnectionType
    ContentHandlingStrategy = ContentHandlingStrategy
    IntegrationType = IntegrationType
    PassthroughBehavior = PassthroughBehavior

    @staticmethod
    def Create(id: str): return Integration(id)

    @staticmethod
    def TlsConfig(): return TlsConfig()


__all__ = ["IntegrationFactory"]
