from crescent.core import Model, Validator
from .constants import AllowedValues


class OrcSerDe(Model):
    @Validator.validate(type=int, min_value=67108864)
    def BlockSizeBytes(self, block_size_bytes: int):
        return self._set_field(self.BlockSizeBytes.__name__, block_size_bytes)

    @Validator.validate(type=str)
    def BloomFilterColumns(self, *bloom_filter_cols: str):
        return self._set_field(self.BloomFilterColumns.__name__, list(bloom_filter_cols))

    @Validator.validate(type=float, min_value=0, max_value=1)
    def BloomFilterFalsePositiveProbability(self, bloom_filter_fp_positive_prob: float):
        return self._set_field(self.BloomFilterFalsePositiveProbability.__name__, bloom_filter_fp_positive_prob)

    @Validator.validate(type=str, allowed_values=AllowedValues.ORC_SER_DE_COMPRESSION)
    def Compression(self, compression: str):
        return self._set_field(self.Compression.__name__, compression)

    @Validator.validate(type=float)
    def DictionaryKeyThreshold(self, dict_key_threshold: float):
        return self._set_field(self.DictionaryKeyThreshold.__name__, dict_key_threshold)

    @Validator.validate(type=bool)
    def EnablePadding(self, enable_padding: bool):
        return self._set_field(self.EnablePadding.__name__, enable_padding)

    @Validator.validate(type=str, allowed_values=AllowedValues.ORC_SER_DE_FORMAT_VERSION)
    def FormatVersion(self, format_version: str):
        return self._set_field(self.FormatVersion.__name__, format_version)

    @Validator.validate(type=float, min_value=0, max_value=1)
    def PaddingTolerance(self, padding_tolerance: float):
        return self._set_field(self.PaddingTolerance.__name__, padding_tolerance)

    @Validator.validate(type=int, min_value=1000)
    def RowIndexStride(self, row_index_stride: int):
        return self._set_field(self.RowIndexStride.__name__, row_index_stride)

    @Validator.validate(type=int, min_value=8388608)
    def StripeSizeBytes(self, stripe_size_bytes: int):
        return self._set_field(self.StripeSizeBytes.__name__, stripe_size_bytes)
