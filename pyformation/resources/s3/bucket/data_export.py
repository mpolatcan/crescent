from pyformation.core import Model, Validator
from .destination import Destination


class DataExport(Model):
    @Validator.validate(type=Destination)
    def Destination(self, value: Destination):
        return self._set_field(self.Destination.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def OutputSchemaVersion(self, value: str):
        return self._set_field(self.OutputSchemaVersion.__name__, value)
