from .fn import Fn as AnyFn, FnArrayValue
from typing import Union


class Equals(FnArrayValue):
    def __init__(self):
        super(Equals, self).__init__(
            fn_name=Equals.__name__,
            field_order=[self.ValueFirst.__name__,
                         self.ValueSecond.__name__]
        )

    def ValueFirst(self, value_first: Union[str, AnyFn]):
        return self._set_field(self.ValueFirst.__name__, value_first)

    def ValueSecond(self, value_second: Union[str, AnyFn]):
        return self._set_field(self.ValueSecond.__name__, value_second)


