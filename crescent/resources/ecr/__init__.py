from .repository import RepositoryFactory
from .arn import *


class Ecr:
    Arn = ArnFactory
    Repository = RepositoryFactory


__all__ = ["Ecr", "RepositoryArn"]
