from crescent.core import Model
from .constants import ModelRequiredProperties


class ProvisionedThroughput(Model):
    def __init__(self):
        super(ProvisionedThroughput, self).__init__(
            required_properties=ModelRequiredProperties.PROVISIONED_THROUGHPUT
        )

    def ReadCapacityUnits(self, read_capacity_units: int):
        return self._set_field(self.ReadCapacityUnits.__name__, read_capacity_units)

    def WriteCapacityUnits(self, write_capacity_units: int):
        return self._set_field(self.WriteCapacityUnits.__name__, write_capacity_units)
