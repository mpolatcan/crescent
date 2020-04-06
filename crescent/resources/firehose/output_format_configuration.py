from crescent.core import Model
from .serializer import Serializer
from .constants import ModelRequiredProperties


class OutputFormatConfiguration(Model):
    def __init__(self):
        super(OutputFormatConfiguration, self).__init__(
            required_properties=ModelRequiredProperties.OUTPUT_FORMAT_CONFIGURATION
        )

    def Serializer(self, serializer: Serializer):
        return self._set_field(self.Serializer.__name__, serializer)
