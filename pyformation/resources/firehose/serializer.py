from pyformation.resources.shared import BaseModel
from pyformation.resources.firehose import OrcSerDe, ParquetSerDe


class Serializer(BaseModel):
    __PROPERTY_ORC_SER_DE = "OrcSerDe"
    __PROPERTY_PARQUET_SER_DE = "ParquetSerDe"

    def orc_ser_de(self, value: OrcSerDe):
        return self._add_field(self.__PROPERTY_ORC_SER_DE, value)

    def parquet_ser_de(self, value: ParquetSerDe):
        return self._add_field(self.__PROPERTY_PARQUET_SER_DE, value)

