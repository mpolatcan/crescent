from crescent.core import Model, Validator
from .serializer import Serializer


class OutputFormatConfiguration(Model):
    @Validator.validate(type=Serializer)
    def Serializer(self, serializer: Serializer):
        return self._set_field(self.Serializer.__name__, serializer.__to_dict__())
