from zepyhrus.core import Model, Validator
from .processor_parameter import ProcessorParameter
from .constants import AllowedValues


class Processor(Model):
    @Validator.validate(type=ProcessorParameter)
    def Parameters(self, *value: ProcessorParameter):
        if self._get_field(self.Parameters.__name__) is None:
            return self._set_field(self.Parameters.__name__, [proc_param.__to_dict__() for proc_param in list(value)])
        else:
            self._get_field(self.Parameters.__name__).extend([proc_param.__to_dict__() for proc_param in list(value)])
            return self

    @Validator.validate(type=str, allowed_values=AllowedValues.PROCESSOR_TYPE)
    def Type(self, value: str):
        return self._set_field(self.Type.__name__, value)
