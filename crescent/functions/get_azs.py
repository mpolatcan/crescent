from .fn import Fn as AnyFn, FnSingleValue
from typing import Union


class GetAZs(FnSingleValue):
    def __init__(self):
        super(GetAZs, self).__init__(fn_name=GetAZs.__name__)

    def Value(self, value: Union[str, AnyFn]):
        return self._set_field(self.Value.__name__, value)
