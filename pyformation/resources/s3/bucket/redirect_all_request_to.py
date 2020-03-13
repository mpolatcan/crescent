from pyformation.core import Model, Validator


class RedirectAllRequestTo(Model):
    @Validator.validate(type=str)
    def HostName(self, value: str):
        return self._set_field(self.HostName.__name__, value)

    @Validator.validate(type=str)
    def Protocol(self, value: str):
        return self._set_field(self.Protocol.__name__, value)
