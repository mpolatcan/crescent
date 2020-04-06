from .core import (
    Region,
    Zone,
    Template,
    ResourceAttributes,
    Parameter,
    ParameterTypes,
    Mapping,
    MappingKV,
    Tag
)
from .resources import *


# TODO Policy builder components will be added


class CrescentFactory:
    Region = Region
    Zone = Zone

    class Resource:
        CreationPolicy = ResourceAttributes.CreationPolicy
        DeletionPolicy = ResourceAttributes.DeletionPolicy
        UpdatePolicy = ResourceAttributes.UpdatePolicy
        UpdateReplacePolicy = ResourceAttributes.UpdateReplacePolicy

    class Parameter:
        Type = ParameterTypes

        @staticmethod
        def Create(id: str, data_type: Type):
            return Parameter(id, data_type)

    class Mapping:
        @staticmethod
        def Create(id: str):
            return Mapping(id)

        @staticmethod
        def KV(key: str, value: (int, str, list, dict)):
            return MappingKV().Key(key).Value(value)

    @staticmethod
    def Template(version: str = "2010-09-09"):
        return Template(version)

    @staticmethod
    def Tag(key: str, value: str):
        return Tag(key, value)


__all__ = [
    "CrescentFactory",
    "Ecr",
    "Efs",
    "Firehose",
    "Iam",
    "Kinesis",
    "Rds",
    "S3",
]
