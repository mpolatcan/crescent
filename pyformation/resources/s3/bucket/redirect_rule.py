from pyformation.core import Model, Validator


class RedirectRule(Model):
    @Validator.validate(type=str)
    def HostName(self, value: str):
        return self._set_field(self.HostName.__name__, value)

    @Validator.validate(type=str)
    def HttpRedirectCode(self, value: str):
        return self._set_field(self.HttpRedirectCode.__name__, value)

    @Validator.validate(type=str)
    def Protocol(self, value: str):
        return self._set_field(self.Protocol.__name__, value)

    @Validator.validate(type=str)
    def ReplaceKeyPrefixWith(self, value: str):
        return self._set_field(self.ReplaceKeyPrefixWith.__name__, value)

    @Validator.validate(type=str)
    def ReplaceKeyWith(self, value: str):
        return self._set_field(self.ReplaceKeyWith.__name__, value)
