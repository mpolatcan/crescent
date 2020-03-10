from resources.shared import BaseModel


class ScalingConfiguration(BaseModel):
    __PROPERTY_AUTO_PAUSE = "AutoPause"
    __PROPERTY_MAX_CAPACITY = "MaxCapacity"
    __PROPERTY_MIN_CAPACITY = "MinCapacity"
    __PROPERTY_SECONDS_UNTIL_AUTO_PAUSE = "SecondsUntilAutoPause"

    def auto_pause(self, value: bool):
        return self._add_field(self.__PROPERTY_AUTO_PAUSE, value)

    def max_capacity(self, value: int):
        return self._add_field(self.__PROPERTY_MAX_CAPACITY, value)

    def min_capacity(self, value: int):
        return self._add_field(self.__PROPERTY_MIN_CAPACITY, value)

    def seconds_until_auto_pause(self, value: int):
        return self._add_field(self.__PROPERTY_SECONDS_UNTIL_AUTO_PAUSE, value)
