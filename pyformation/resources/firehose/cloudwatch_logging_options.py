from pyformation import PyformationModel


class CloudwatchLoggingOptions(PyformationModel):
    def Enabled(self, value: bool):
        return self._set_field(self.Enabled.__name__, value)

    def LogGroupName(self, value: str):
        return self._set_field(self.LogGroupName.__name__, value)

    def LogStreamName(self, value: str):
        return self._set_field(self.LogStreamName.__name__, value)
