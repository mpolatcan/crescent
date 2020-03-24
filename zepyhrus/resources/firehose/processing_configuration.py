from zepyhrus.core import Model, Validator
from .processor import Processor


class ProcessingConfiguration(Model):
    @Validator.validate(type=bool)
    def Enabled(self, value: bool):
        return self._set_field(self.Enabled.__name__, value)

    @Validator.validate(type=Processor)
    def Processors(self, *value: Processor):
        return self._set_field(self.Processors.__name__, [proc.__to_dict__() for proc in list(value)])
