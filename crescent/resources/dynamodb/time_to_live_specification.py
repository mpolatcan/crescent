from crescent.core import Model
from .constants import ModelRequiredProperties


class TimeToLiveSpecification(Model):
    def __init__(self):
        super(TimeToLiveSpecification, self).__init__(
            min_length={self.AttributeName.__name__: 1},
            max_length={self.AttributeName.__name__: 255},
            required_properties=ModelRequiredProperties.TIME_TO_LIVE_SPECIFICATION
        )

    def AttributeName(self, attribute_name: str):
        return self._set_field(self.AttributeName.__name__, attribute_name)

    def Enabled(self, enabled: bool):
        return self._set_field(self.Enabled.__name__, enabled)