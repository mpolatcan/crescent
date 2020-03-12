from pyformation import PyformationModel
from .deserializer import Deserializer


class InputFormatConfiguration(PyformationModel):
    def Deserializer(self, value: Deserializer):
        return self._set_field(self.Deserializer.__name__, value.__to_dict__())
