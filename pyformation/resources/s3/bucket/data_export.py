from pyformation import PyformationModel
from .destination import Destination


class DataExport(PyformationModel):
    def Destination(self, value: Destination):
        return self._set_field(self.Destination.__name__, value.__to_dict__())

    def OutputSchemaVersion(self, value: str):
        return self._set_field(self.OutputSchemaVersion.__name__, value)
