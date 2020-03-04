from resources.shared.base_model import BaseModel


class DefaultRetention(BaseModel):
    __PROPERTY_DAYS = "Days"
    __PROPERTY_MODE = "Mode"
    __PROPERTY_YEARS = "Years"

    def days(self, value: int):
        return self._add_field(self.__PROPERTY_DAYS, value)

    def mode(self, value: str):
        return self._add_field(self.__PROPERTY_MODE, value)

    def years(self, value: int):
        return self._add_field(self.__PROPERTY_YEARS, value)
