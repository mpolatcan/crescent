from crescent.core import Model
from .constants import ModelRequiredProperties, AllowedValues


class StreamSpecification(Model):
    def __init__(self):
        super(StreamSpecification, self).__init__(
            allowed_values={self.StreamViewType.__name__: AllowedValues.STREAM_VIEW_TYPE},
            required_properties=ModelRequiredProperties.STREAM_SPECIFICATION
        )

    def StreamViewType(self, stream_view_type: str):
        return self._set_field(self.StreamViewType.__name__, stream_view_type)
