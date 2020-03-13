from pyformation.core import Model, Validator


class ParquetSerDe(Model):
    @Validator.validate(type=int)
    def BlockSizeBytes(self, value: int):
        return self._set_field(self.BlockSizeBytes.__name__, value)

    @Validator.validate(type=str)
    def Compression(self, value: str):
        return self._set_field(self.Compression.__name__, value)

    @Validator.validate(type=bool)
    def EnableDictionaryCompression(self, value: bool):
        return self._set_field(self.EnableDictionaryCompression.__name__, value)

    @Validator.validate(type=int)
    def MaxPaddingBytes(self, value: int):
        return self._set_field(self.MaxPaddingBytes.__name__, value)

    @Validator.validate(type=int)
    def PageSizeBytes(self, value: int):
        return self._set_field(self.PageSizeBytes.__name__, value)

    @Validator.validate(type=str)
    def WriterVersion(self, value: str):
        return self._set_field(self.WriterVersion.__name__, value)
