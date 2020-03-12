from pyformation import PyformationModel


class AccelerateConfiguration(PyformationModel):
    def AccelerationStatus(self, value: str):
        return self._set_field(self.AccelerationStatus.__name__, value)
