from resources.shared import BaseModel


class OrcSerDe(BaseModel):
    __PROPERTY_BLOCK_SIZE_BYTES = "BlockSizeBytes"
    __PROPERTY_BLOOM_FILTER_COLUMNS = "BloomFilterColumns"
    __PROPERTY_BLOOM_FILTER_FALSE_POSITIVE_PROBABILITY = "BloomFilterFalsePositiveProbability"
    __PROPERTY_COMPRESSION = "Compression"
    __PROPERTY_DICTIONARY_KEY_THRESHOLD = "DictionaryKeyThreshold"
    __PROPERTY_ENABLE_PADDING = "EnablePadding"
    __PROPERTY_FORMAT_VERSION = "FormatVersion"
    __PROPERTY_PADDING_TOLERANCE = "PaddingTolerance"
    __PROPERTY_ROW_INDEX_STRIDE = "RowIndexStride"
    __PROPERTY_STRIPE_SIZE_BYTES = "StripeSizeBytes"

    def block_size_bytes(self, value: int):
        return self._add_field(self.__PROPERTY_BLOCK_SIZE_BYTES, value)

    def bloom_filter_columns(self, *value: str):
        return self._add_field(self.__PROPERTY_BLOOM_FILTER_COLUMNS, list(value))

    def bloom_filter_false_positive_probability(self, value: float):
        return self._add_field(self.__PROPERTY_BLOOM_FILTER_FALSE_POSITIVE_PROBABILITY, value)

    def compression(self, value: str):
        return self._add_field(self.__PROPERTY_COMPRESSION, value)

    def dictionary_key_threshold(self, value: float):
        return self._add_field(self.__PROPERTY_DICTIONARY_KEY_THRESHOLD, value)

    def enable_padding(self, value: bool):
        return self._add_field(self.__PROPERTY_ENABLE_PADDING, value)

    def format_version(self, value: str):
        return self._add_field(self.__PROPERTY_FORMAT_VERSION, value)

    def padding_tolerance(self, value: float):
        return self._add_field(self.__PROPERTY_PADDING_TOLERANCE, value)

    def row_index_stride(self, value: int):
        return self._add_field(self.__PROPERTY_ROW_INDEX_STRIDE, value)

    def stripe_size_bytes(self, value: int):
        return self._add_field(self.__PROPERTY_STRIPE_SIZE_BYTES, value)
