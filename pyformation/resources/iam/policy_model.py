from pyformation import PyformationModel


class PolicyModel(PyformationModel):
    def PolicyDocument(self, value: dict):
        return self._set_field(self.PolicyDocument.__name__, value)

    def PolicyName(self, value: str):
        return self._set_field(self.PolicyName.__name__, value)
