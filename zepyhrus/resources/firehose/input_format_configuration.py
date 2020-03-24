from zepyhrus.core import Model, Validator
from .deserializer import Deserializer


class InputFormatConfiguration(Model):
    @Validator.validate(type=Deserializer)
    def Deserializer(self, value: Deserializer):
        return self._set_field(self.Deserializer.__name__, value.__to_dict__())
