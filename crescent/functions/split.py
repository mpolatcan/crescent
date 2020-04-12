from .fn import Fn as AnyFn, FnArrayValue
from typing import Union


class Split(FnArrayValue):
    def __init__(self):
        super(Split, self).__init__(
            fn_name=Split.__name__,
            field_order=[self.Delimiter.__name__, self.SourceString.__name__]
        )

    def Delimiter(self, delimiter: str):
        return self._set_field(self.Delimiter.__name__, delimiter)

    def SourceString(self, source_str: Union[str, AnyFn]):
        return self._set_field(self.SourceString.__name__, source_str)
