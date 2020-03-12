from pyformation import PyformationModel


class KinesisStreamSourceConfiguration(PyformationModel):
    def KinesisStreamARN(self, value: str):
        return self._set_field(self.KinesisStreamARN.__name__, value)

    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)
