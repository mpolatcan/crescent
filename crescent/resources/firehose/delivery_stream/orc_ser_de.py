from crescent.core import Model
from crescent.functions import AnyFn
from .constants import AllowedValues
from typing import Union


class OrcSerDe(Model):
    def __init__(self):
        super(OrcSerDe, self).__init__(
            min_value={self.BlockSizeBytes.__name__: 67108864,
                       self.BloomFilterFalsePositiveProbability.__name__: 0,
                       self.PaddingTolerance.__name__: 0,
                       self.RowIndexStride.__name__: 1000,
                       self.StripeSizeBytes.__name__: 8388608},
            max_value={self.BloomFilterFalsePositiveProbability.__name__: 1,
                       self.PaddingTolerance.__name__: 1},
            allowed_values={self.Compression.__name__: AllowedValues.ORC_SER_DE_COMPRESSION,
                            self.FormatVersion.__name__: AllowedValues.ORC_SER_DE_FORMAT_VERSION}
        )

    def BlockSizeBytes(self, block_size_bytes: Union[int, AnyFn]):
        return self._set_field(self.BlockSizeBytes.__name__, block_size_bytes)

    def BloomFilterColumns(self, *bloom_filter_cols: Union[str, AnyFn]):
        return self._set_field(self.BloomFilterColumns.__name__, list(bloom_filter_cols))

    def BloomFilterFalsePositiveProbability(self, bloom_filter_fp_positive_prob: Union[float, AnyFn]):
        return self._set_field(self.BloomFilterFalsePositiveProbability.__name__, bloom_filter_fp_positive_prob)

    def Compression(self, compression: Union[str, AnyFn]):
        return self._set_field(self.Compression.__name__, compression)

    def DictionaryKeyThreshold(self, dict_key_threshold: Union[float, AnyFn]):
        return self._set_field(self.DictionaryKeyThreshold.__name__, dict_key_threshold)

    def EnablePadding(self, enable_padding: Union[bool, AnyFn]):
        return self._set_field(self.EnablePadding.__name__, enable_padding)

    def FormatVersion(self, format_version: Union[str, AnyFn]):
        return self._set_field(self.FormatVersion.__name__, format_version)

    def PaddingTolerance(self, padding_tolerance: Union[float, AnyFn]):
        return self._set_field(self.PaddingTolerance.__name__, padding_tolerance)

    def RowIndexStride(self, row_index_stride: Union[int, AnyFn]):
        return self._set_field(self.RowIndexStride.__name__, row_index_stride)

    def StripeSizeBytes(self, stripe_size_bytes: Union[int, AnyFn]):
        return self._set_field(self.StripeSizeBytes.__name__, stripe_size_bytes)
