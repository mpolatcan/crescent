from pyformation import PyformationModel
from .destination import Destination


class InventoryConfiguration(PyformationModel):
    def Destination(self, value: Destination):
        return self._set_field(self.Destination.__name__, value.__to_dict__())

    def Enabled(self, value: bool):
        return self._set_field(self.Enabled, value)

    def Id(self, value: str):
        return self._set_field(self.Id.__name__, value)

    def IncludedObjectVersions(self, value: str):
        return self._set_field(self.IncludedObjectVersions.__name__, value)

    def OptionalFields(self, *value: str):
        return self._set_field(self.OptionalFields.__name__, list(value))

    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)

    def ScheduleFrequency(self, value: str):
        return self._set_field(self.ScheduleFrequency.__name__, value)

