from .repository import Repository
from .lifecycle_policy import LifecyclePolicy


class RepositoryFactory:
    @staticmethod
    def Create(id: str): return Repository(id)

    @staticmethod
    def LifecyclePolicy(): return LifecyclePolicy()


__all__ = ["RepositoryFactory"]
