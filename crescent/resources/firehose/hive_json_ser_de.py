from crescent.core import Model
from crescent.functions import AnyFn
from typing import Union


class HiveJsonSerDe(Model):
    def TimestampFormats(self, *timestamp_fmts: Union[str, AnyFn]):
        return self._set_field(self.TimestampFormats.__name__, list(timestamp_fmts))
