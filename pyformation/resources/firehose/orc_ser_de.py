from pyformation.core import Model, Validator


class OrcSerDe(Model):
    @Validator.validate(type=int)
    def BlockSizeBytes(self, value: int):
        return self._set_field(self.BlockSizeBytes.__name__, value)

    @Validator.validate(type=str)
    def BloomFilterColumns(self, *value: str):
        return self._set_field(self.BloomFilterColumns.__name__, list(value))

    @Validator.validate(type=float)
    def BloomFilterFalsePositiveProbability(self, value: float):
        return self._set_field(self.BloomFilterFalsePositiveProbability.__name__, value)

    @Validator.validate(type=str)
    def Compression(self, value: str):
        return self._set_field(self.Compression.__name__, value)

    @Validator.validate(type=float)
    def DictionaryKeyThreshold(self, value: float):
        return self._set_field(self.DictionaryKeyThreshold.__name__, value)

    @Validator.validate(type=bool)
    def EnablePadding(self, value: bool):
        return self._set_field(self.EnablePadding.__name__, value)

    @Validator.validate(type=str)
    def FormatVersion(self, value: str):
        return self._set_field(self.FormatVersion.__name__, value)

    @Validator.validate(type=float)
    def PaddingTolerance(self, value: float):
        return self._set_field(self.PaddingTolerance.__name__, value)

    @Validator.validate(type=int)
    def RowIndexStride(self, value: int):
        return self._set_field(self.RowIndexStride.__name__, value)

    @Validator.validate(type=int)
    def StripeSizeBytes(self, value: int):
        return self._set_field(self.StripeSizeBytes.__name__, value)
