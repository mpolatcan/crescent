from pyformation.resources.shared import BaseModel
from pyformation.resources.firehose import Serializer


class OutputFormatConfiguration(BaseModel):
    __PROPERTY_SERIALIZER = "Serializer"

    def serializer(self, value: Serializer):
        return self._add_field(self.__PROPERTY_SERIALIZER, value)
