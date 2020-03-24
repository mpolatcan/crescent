from pyformation.core import Model, Validator
from .data_export import DataExport
from .constants import RequiredProperties


class StorageClassAnalysis(Model):
    @Validator.validate(type=DataExport, required_properties=RequiredProperties.DATA_EXPORT)
    def DataExport(self, value: DataExport):
        return self._set_field(self.DataExport.__name__, value.__to_dict__())
