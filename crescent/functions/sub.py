from .fn import FnArrayValue


class Sub(FnArrayValue):
    def __init__(self):
        super(Sub, self).__init__(
            fn_name=Sub.__name__,
            field_order=[self.String.__name__, self.Format.__name__]
        )

    def String(self, value: str):
        return self._set_field(self.String.__name__, value)

    def Format(self, **format: dict):
        return self._set_field(self.Format.__name__, format)
