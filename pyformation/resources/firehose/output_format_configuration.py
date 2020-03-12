from pyformation import PyformationModel
from .serializer import Serializer


class OutputFormatConfiguration(PyformationModel):
    def Serializer(self, value: Serializer):
        return self._set_field(self.Serializer.__name__, value.__to_dict__())
