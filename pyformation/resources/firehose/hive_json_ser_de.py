from pyformation.core import Model, Validator


class HiveJsonSerDe(Model):
    __PROPERTY_TIMESTAMP_FORMATS = "TimestampFormats"

    @Validator.validate(type=str)
    def TimestampFormats(self, *value: str):
        return self._set_field(self.TimestampFormats.__name__, list(value))
