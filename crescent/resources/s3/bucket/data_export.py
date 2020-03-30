from crescent.core import Model, Validator
from .destination import Destination
from .constants import AllowedValues, ModelRequiredProperties


class DataExport(Model):
    @Validator.validate(type=Destination, required_properties=ModelRequiredProperties.DESTINATION)
    def Destination(self, destination: Destination):
        return self._set_field(self.Destination.__name__, destination.__to_dict__())

    @Validator.validate(type=str, allowed_values=AllowedValues.OUTPUT_SCHEMA_VERSION)
    def OutputSchemaVersion(self, output_schema_version: str):
        return self._set_field(self.OutputSchemaVersion.__name__, output_schema_version)
