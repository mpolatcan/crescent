from pyformation import PyformationModel


class BufferingHints(PyformationModel):
    def IntervalInSeconds(self, value: int):
        return self._set_field(self.IntervalInSeconds.__name__, value)

    def SizeInMBs(self, value: int):
        return self._set_field(self.SizeInMBs.__name__, value)
