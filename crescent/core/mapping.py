from .typesafe_dict import TypeSafeDict


class Mapping(TypeSafeDict):
    def __init__(self, id: str = None):
        super(Mapping, self).__init__()
        self.__id = id
        self._set_field(self.__id, {})

    def __rearrange_mapping(self):
        kvs = self.__get_field__(self.KeyValue.__name__)
        json = self.__get_field__(self.Json.__name__)

        if json or kvs:
            for key, value in kvs.items() if kvs else json.items():
                self.__get_field__(self.__id).update({key: value})

            self._pop_field(self.KeyValue.__name__ if kvs else self.Json.__name__)

    def __to_dict__(self, **kwargs):
        conversion_success, conversion_result = super().__to_dict__(id=self.__id)

        if conversion_success:
            self.__rearrange_mapping()

        return conversion_success, conversion_result
