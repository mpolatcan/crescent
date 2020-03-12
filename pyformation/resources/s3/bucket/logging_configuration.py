from pyformation import PyformationModel


class LoggingConfiguration(PyformationModel):
    def DestinationBucketName(self, value: str):
        return self._set_field(self.DestinationBucketName.__name__, value)

    def LogFilePrefix(self, value: str):
        return self._set_field(self.LogFilePrefix.__name__, value)
