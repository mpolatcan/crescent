from pyformation import PyformationModel


class HiveJsonSerDe(PyformationModel):
    __PROPERTY_TIMESTAMP_FORMATS = "TimestampFormats"

    def TimestampFormats(self, *value: str):
        return self._set_field(self.TimestampFormats.__name__, list(value))
