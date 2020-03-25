from crescent.core import Model, Validator


class HiveJsonSerDe(Model):
    @Validator.validate(type=str)
    def TimestampFormats(self, *value: str):
        return self._set_field(self.TimestampFormats.__name__, list(value))
