from crescent.core import Model
from crescent.functions import AnyFn
from .destination import Destination
from .constants import AllowedValues, ModelRequiredProperties
from typing import Union


class DataExport(Model):
    def __init__(self):
        super(DataExport, self).__init__(
            allowed_values={self.OutputSchemaVersion.__name__: AllowedValues.OUTPUT_SCHEMA_VERSION},
            required_properties=ModelRequiredProperties.DATA_EXPORT
        )

    def Destination(self, destination: Destination):
        return self._set_field(self.Destination.__name__, destination)

    def OutputSchemaVersion(self, output_schema_version: Union[str, AnyFn]):
        return self._set_field(self.OutputSchemaVersion.__name__, output_schema_version)
