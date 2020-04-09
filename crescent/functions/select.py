from .fn import FnArrayValue


class Select(FnArrayValue):
    def __init__(self):
        super(Select, self).__init__(
            fn_name=Select.__name__,
            field_order=[self.Index.__name__, self.Values.__name__]
        )

    def Index(self, index: int):
        return self._set_field(self.Index.__name__, index)

    def Values(self, *values: object):
        return self._set_field(self.Values.__name__, list(values))