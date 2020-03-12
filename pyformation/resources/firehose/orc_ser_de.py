from pyformation import PyformationModel


class OrcSerDe(PyformationModel):
    def BlockSizeBytes(self, value: int):
        return self._set_field(self.BlockSizeBytes.__name__, value)

    def BloomFilterColumns(self, *value: str):
        return self._set_field(self.BloomFilterColumns.__name__, list(value))

    def BloomFilterFalsePositiveProbability(self, value: float):
        return self._set_field(self.BloomFilterFalsePositiveProbability.__name__, value)

    def Compression(self, value: str):
        return self._set_field(self.Compression.__name__, value)

    def DictionaryKeyThreshold(self, value: float):
        return self._set_field(self.DictionaryKeyThreshold.__name__, value)

    def EnablePadding(self, value: bool):
        return self._set_field(self.EnablePadding.__name__, value)

    def FormatVersion(self, value: str):
        return self._set_field(self.FormatVersion.__name__, value)

    def PaddingTolerance(self, value: float):
        return self._set_field(self.PaddingTolerance.__name__, value)

    def RowIndexStride(self, value: int):
        return self._set_field(self.RowIndexStride.__name__, value)

    def StripeSizeBytes(self, value: int):
        return self._set_field(self.StripeSizeBytes.__name__, value)
