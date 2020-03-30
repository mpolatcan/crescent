from crescent.core import Model, Validator


class OpenXJsonSerDe(Model):
    @Validator.validate(type=bool)
    def CaseInsensitive(self, case_insensitive: bool):
        return self._set_field(self.CaseInsensitive.__name__, case_insensitive)

    @Validator.validate(type=dict)
    def ColumnToJsonKeyMappings(self, col_to_json_key_mappings: dict):
        return self._set_field(self.ColumnToJsonKeyMappings.__name__, col_to_json_key_mappings)

    @Validator.validate(type=bool)
    def ConvertDotsInJsonKeysToUnderscores(self, convert_dots_in_json_keys_to_underscores: bool):
        return self._set_field(self.ConvertDotsInJsonKeysToUnderscores.__name__, convert_dots_in_json_keys_to_underscores)
