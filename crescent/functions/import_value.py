from .fn import Fn


class ImportValue(Fn):
    def __init__(self, import_value: str):
        super(ImportValue, self).__init__(fn_name=ImportValue.__name__)
        self._set_fn_value(import_value)
