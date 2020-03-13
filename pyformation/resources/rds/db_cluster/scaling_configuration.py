from pyformation.core import Model, Validator


class ScalingConfiguration(Model):
    @Validator.validate(type=bool)
    def AutoPause(self, value: bool):
        return self._set_field(self.AutoPause.__name__, value)

    @Validator.validate(type=int)
    def MaxCapacity(self, value: int):
        return self._set_field(self.MaxCapacity.__name__, value)

    @Validator.validate(type=int)
    def MinCapacity(self, value: int):
        return self._set_field(self.MinCapacity.__name__, value)

    @Validator.validate(type=int)
    def SecondsUntilAutoPause(self, value: int):
        return self._set_field(self.SecondsUntilAutoPause.__name__, value)
