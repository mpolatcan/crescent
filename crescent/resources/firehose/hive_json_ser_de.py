from crescent.core import Model, Validator


class HiveJsonSerDe(Model):
    @Validator.validate(type=str)
    def TimestampFormats(self, *timestamp_fmts: str):
        return self._set_field(self.TimestampFormats.__name__, list(timestamp_fmts))
