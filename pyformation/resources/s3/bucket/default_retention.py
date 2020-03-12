from pyformation import PyformationModel


class DefaultRetention(PyformationModel):
    def Days(self, value: int):
        return self._set_field(self.Days.__name__, value)

    def Mode(self, value: str):
        return self._set_field(self.Mode.__name__, value)

    def Years(self, value: int):
        return self._set_field(self.Years.__name__, value)
