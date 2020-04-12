from .fn import Fn as AnyFn, FnSingleValue
from typing import Union


class ImportValue(FnSingleValue):
    def __init__(self):
        super(ImportValue, self).__init__(fn_name=ImportValue.__name__)

    def Value(self, value: Union[str, AnyFn]):
        return self._set_field(self.Value.__name__, value)
