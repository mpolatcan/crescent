from pyformation import PyformationModel


class PublicAccessBlockConfiguration(PyformationModel):
    def BlockPublicAcls(self, value: bool):
        return self._set_field(self.BlockPublicAcls.__name__, value)

    def BlockPublicPolicy(self, value: bool):
        return self._set_field(self.BlockPublicPolicy.__name__, value)

    def IgnorePublicAcls(self, value: bool):
        return self._set_field(self.IgnorePublicAcls.__name__, value)

    def RestrictPublicBuckets(self, value: bool):
        return self._set_field(self.RestrictPublicBuckets.__name__, value)
