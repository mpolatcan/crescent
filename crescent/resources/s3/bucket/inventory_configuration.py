from crescent.core import Model, Validator
from .destination import Destination
from .constants import AllowedValues, RequiredProperties


class InventoryConfiguration(Model):
    @Validator.validate(type=Destination, required_properties=RequiredProperties.DESTINATION)
    def Destination(self, value: Destination):
        return self._set_field(self.Destination.__name__, value.__to_dict__())

    @Validator.validate(type=bool)
    def Enabled(self, value: bool):
        return self._set_field(self.Enabled, value)

    @Validator.validate(type=str)
    def Id(self, value: str):
        return self._set_field(self.Id.__name__, value)

    @Validator.validate(type=str, allowed_values=AllowedValues.INCLUDED_OBJECT_VERSIONS)
    def IncludedObjectVersions(self, value: str):
        return self._set_field(self.IncludedObjectVersions.__name__, value)

    @Validator.validate(type=str)
    def OptionalFields(self, *value: str):
        return self._set_field(self.OptionalFields.__name__, list(value))

    @Validator.validate(type=str)
    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)

    @Validator.validate(type=str, allowed_values=AllowedValues.SCHEDULE_FREQUENCY)
    def ScheduleFrequency(self, value: str):
        return self._set_field(self.ScheduleFrequency.__name__, value)

