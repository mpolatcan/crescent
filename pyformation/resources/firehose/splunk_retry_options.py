from pyformation import PyformationModel


class SplunkRetryOptions(PyformationModel):
    def DurationInSeconds(self, value: int):
        return self._set_field(self.DurationInSeconds.__name__, value)
