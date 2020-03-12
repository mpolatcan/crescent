from pyformation import PyformationModel


class AccessControlTranslation(PyformationModel):
    def Owner(self, value: str):
        return self._set_field(self.Owner.__name__, value)
