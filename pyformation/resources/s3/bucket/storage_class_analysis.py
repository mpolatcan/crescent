from pyformation import PyformationModel
from .data_export import DataExport


class StorageClassAnalysis(PyformationModel):
    __PROPERTY_DATA_EXPORT = "DataExport"

    def DataExport(self, value: DataExport):
        return self._set_field(self.DataExport.__name__, value.__to_dict__())
