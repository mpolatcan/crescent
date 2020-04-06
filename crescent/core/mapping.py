from .model import Model


class MappingKV(Model):
    def __init__(self):
        super(MappingKV, self).__init__()

    def Key(self, key: str):
        return self._set_field(self.Key.__name__, key)

    def Value(self, value: (int, float, list, str, dict)):
        return self._set_field(self.Value.__name__, value)

# --------------------------------------


class Mapping(Model):
    def __init__(self, id: str = None):
        super(Mapping, self).__init__()
        self.__id = id

    def KV(self, *kvs: MappingKV):
        return self._set_field(self.KV.__name__, list(kvs))

    def __rearrange_mapping(self):
        self._set_field(self.__id, {})

        for kv in self.__get_field__(self.KV.__name__):
            key, value = tuple(kv.values())
            self.__get_field__(self.__id).update({key: value})

        self._pop_field(self.KV.__name__)

    def __to_dict__(self, **kwargs):
        conversion_success, conversion_result = super().__to_dict__(id=self.__id)

        if conversion_success:
            self.__rearrange_mapping()

        return conversion_success, conversion_result
