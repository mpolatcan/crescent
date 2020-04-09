from .core import (
    Region,
    Zone,
    Template,
    ResourceAttributes,
    Parameter,
    ParameterTypes,
    Mapping,
    Output,
    Metadata,
    CfnAuthentication,
    CfnInterface,
    ParameterLabel,
    ParameterGroup,
    Label,
    Tag
)
from .resources import *
from .functions import *


# TODO Policy builder components will be added


class CrescentFactory:
    Region = Region
    Zone = Zone

    class ResourceAttrs:
        CreationPolicy = ResourceAttributes.CreationPolicy
        DeletionPolicy = ResourceAttributes.DeletionPolicy
        UpdatePolicy = ResourceAttributes.UpdatePolicy
        UpdateReplacePolicy = ResourceAttributes.UpdateReplacePolicy

    class Parameter:
        Type = ParameterTypes

        @staticmethod
        def Create(id: str, data_type: Type):
            return Parameter(id, data_type)

    class Metadata:
        @staticmethod
        def Create():
            return Metadata()

        class CfnAuthentication:
            @staticmethod
            def Create(id: str):
                return CfnAuthentication(id)

        class CfnInterface:
            @staticmethod
            def Create(id: str):
                return CfnInterface(id)

            @staticmethod
            def ParameterLabel(id: str):
                return ParameterLabel(id)

            @staticmethod
            def ParameterGroup():
                return ParameterGroup()

            @staticmethod
            def Label():
                return Label()

    class Fn:
        @staticmethod
        def Base64(value):
            return Base64(value)

        @staticmethod
        def Cidr():
            return Cidr()

        @staticmethod
        def GetAtt():
            return GetAtt()

        @staticmethod
        def GetAZs(region: str):
            return GetAZs(region)

        @staticmethod
        def ImportValue(import_value: str):
            return ImportValue(import_value)

        @staticmethod
        def Join():
            return Join()

        @staticmethod
        def Select():
            return Select()

        @staticmethod
        def Split():
            return Split()

        @staticmethod
        def Ref(id: str):
            return Ref(id)

        @staticmethod
        def Sub():
            return Sub()

        @staticmethod
        def FindInMap():
            return FindInMap()

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
