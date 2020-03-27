from crescent.core import Model, Validator
from .data_export import DataExport
from .constants import ModelRequiredProperties


class StorageClassAnalysis(Model):
    @Validator.validate(type=DataExport, required_properties=ModelRequiredProperties.DATA_EXPORT)
    def DataExport(self, value: DataExport):
        return self._set_field(self.DataExport.__name__, value.__to_dict__())
