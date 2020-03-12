from pyformation import PyformationModel


class AbortIncompleteMultipartUpload(PyformationModel):
    def DaysAfterInitiation(self, value: int):
        return self._set_field(self.DaysAfterInitiation.__name__, value)
