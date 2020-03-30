from crescent.core import Model, Validator
from .processor import Processor


class ProcessingConfiguration(Model):
    @Validator.validate(type=bool)
    def Enabled(self, enabled: bool):
        return self._set_field(self.Enabled.__name__, enabled)

    @Validator.validate(type=Processor)
    def Processors(self, *processors: Processor):
        return self._set_field(self.Processors.__name__, [proc.__to_dict__() for proc in list(processors)])
