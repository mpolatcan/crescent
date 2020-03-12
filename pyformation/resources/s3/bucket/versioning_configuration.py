from pyformation import PyformationModel


class VersioningConfiguration(PyformationModel):
    def Status(self, value: str):
        return self._set_field(self.Status.__name__, value)
