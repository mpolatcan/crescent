from pyformation.resources.shared import BaseModel


class HiveJsonSerDe(BaseModel):
    __PROPERTY_TIMESTAMP_FORMATS = "TimestampFormats"

    def timestamp_formats(self, *value: str):
        return self._add_field(self.__PROPERTY_TIMESTAMP_FORMATS, list(value))
