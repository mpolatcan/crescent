from pyformation.core import Model, Validator
from .constants import AllowedValues, Conditions


class RedirectRule(Model):
    @Validator.validate(type=str)
    def HostName(self, value: str):
        return self._set_field(self.HostName.__name__, value)

    @Validator.validate(type=str)
    def HttpRedirectCode(self, value: str):
        return self._set_field(self.HttpRedirectCode.__name__, value)

    @Validator.validate(type=str, allowed_values=AllowedValues.REDIRECT_RULE_PROTOCOL)
    def Protocol(self, value: str):
        return self._set_field(self.Protocol.__name__, value)

    @Validator.validate(type=str, conditions=Conditions.REPLACE_KEY_PREFIX_WITH)
    def ReplaceKeyPrefixWith(self, value: str):
        return self._set_field(self.ReplaceKeyPrefixWith.__name__, value)

    @Validator.validate(type=str, conditions=Conditions.REPLACE_KEY_WITH)
    def ReplaceKeyWith(self, value: str):
        return self._set_field(self.ReplaceKeyWith.__name__, value)
