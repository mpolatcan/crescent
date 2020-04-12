from crescent.core import Model
from crescent.functions import AnyFn
from typing import Union


class ScalingConfiguration(Model):
    def AutoPause(self, auto_pause: Union[bool, AnyFn]):
        return self._set_field(self.AutoPause.__name__, auto_pause)

    def MaxCapacity(self, max_capacity: Union[int, AnyFn]):
        return self._set_field(self.MaxCapacity.__name__, max_capacity)

    def MinCapacity(self, min_capacity: Union[int, AnyFn]):
        return self._set_field(self.MinCapacity.__name__, min_capacity)

    def SecondsUntilAutoPause(self, secs_until_auto_pause: Union[int, AnyFn]):
        return self._set_field(self.SecondsUntilAutoPause.__name__, secs_until_auto_pause)
