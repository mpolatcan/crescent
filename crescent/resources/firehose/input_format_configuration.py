from crescent.core import Model, Validator
from .deserializer import Deserializer


class InputFormatConfiguration(Model):
    @Validator.validate(type=Deserializer)
    def Deserializer(self, deserializer: Deserializer):
        return self._set_field(self.Deserializer.__name__, deserializer.__to_dict__())
