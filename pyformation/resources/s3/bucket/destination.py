from pyformation import PyformationModel


class Destination(PyformationModel):
    def BucketAccountId(self, value: str):
        return self._set_field(self.BucketAccountId.__name__, value)

    def BucketArn(self, value: str):
        return self._set_field(self.BucketArn.__name__, value)

    def Format(self, value: str):
        return self._set_field(self.Format.__name__, value)

    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)
