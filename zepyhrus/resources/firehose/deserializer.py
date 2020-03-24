from zepyhrus.core import Model, Validator
from .hive_json_ser_de import HiveJsonSerDe
from .openx_json_ser_de import OpenXJsonSerDe


class Deserializer(Model):
    @Validator.validate(type=HiveJsonSerDe)
    def HiveJsonSerDe(self, value: HiveJsonSerDe):
        return self._set_field(self.HiveJsonSerDe.__name__, value.__to_dict__())

    @Validator.validate(type=OpenXJsonSerDe)
    def OpenXJsonSerDe(self, value: OpenXJsonSerDe):
        return self._set_field(self.OpenXJsonSerDe.__name__, value.__to_dict__())
