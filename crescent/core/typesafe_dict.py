from .model import Model
from .constants import Conditions


class TypeSafeDict(Model):
    def __init__(self, **validations):
        __type_safe_dict_conditions = {
            self.KeyValue.__name__: Conditions.TYPE_SAFE_DICT_KEY_VALUE,
            self.Json.__name__: Conditions.TYPE_SAFE_DICT_JSON
        }

        if validations.get("conditions", None):
            validations["conditions"].update(__type_safe_dict_conditions)
        else:
            validations["condition"] = __type_safe_dict_conditions

        super(TypeSafeDict, self).__init__(**validations)

    def Json(self, kvs: dict):
        return self._set_field(self.Json.__name__, kvs)

    def KeyValue(self, **kvs: dict):
        return self._set_field(self.KeyValue.__name__, kvs)
