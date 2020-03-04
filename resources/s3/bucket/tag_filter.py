from resources.shared.base_model import BaseModel


class TagFilter(BaseModel):
    __PROPERTY_KEY = "Key"
    __PROPERTY_VALUE = "Value"

    def key(self, value: str):
        return self._add_field(self.__PROPERTY_KEY, value)

    def value(self, value: str):
        return self._add_field(self.__PROPERTY_VALUE, value)
