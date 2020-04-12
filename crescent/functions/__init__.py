from .fn import Fn as AnyFn
from .ref import Ref as FnRef
from .base64 import Base64 as FnBase64
from .find_in_map import FindInMap as FnFindInMap
from .get_att import GetAtt as FnGetAtt
from .get_azs import GetAZs as FnGetAZs
from .import_value import ImportValue as FnImportValue
from .split import Split as FnSplit
from .join import Join as FnJoin
from .sub import Sub as FnSub
from .cidr import Cidr as FnCidr
from .select import Select as FnSelect
from .condition import Equals as FnEquals
from typing import Union


class FnFactory:
    @staticmethod
    def Base64(value: Union[str, AnyFn]):
        return FnBase64().Value(value)

    @staticmethod
    def Cidr():
        return FnCidr()

    @staticmethod
    def GetAtt():
        return FnGetAtt()

    @staticmethod
    def GetAZs(region: Union[str, FnRef]):
        return FnGetAZs().Value(region)

    @staticmethod
    def ImportValue(import_value: str):
        return FnImportValue().Value(import_value)

    @staticmethod
    def Join():
        return FnJoin()

    @staticmethod
    def Select():
        return FnSelect()

    @staticmethod
    def Split():
        return FnSplit()

    @staticmethod
    def Ref(id: str):
        return FnRef().Value(id)

    @staticmethod
    def Sub():
        return FnSub()

    @staticmethod
    def FindInMap():
        return FnFindInMap()

    @staticmethod
    def Equals(val1: Union[str, FnRef], val2: Union[str, FnRef]):
        return FnEquals().ValueFirst(val1).ValueSecond(val2)


__all__ = [
    "FnFactory",
    "AnyFn",
    "FnRef"
]
