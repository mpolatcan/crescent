from .core import *
from .resources import *


class CrescentFactory:
    @staticmethod
    def Template(version: str = "2010-09-09"):
        return Template(version)

    @staticmethod
    def Mapping(id: str):
        return Mapping(id)

    @staticmethod
    def Parameter(id: str, data_type: Type):
        return Parameter(id, data_type)

    @staticmethod
    def Tag(key: str, value: str):
        return Tag(key, value)


__all__ = [
    "CrescentFactory",
    "Region",
    "Zone",
    "CreationPolicy",
    "DeletionPolicy",
    "UpdatePolicy",
    "UpdateReplacePolicy",
    "Types",
    "AwsTypes",
    "Ecr",
    "Efs",
    "Firehose",
    "Iam",
    "Kinesis",
    "Rds",
    "S3"
]
