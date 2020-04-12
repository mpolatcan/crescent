from crescent.core import Model
from crescent.functions import AnyFn
from typing import Union


class OpenXJsonSerDe(Model):
    def CaseInsensitive(self, case_insensitive: Union[bool, AnyFn]):
        return self._set_field(self.CaseInsensitive.__name__, case_insensitive)

    def ColumnToJsonKeyMappings(self, col_to_json_key_mappings: Union[dict, AnyFn]):
        return self._set_field(self.ColumnToJsonKeyMappings.__name__, col_to_json_key_mappings)

    def ConvertDotsInJsonKeysToUnderscores(self, convert_dots_in_json_keys_to_underscores: Union[bool, AnyFn]):
        return self._set_field(self.ConvertDotsInJsonKeysToUnderscores.__name__, convert_dots_in_json_keys_to_underscores)
