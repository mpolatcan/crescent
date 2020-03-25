from crescent.core import Model, Validator
from .constants import AllowedValues


class ParquetSerDe(Model):
    @Validator.validate(type=int, min_value=67108864)
    def BlockSizeBytes(self, value: int):
        return self._set_field(self.BlockSizeBytes.__name__, value)

    @Validator.validate(type=str, allowed_values=AllowedValues.PARQUET_SER_DE_COMPRESSION)
    def Compression(self, value: str):
        return self._set_field(self.Compression.__name__, value)

    @Validator.validate(type=bool)
    def EnableDictionaryCompression(self, value: bool):
        return self._set_field(self.EnableDictionaryCompression.__name__, value)

    @Validator.validate(type=int, min_value=0)
    def MaxPaddingBytes(self, value: int):
        return self._set_field(self.MaxPaddingBytes.__name__, value)

    @Validator.validate(type=int, min_value=65536)
    def PageSizeBytes(self, value: int):
        return self._set_field(self.PageSizeBytes.__name__, value)

    @Validator.validate(type=str, allowed_values=AllowedValues.PARQUET_SER_DE_WRITER_VERSION)
    def WriterVersion(self, value: str):
        return self._set_field(self.WriterVersion.__name__, value)
