from resources.shared import BaseModel


class ParquetSerDe(BaseModel):
    __PROPERTY_BLOCK_SIZE_BYTES = "BlockSizeBytes"
    __PROPERTY_COMPRESSION = "Compression"
    __PROPERTY_ENABLE_DICTIONARY_COMPRESSION = "EnableDictionaryCompression"
    __PROPERTY_MAX_PADDING_BYTES = "MaxPaddingBytes"
    __PROPERTY_PAGE_SIZE_BYTES = "PageSizeBytes"
    __PROPERTY_WRITER_VERSION = "WriterVersion"

    def block_size_bytes(self, value: int):
        return self._add_field(self.__PROPERTY_BLOCK_SIZE_BYTES, value)

    def compression(self, value: str):
        return self._add_field(self.__PROPERTY_COMPRESSION, value)

    def enable_dictionary_compression(self, value: bool):
        return self._add_field(self.__PROPERTY_ENABLE_DICTIONARY_COMPRESSION, value)

    def max_padding_bytes(self, value: int):
        return self._add_field(self.__PROPERTY_MAX_PADDING_BYTES, value)

    def page_size_bytes(self, value: int):
        return self._add_field(self.__PROPERTY_PAGE_SIZE_BYTES, value)

    def writer_version(self, value: str):
        return self._add_field(self.__PROPERTY_WRITER_VERSION, value)
