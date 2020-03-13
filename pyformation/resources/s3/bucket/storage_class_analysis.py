from pyformation.core import Model, Validator
from .data_export import DataExport


class StorageClassAnalysis(Model):
    __PROPERTY_DATA_EXPORT = "DataExport"

    @Validator.validate(type=DataExport)
    def DataExport(self, value: DataExport):
        return self._set_field(self.DataExport.__name__, value.__to_dict__())
