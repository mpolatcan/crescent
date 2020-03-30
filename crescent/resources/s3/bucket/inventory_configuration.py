from crescent.core import Model, Validator
from .destination import Destination
from .constants import AllowedValues, ModelRequiredProperties


class InventoryConfiguration(Model):
    @Validator.validate(type=Destination, required_properties=ModelRequiredProperties.DESTINATION)
    def Destination(self, destination: Destination):
        return self._set_field(self.Destination.__name__, destination.__to_dict__())

    @Validator.validate(type=bool)
    def Enabled(self, enabled: bool):
        return self._set_field(self.Enabled, enabled)

    @Validator.validate(type=str)
    def Id(self, id: str):
        return self._set_field(self.Id.__name__, id)

    @Validator.validate(type=str, allowed_values=AllowedValues.INCLUDED_OBJECT_VERSIONS)
    def IncludedObjectVersions(self, included_object_versions: str):
        return self._set_field(self.IncludedObjectVersions.__name__, included_object_versions)

    @Validator.validate(type=str)
    def OptionalFields(self, *optional_fields: str):
        return self._set_field(self.OptionalFields.__name__, list(optional_fields))

    @Validator.validate(type=str)
    def Prefix(self, prefix: str):
        return self._set_field(self.Prefix.__name__, prefix)

    @Validator.validate(type=str, allowed_values=AllowedValues.SCHEDULE_FREQUENCY)
    def ScheduleFrequency(self, schedule_frequency: str):
        return self._set_field(self.ScheduleFrequency.__name__, schedule_frequency)

