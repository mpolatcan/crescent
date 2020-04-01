from .repository import Repository
from .lifecycle_policy import LifecyclePolicy
from .arn import RepositoryArn


class Ecr:
    @staticmethod
    def Repository(id: str):
        return Repository(id)

    @staticmethod
    def LifecyclePolicy():
        return LifecyclePolicy()

    @staticmethod
    def RepositoryArn(repository_name: str,
                      partition: str = "aws",
                      region: str = "",
                      account_id: str = ""):
        return RepositoryArn(
            repository_name=repository_name,
            partition=partition,
            region=region,
            account_id=account_id
        )


__all__ = [
    "Ecr",
    "RepositoryArn"
]
