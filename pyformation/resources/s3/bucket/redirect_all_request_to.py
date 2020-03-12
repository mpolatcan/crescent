from pyformation import PyformationModel


class RedirectAllRequestTo(PyformationModel):
    def HostName(self, value: str):
        return self._set_field(self.HostName.__name__, value)

    def Protocol(self, value: str):
        return self._set_field(self.Protocol.__name__, value)
