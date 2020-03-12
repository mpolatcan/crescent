from pyformation import PyformationModel


class OpenXJsonSerDe(PyformationModel):
    def CaseInsensitive(self, value: bool):
        return self._set_field(self.CaseInsensitive.__name__, value)

    def ColumnToJsonKeyMappings(self, value: dict):
        return self._set_field(self.ColumnToJsonKeyMappings.__name__, value)

    def ConvertDotsInJsonKeysToUnderscores(self, value: bool):
        return self._set_field(self.ConvertDotsInJsonKeysToUnderscores.__name__, value)
