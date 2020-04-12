from .fn import Fn as AnyFn, FnArrayValue
from typing import Union


class Join(FnArrayValue):
    def __init__(self):
        super(Join, self).__init__(
            fn_name=Join.__name__,
            field_order=[self.Delimiter.__name__, self.Values.__name__]
        )

    def Delimiter(self, delimiter: str):
        return self._set_field(self.Delimiter.__name__, delimiter)

    def Values(self, *values: Union[int, str, float, AnyFn]):
        return self._set_field(self.Values.__name__, list(values))
