from .route import Route
from .constants import AuthorizationType


class RouteFactory:
    AuthorizationType = AuthorizationType

    @staticmethod
    def Create(id: str): return Route(id)


__all__ = ["RouteFactory"]
