from crescent.core import Model
from .key_schema import KeySchema
from .projection import Projection
from .constants import ModelRequiredProperties


class LocalSecondaryIndex(Model):
    def __init__(self):
        super(LocalSecondaryIndex, self).__init__(
            min_length={self.IndexName.__name__: 3},
            max_length={self.IndexName.__name__: 255},
            pattern={self.IndexName.__name__: r"[a-zA-Z0-9_.-]+"},
            required_properties=ModelRequiredProperties.LOCAL_SECONDARY_INDEX
        )

    def IndexName(self, index_name: str):
        return self._set_field(self.IndexName.__name__, index_name)

    def KeySchema(self, *key_schema: KeySchema):
        return self._set_field(self.KeySchema.__name__, list(key_schema))

    def Projection(self, projection: Projection):
        return self._set_field(self.Projection.__name__, projection)
