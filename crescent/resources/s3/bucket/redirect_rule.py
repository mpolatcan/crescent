from crescent.core import Model
from .constants import AllowedValues, Conditions


class RedirectRule(Model):
    def __init__(self):
        super(RedirectRule, self).__init__(
            allowed_values={self.Protocol.__name__: AllowedValues.REDIRECT_RULE_PROTOCOL},
            conditions={self.ReplaceKeyWith.__name__: Conditions.REDIRECT_RULE_REPLACE_KEY_WITH,
                        self.ReplaceKeyPrefixWith.__name__: Conditions.REDIRECT_RULE_REPLACE_KEY_PREFIX_WITH}
        )

    def HostName(self, host_name: str):
        return self._set_field(self.HostName.__name__, host_name)

    def HttpRedirectCode(self, http_redirect_code: str):
        return self._set_field(self.HttpRedirectCode.__name__, http_redirect_code)

    def Protocol(self, protocol: str):
        return self._set_field(self.Protocol.__name__, protocol)

    def ReplaceKeyPrefixWith(self, replace_key_prefix_with: str):
        return self._set_field(self.ReplaceKeyPrefixWith.__name__, replace_key_prefix_with)

    def ReplaceKeyWith(self, replace_key_with: str):
        return self._set_field(self.ReplaceKeyWith.__name__, replace_key_with)
