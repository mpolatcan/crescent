from .fn import Fn


class GetAZs(Fn):
    def __init__(self, region: str):
        super(GetAZs, self).__init__(fn_name=GetAZs.__name__)
        self._set_fn_value(region)
