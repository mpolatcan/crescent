from crescent.core import Model
from .destination import Destination
from .constants import AllowedValues, ModelRequiredProperties


class InventoryConfiguration(Model):
    def __init__(self):
        super(InventoryConfiguration, self).__init__(
            allowed_values={self.IncludedObjectVersions.__name__: AllowedValues.INCLUDED_OBJECT_VERSIONS,
                            self.ScheduleFrequency.__name__: AllowedValues.SCHEDULE_FREQUENCY},
            required_properties=ModelRequiredProperties.INVENTORY_CONFIGURATION
        )

    def Destination(self, destination: Destination):
        return self._set_field(self.Destination.__name__, destination.__to_dict__())

    def Enabled(self, enabled: bool):
        return self._set_field(self.Enabled, enabled)

    def Id(self, id: str):
        return self._set_field(self.Id.__name__, id)

    def IncludedObjectVersions(self, included_object_versions: str):
        return self._set_field(self.IncludedObjectVersions.__name__, included_object_versions)

    def OptionalFields(self, *optional_fields: str):
        return self._set_field(self.OptionalFields.__name__, list(optional_fields))

    def Prefix(self, prefix: str):
        return self._set_field(self.Prefix.__name__, prefix)

    def ScheduleFrequency(self, schedule_frequency: str):
        return self._set_field(self.ScheduleFrequency.__name__, schedule_frequency)

