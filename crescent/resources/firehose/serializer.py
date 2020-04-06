from crescent.core import Model
from .orc_ser_de import OrcSerDe
from .parquet_ser_de import ParquetSerDe


class Serializer(Model):
    def OrcSerDe(self, orc_ser_de: OrcSerDe):
        return self._set_field(self.OrcSerDe.__name__, orc_ser_de)

    def ParquetSerDe(self, parquet_ser_de: ParquetSerDe):
        return self._set_field(self.ParquetSerDe.__name__, parquet_ser_de)

