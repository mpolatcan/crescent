from pyformation import PyformationModel


class ScalingConfiguration(PyformationModel):
    def AutoPause(self, value: bool):
        return self._set_field(self.AutoPause.__name__, value)

    def MaxCapacity(self, value: int):
        return self._set_field(self.MaxCapacity.__name__, value)

    def MinCapacity(self, value: int):
        return self._set_field(self.MinCapacity.__name__, value)

    def SecondsUntilAutoPause(self, value: int):
        return self._set_field(self.SecondsUntilAutoPause.__name__, value)
