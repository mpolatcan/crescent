from crescent.core import Model
from .key_schema import KeySchema
from .projection import Projection
from .provisioned_throughput import ProvisionedThroughput
from .constants import ModelRequiredProperties


class GlobalSecondaryIndex(Model):
    def __init__(self):
        super(GlobalSecondaryIndex, self).__init__(
            min_length={self.IndexName.__name__: 3},
            max_length={self.IndexName.__name__: 255},
            pattern={self.IndexName.__name__: r"[a-zA-Z0-9_.-]+"},
            required_properties=ModelRequiredProperties.GLOBAL_SECONDARY_INDEX
        )

    def IndexName(self, index_name: str):
        return self._set_field(self.IndexName.__name__, index_name)

    def KeySchema(self, *key_schema: KeySchema):
        return self._set_field(self.KeySchema.__name__, list(key_schema))

    def Projection(self, projection: Projection):
        return self._set_field(self.Projection.__name__, projection)

    def ProvisionedThroughput(self, provisioned_throughput: ProvisionedThroughput):
        return self._set_field(self.ProvisionedThroughput.__name__, provisioned_throughput)
