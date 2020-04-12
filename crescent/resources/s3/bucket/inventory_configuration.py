from crescent.core import Model
from crescent.functions import AnyFn
from .destination import Destination
from .constants import AllowedValues, ModelRequiredProperties
from typing import Union


class InventoryConfiguration(Model):
    def __init__(self):
        super(InventoryConfiguration, self).__init__(
            allowed_values={self.IncludedObjectVersions.__name__: AllowedValues.INCLUDED_OBJECT_VERSIONS,
                            self.ScheduleFrequency.__name__: AllowedValues.SCHEDULE_FREQUENCY},
            required_properties=ModelRequiredProperties.INVENTORY_CONFIGURATION
        )

    def Destination(self, destination: Destination):
        return self._set_field(self.Destination.__name__, destination.__to_dict__())

    def Enabled(self, enabled: Union[bool, AnyFn]):
        return self._set_field(self.Enabled, enabled)

    def Id(self, id: Union[str, AnyFn]):
        return self._set_field(self.Id.__name__, id)

    def IncludedObjectVersions(self, included_object_versions: Union[str, AnyFn]):
        return self._set_field(self.IncludedObjectVersions.__name__, included_object_versions)

    def OptionalFields(self, *optional_fields: Union[str, AnyFn]):
        return self._set_field(self.OptionalFields.__name__, list(optional_fields))

    def Prefix(self, prefix: Union[str, AnyFn]):
        return self._set_field(self.Prefix.__name__, prefix)

    def ScheduleFrequency(self, schedule_frequency: Union[str, AnyFn]):
        return self._set_field(self.ScheduleFrequency.__name__, schedule_frequency)

