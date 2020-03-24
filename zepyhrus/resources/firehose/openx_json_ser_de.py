from zepyhrus.core import Model, Validator


class OpenXJsonSerDe(Model):
    @Validator.validate(type=bool)
    def CaseInsensitive(self, value: bool):
        return self._set_field(self.CaseInsensitive.__name__, value)

    @Validator.validate(type=dict)
    def ColumnToJsonKeyMappings(self, value: dict):
        return self._set_field(self.ColumnToJsonKeyMappings.__name__, value)

    @Validator.validate(type=bool)
    def ConvertDotsInJsonKeysToUnderscores(self, value: bool):
        return self._set_field(self.ConvertDotsInJsonKeysToUnderscores.__name__, value)
