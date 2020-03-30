from crescent.core import Model, Validator


class ScalingConfiguration(Model):
    @Validator.validate(type=bool)
    def AutoPause(self, auto_pause: bool):
        return self._set_field(self.AutoPause.__name__, auto_pause)

    @Validator.validate(type=int)
    def MaxCapacity(self, max_capacity: int):
        return self._set_field(self.MaxCapacity.__name__, max_capacity)

    @Validator.validate(type=int)
    def MinCapacity(self, min_capacity: int):
        return self._set_field(self.MinCapacity.__name__, min_capacity)

    @Validator.validate(type=int)
    def SecondsUntilAutoPause(self, secs_until_auto_pause: int):
        return self._set_field(self.SecondsUntilAutoPause.__name__, secs_until_auto_pause)
