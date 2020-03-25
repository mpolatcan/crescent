from crescent.core import Model, Validator
from .destination import Destination
from .constants import AllowedValues, RequiredProperties


class DataExport(Model):
    @Validator.validate(type=Destination, required_properties=RequiredProperties.DESTINATION)
    def Destination(self, value: Destination):
        return self._set_field(self.Destination.__name__, value.__to_dict__())

    @Validator.validate(type=str, allowed_values=AllowedValues.OUTPUT_SCHEMA_VERSION)
    def OutputSchemaVersion(self, value: str):
        return self._set_field(self.OutputSchemaVersion.__name__, value)
