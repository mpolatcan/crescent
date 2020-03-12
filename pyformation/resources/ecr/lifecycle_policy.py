from pyformation import PyformationModel


class LifecyclePolicy(PyformationModel):
    def LifecyclePolicyText(self, value: str):
        return self._set_field(self.LifecyclePolicyText.__name__, value)

    def RegistryId(self, value: str):
        return self._set_field(self.RegistryId.__name__, value)
