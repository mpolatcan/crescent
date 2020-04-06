from crescent.core import Model
from .data_export import DataExport


class StorageClassAnalysis(Model):
    def DataExport(self, data_export: DataExport):
        return self._set_field(self.DataExport.__name__, data_export)
