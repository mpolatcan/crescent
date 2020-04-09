from .fn import FnArrayValue


class FindInMap(FnArrayValue):
    def __init__(self):
        super(FindInMap, self).__init__(
            fn_name=FindInMap.__name__,
            field_order=[self.MapName.__name__,
                         self.TopLevelKey.__name__,
                         self.SecondLevelKey.__name__]
        )

    def MapName(self, map_name: str):
        return self._set_field(self.MapName.__name__, map_name)

    def TopLevelKey(self, top_level_key: str):
        return self._set_field(self.TopLevelKey.__name__, top_level_key)

    def SecondLevelKey(self, second_level_key: str):
        return self._set_field(self.SecondLevelKey.__name__, second_level_key)

