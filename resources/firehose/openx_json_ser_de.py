from resources.shared import BaseModel


class OpenXJsonSerDe(BaseModel):
    __PROPERTY_CASE_INSENSITIVE = "CaseInsensitive"
    __PROPERTY_COLUMN_TO_JSON_KEY_MAPPINGS = "ColumnToJsonKeyMappings"
    __PROPERTY_CONVERT_DOTS_IN_JSON_KEYS_TO_UNDERSCORES = "ConvertDotsInJsonKeysToUnderscores"

    def case_insensitive(self, value: bool):
        return self._add_field(self.__PROPERTY_CASE_INSENSITIVE, value)

    def column_to_json_key_mappings(self, value: dict):
        return self._add_field(self.__PROPERTY_COLUMN_TO_JSON_KEY_MAPPINGS, value)

    def convert_dots_in_json_keys_to_underscores(self, value: bool):
        return self._add_field(self.__PROPERTY_CONVERT_DOTS_IN_JSON_KEYS_TO_UNDERSCORES, value)
