from crescent.core import Model, Validator
from .constants import AllowedValues


class ParquetSerDe(Model):
    @Validator.validate(type=int, min_value=67108864)
    def BlockSizeBytes(self, block_size_bytes: int):
        return self._set_field(self.BlockSizeBytes.__name__, block_size_bytes)

    @Validator.validate(type=str, allowed_values=AllowedValues.PARQUET_SER_DE_COMPRESSION)
    def Compression(self, compression: str):
        return self._set_field(self.Compression.__name__, compression)

    @Validator.validate(type=bool)
    def EnableDictionaryCompression(self, enable_dict_compression: bool):
        return self._set_field(self.EnableDictionaryCompression.__name__, enable_dict_compression)

    @Validator.validate(type=int, min_value=0)
    def MaxPaddingBytes(self, max_padding_bytes: int):
        return self._set_field(self.MaxPaddingBytes.__name__, max_padding_bytes)

    @Validator.validate(type=int, min_value=65536)
    def PageSizeBytes(self, page_size_bytes: int):
        return self._set_field(self.PageSizeBytes.__name__, page_size_bytes)

    @Validator.validate(type=str, allowed_values=AllowedValues.PARQUET_SER_DE_WRITER_VERSION)
    def WriterVersion(self, writer_version: str):
        return self._set_field(self.WriterVersion.__name__, writer_version)
