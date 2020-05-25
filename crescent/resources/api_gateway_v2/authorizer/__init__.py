from .jwt_configuration import JWTConfiguration
from .authorizer import Authorizer
from .constants import AuthorizerType


class AuthorizerFactory:
    AuthorizerType = AuthorizerType

    @staticmethod
    def Create(id: str): return Authorizer(id)

    @staticmethod
    def JWTConfiguration(): return JWTConfiguration()


__all__ = ["AuthorizerFactory"]
