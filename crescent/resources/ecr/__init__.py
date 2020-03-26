from .repository import Repository
from .lifecycle_policy import LifecyclePolicy


class Ecr:
    @staticmethod
    def Repository(id: str):
        return Repository(id)

    @staticmethod
    def LifecyclePolicy():
        return LifecyclePolicy()


__all__ = [
    "Ecr"
]
