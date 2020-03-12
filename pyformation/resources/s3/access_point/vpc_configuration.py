from pyformation import PyformationModel


class VpcConfiguration(PyformationModel):
    def VpcId(self, value: str):
        return self._set_field(self.VpcId.__name__, value)
