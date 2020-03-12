from pyformation import PyformationModel


class FilterRule(PyformationModel):
    def Name(self, value: str):
        return self._set_field(self.Name.__name__, value)

    def Value(self, value: str):
        return self._set_field(self.Value.__name__, value)
