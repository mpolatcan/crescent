from .deployment import Deployment


class DeploymentFactory:
    @staticmethod
    def Create(id: str): return Deployment(id)


__all__ = ["DeploymentFactory"]
