from crescent.core import Model
from .constants import ModelRequiredProperties, AllowedValues


class KeySchema(Model):
    def __init__(self):
        super(KeySchema, self).__init__(
            min_length={self.AttributeName.__name__: 1},
            max_length={self.AttributeName.__name__: 255},
            allowed_values={self.KeyType.__name__: AllowedValues.KEY_TYPE},
            required_propertieS=ModelRequiredProperties.KEY_SCHEMA
        )

    def AttributeName(self, attr_name: str):
        return self._set_field(self.AttributeName.__name__, attr_name)

    def KeyType(self, key_type: str):
        return self._set_field(self.KeyType.__name__, key_type)
