from pyformation import PyformationModel
from .processor import Processor


class ProcessingConfiguration(PyformationModel):
    def Enabled(self, value: bool):
        return self._set_field(self.Enabled.__name__, value)

    def Processors(self, *value: Processor):
        return self._set_field(self.Processors.__name__, [proc.__to_dict__() for proc in list(value)])
