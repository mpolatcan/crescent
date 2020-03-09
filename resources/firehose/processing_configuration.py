from resources.shared import BaseModel
from resources.firehose import Processor


class ProcessingConfiguration(BaseModel):
    __PROPERTY_ENABLED = "Enabled"
    __PROPERTY_PROCESSORS = "Processors"

    def enabled(self, value: bool):
        return self._add_field(self.__PROPERTY_ENABLED, value)

    def processors(self, *value: Processor):
        return self._add_field(self.__PROPERTY_PROCESSORS, [
            processor.create() for processor in list(value)
        ])
