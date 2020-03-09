from resources.shared import BaseModel


class Transition(BaseModel):
    __PROPERTY_STORAGE_CLASS = "StorageClass"
    __PROPERTY_TRANSITION_DATE = "TransitionDate"
    __PROPERTY_TRANSITION_IN_DAYS = "TransitionInDays"

    def storage_class(self, value: str):
        return self._add_field(self.__PROPERTY_STORAGE_CLASS, value)

    def transition_date(self, value: str):
        return self._add_field(self.__PROPERTY_TRANSITION_DATE, value)

    def transition_in_days(self, value: int):
        return self._add_field(self.__PROPERTY_TRANSITION_IN_DAYS, value)
