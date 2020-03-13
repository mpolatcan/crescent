from pyformation.core import Model, Validator
from .processor_parameter import ProcessorParameter


class Processor(Model):
    @Validator.validate(type=ProcessorParameter)
    def Parameters(self, *value: ProcessorParameter):
        return self._set_field(self.Parameters.__name__, [proc_param.__to_dict__() for proc_param in list(value)])

    @Validator.validate(type=str)
    def Type(self, value: str):
        return self._set_field(self.Type.__name__, value)
