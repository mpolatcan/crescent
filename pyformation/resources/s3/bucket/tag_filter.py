from pyformation import PyformationModel


class TagFilter(PyformationModel):
    def Key(self, value: str):
        return self._set_field(self.Key.__name__, value)

    def Value(self, value: str):
        return self._set_field(self.Value.__name__, value)
