from resources.shared import BaseModel
from resources.firehose import (
    HiveJsonSerDe,
    OpenXJsonSerDe
)


class Deserializer(BaseModel):
    __PROPERTY_HIVE_JSON_SER_DE = "HiveJsonSerDe"
    __PROPERTY_OPENX_JSON_SER_DE = "OpenXJsonSerDe"

    def hive_json_ser_de(self, value: HiveJsonSerDe):
        return self._add_field(self.__PROPERTY_HIVE_JSON_SER_DE, value.create())

    def openx_json_ser_de(self, value: OpenXJsonSerDe):
        return self._add_field(self.__PROPERTY_OPENX_JSON_SER_DE, value.create())
