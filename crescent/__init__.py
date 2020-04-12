from .core import (
    Region,
    Zone,
    Template,
    ResourceAttributesFactory,
    Parameter,
    ParameterType,
    ParameterTypes,
    Mapping,
    Output,
    Condition,
    MetadataFactory,
    Tag
)
from .resources import *
from .functions import AnyFn as AnyFn, FnFactory


# TODO Policy builder components will be added


class CrescentFactory:
    Region = Region
    Zone = Zone
    Metadata = MetadataFactory
    Fn = FnFactory

    class ResourceAttrs:
        CreationPolicy = ResourceAttributesFactory.CreationPolicy
        DeletionPolicy = ResourceAttributesFactory.DeletionPolicy
        UpdatePolicy = ResourceAttributesFactory.UpdatePolicy
        UpdateReplacePolicy = ResourceAttributesFactory.UpdateReplacePolicy

    class Parameter:
        Type = ParameterTypes

        @staticmethod
        def Create(id: str, data_type: ParameterType):
            return Parameter(id, data_type)

    @staticmethod
    def Condition(id: str, fn: AnyFn):
        return Condition(id).Fn(fn)

    @staticmethod
    def Mapping(id: str):
        return Mapping(id)

    @staticmethod
    def Output(id: str):
        return Output(id)

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
    "S3"
]
