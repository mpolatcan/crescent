from .fn import Fn as AnyFn, FnSingleValue
from typing import Union


class Base64(FnSingleValue):
    def __init__(self):
        super(Base64, self).__init__(fn_name=Base64.__name__)

    def Value(self, value: Union[str, AnyFn]):
        return self._set_field(self.Value.__name__, value)
