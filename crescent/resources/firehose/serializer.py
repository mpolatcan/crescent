from crescent.core import Model, Validator
from .orc_ser_de import OrcSerDe
from .parquet_ser_de import ParquetSerDe


class Serializer(Model):
    @Validator.validate(type=OrcSerDe)
    def OrcSerDe(self, value: OrcSerDe):
        return self._set_field(self.OrcSerDe.__name__, value.__to_dict__())

    @Validator.validate(type=ParquetSerDe)
    def ParquetSerDe(self, value: ParquetSerDe):
        return self._set_field(self.ParquetSerDe.__name__, value.__to_dict__())

