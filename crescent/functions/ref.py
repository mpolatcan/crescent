from .fn import FnSingleValue


class Ref(FnSingleValue):
    def __init__(self):
        super(Ref, self).__init__(fn_name=Ref.__name__)

    def Value(self, value: str):
        return self._set_field(self.Value.__name__, value)
