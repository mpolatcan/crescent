from crescent.core import Model
from .hive_json_ser_de import HiveJsonSerDe
from .openx_json_ser_de import OpenXJsonSerDe


class Deserializer(Model):
    def HiveJsonSerDe(self, hive_json_ser_de: HiveJsonSerDe):
        return self._set_field(self.HiveJsonSerDe.__name__, hive_json_ser_de)

    def OpenXJsonSerDe(self, openx_json_ser_de: OpenXJsonSerDe):
        return self._set_field(self.OpenXJsonSerDe.__name__, openx_json_ser_de)
