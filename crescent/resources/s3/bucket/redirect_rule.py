from crescent.core import Model, Validator
from .constants import AllowedValues, Conditions


class RedirectRule(Model):
    @Validator.validate(type=str)
    def HostName(self, host_name: str):
        return self._set_field(self.HostName.__name__, host_name)

    @Validator.validate(type=str)
    def HttpRedirectCode(self, http_redirect_code: str):
        return self._set_field(self.HttpRedirectCode.__name__, http_redirect_code)

    @Validator.validate(type=str, allowed_values=AllowedValues.REDIRECT_RULE_PROTOCOL)
    def Protocol(self, protocol: str):
        return self._set_field(self.Protocol.__name__, protocol)

    @Validator.validate(type=str, conditions=Conditions.REPLACE_KEY_PREFIX_WITH)
    def ReplaceKeyPrefixWith(self, replace_key_prefix_with: str):
        return self._set_field(self.ReplaceKeyPrefixWith.__name__, replace_key_prefix_with)

    @Validator.validate(type=str, conditions=Conditions.REPLACE_KEY_WITH)
    def ReplaceKeyWith(self, replace_key_with: str):
        return self._set_field(self.ReplaceKeyWith.__name__, replace_key_with)
