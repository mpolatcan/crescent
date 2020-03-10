from pyformation.resources.shared import BaseModel
from pyformation.resources.firehose import Deserializer


class InputFormatConfiguration(BaseModel):
    __PROPERTY_DESERIALIZER = "Deserializer"

    def deserializer(self, value: Deserializer):
        return self._add_field(self.__PROPERTY_DESERIALIZER, value)
