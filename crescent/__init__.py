from .core import *
from .resources import (
    Ecr as ecr,
    Efs as efs,
    Firehose as firehose,
    Iam as iam,
    Kinesis as kinesis,
    Rds as rds,
    S3 as s3
)

# TODO Policy builder components will be added


class CrescentFactory:
    Region = Region
    Zone = Zone
    Types = Types
    CreationPolicy = ResourceAttributes.CreationPolicy
    DeletionPolicy = ResourceAttributes.DeletionPolicy
    UpdatePolicy = ResourceAttributes.UpdatePolicy
    UpdateReplacePolicy = ResourceAttributes.UpdateReplacePolicy

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
    "ecr",
    "efs",
    "firehose",
    "iam",
    "kinesis",
    "rds",
    "s3",
    "actions"
]
