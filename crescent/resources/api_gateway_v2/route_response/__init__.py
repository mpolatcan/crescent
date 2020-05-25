from .route_response import RouteResponse


class RouteResponseFactory:
    @staticmethod
    def Create(id: str): return RouteResponse(id)


__all__ = ["RouteResponseFactory"]
