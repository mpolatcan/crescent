from crescent.core import Model
from .constants import AllowedValues


class AttributeDefinition(Model):
    def __init__(self):
        super(AttributeDefinition, self).__init__(
            min_length={self.AttributeName.__name__: 1},
            max_length={self.AttributeName.__name__: 255},
            allowed_values={
                self.AttributeType.__name__: AllowedValues.ATTRIBUTE_TYPE
            }
        )

    def AttributeName(self, attr_name: str):
        return self._set_field(self.AttributeName.__name__, attr_name)

    def AttributeType(self, attr_type: str):
        return self._set_field(self.AttributeType.__name__, attr_type)
