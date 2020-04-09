from .fn import Fn


class Ref(Fn):
    def __init__(self, id: str):
        super(Ref, self).__init__(fn_name=Ref.__name__)
        self._set_fn_value(id)
