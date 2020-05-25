from crescent.core import Model
from .deserializer import Deserializer
from .constants import ModelRequiredProperties


class InputFormatConfiguration(Model):
    def __init__(self):
        super(InputFormatConfiguration, self).__init__(
            required_properties=ModelRequiredProperties.INPUT_FORMAT_CONFIGURATION
        )

    def Deserializer(self, deserializer: Deserializer):
        return self._set_field(self.Deserializer.__name__, deserializer)
