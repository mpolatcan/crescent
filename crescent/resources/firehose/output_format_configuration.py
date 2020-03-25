from crescent.core import Model, Validator
from .serializer import Serializer


class OutputFormatConfiguration(Model):
    @Validator.validate(type=Serializer)
    def Serializer(self, value: Serializer):
        return self._set_field(self.Serializer.__name__, value.__to_dict__())
