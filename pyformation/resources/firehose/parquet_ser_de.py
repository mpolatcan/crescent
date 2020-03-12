from pyformation import PyformationModel


class ParquetSerDe(PyformationModel):
    def BlockSizeBytes(self, value: int):
        return self._set_field(self.BlockSizeBytes.__name__, value)

    def Compression(self, value: str):
        return self._set_field(self.Compression.__name__, value)

    def EnableDictionaryCompression(self, value: bool):
        return self._set_field(self.EnableDictionaryCompression.__name__, value)

    def MaxPaddingBytes(self, value: int):
        return self._set_field(self.MaxPaddingBytes.__name__, value)

    def PageSizeBytes(self, value: int):
        return self._set_field(self.PageSizeBytes.__name__, value)

    def WriterVersion(self, value: str):
        return self._set_field(self.WriterVersion.__name__, value)
