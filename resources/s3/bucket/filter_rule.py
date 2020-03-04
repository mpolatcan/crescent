from resources.shared.base_model import BaseModel


class FilterRule(BaseModel):
    __PROPERTY_NAME = "Name"
    __PROPERTY_VALUE = "Value"

    def name(self, value: str):
        return self._add_field(self.__PROPERTY_NAME, value)

    def value(self, value: str):
        return self._add_field(self.__PROPERTY_VALUE, value)
