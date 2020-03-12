from .repository import Repository
from .lifecycle_policy import LifecyclePolicy


class EcrFactory:
    @staticmethod
    def Repository(id: str):
        return Repository(id)

    @staticmethod
    def LifecyclePolicy():
        return LifecyclePolicy()


__all__ = [
    "EcrFactory"
]
