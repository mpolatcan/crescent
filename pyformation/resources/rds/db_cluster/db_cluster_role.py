from pyformation import PyformationModel


class DBClusterRole(PyformationModel):
    def FeatureName(self, value: str):
        return self._set_field(self.FeatureName.__name__, value)

    def RoleArn(self, value: str):
        return self._set_field(self.RoleArn.__name__, value)
