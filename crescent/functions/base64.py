from .fn import Fn


class Base64(Fn):
    def __init__(self, value):
        super(Base64, self).__init__(fn_name=Base64.__name__)
        self._set_fn_value(value)
