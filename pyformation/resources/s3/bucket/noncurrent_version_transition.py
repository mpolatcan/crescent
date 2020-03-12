from pyformation import PyformationModel


class NoncurrentVersionTransition(PyformationModel):
    def StorageClass(self, value: str):
        return self._set_field(self.StorageClass.__name__, value)

    def TransitionInDays(self, value: int):
        return self._set_field(self.TransitionInDays.__name__, value)
