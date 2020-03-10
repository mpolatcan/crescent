from pyformation.resources.shared import BaseModel
from pyformation.resources.firehose import ProcessorParameter


class Processor(BaseModel):
    __PROPERTY_PARAMETERS = "Parameters"
    __PROPERTY_TYPE = "Type"

    def parameters(self, *value: ProcessorParameter):
        return self._add_field(self.__PROPERTY_PARAMETERS, [
            proc_parameter for proc_parameter in list(value)
        ])

    def type(self, value: str):
        return self._add_field(self.__PROPERTY_TYPE, value)
