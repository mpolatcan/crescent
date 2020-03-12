from pyformation import PyformationModel


class RedirectRule(PyformationModel):
    def HostName(self, value: str):
        return self._set_field(self.HostName.__name__, value)

    def HttpRedirectCode(self, value: str):
        return self._set_field(self.HttpRedirectCode.__name__, value)

    def Protocol(self, value: str):
        return self._set_field(self.Protocol.__name__, value)

    def ReplaceKeyPrefixWith(self, value: str):
        return self._set_field(self.ReplaceKeyPrefixWith.__name__, value)

    def ReplaceKeyWith(self, value: str):
        return self._set_field(self.ReplaceKeyWith.__name__, value)
