from pyformation import PyformationModel


class Transition(PyformationModel):
    def StorageClass(self, value: str):
        return self._set_field(self.StorageClass.__name__, value)

    def TransitionDate(self, value: str):
        return self._set_field(self.TransitionDate.__name__, value)

    def TransitionInDays(self, value: int):
        return self._set_field(self.TransitionInDays.__name__, value)
