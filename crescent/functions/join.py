from .fn import FnArrayValue


class Join(FnArrayValue):
    def __init__(self):
        super(Join, self).__init__(
            fn_name=Join.__name__,
            field_order=[self.Delimiter.__name__, self.Values.__name__]
        )

    def Values(self, *values: object):
        return self._set_field(self.Values.__name__, list(values))

    def Delimiter(self, delimiter: str):
        return self._set_field(self.Delimiter.__name__, delimiter)
