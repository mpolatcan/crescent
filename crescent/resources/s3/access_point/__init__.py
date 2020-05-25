from .access_point import AccessPoint
from .vpc_configuration import VpcConfiguration
from .public_access_block_configuration import PublicAccessBlockConfiguration


class AccessPointFactory:
    @staticmethod
    def Create(id: str): return AccessPoint(id)

    @staticmethod
    def PublicAccessBlockConfiguration(): return PublicAccessBlockConfiguration()

    @staticmethod
    def VpcConfiguration(): return VpcConfiguration()


__all__ = ["AccessPointFactory"]
