from crescent.core import Model


class HiveJsonSerDe(Model):
    def TimestampFormats(self, *timestamp_fmts: str):
        return self._set_field(self.TimestampFormats.__name__, list(timestamp_fmts))
