from crescent.core import Model
from .processor import Processor


class ProcessingConfiguration(Model):
    def Enabled(self, enabled: bool):
        return self._set_field(self.Enabled.__name__, enabled)

    def Processors(self, *processors: Processor):
        return self._set_field(self.Processors.__name__, list(processors))
