from pyformation.resources.shared import BaseModel


class RedirectRule(BaseModel):
    __PROPERTY_HOST_NAME = "HostName"
    __PROPERTY_HTTP_REDIRECT_CODE = "HttpRedirectCode"
    __PROPERTY_PROTOCOL = "Protocol"
    __PROPERTY_REPLACE_KEY_PREFIX_WITH = "ReplaceKeyPrefixWith"
    __PROPERTY_REPLACE_KEY_WITH = "ReplaceKeyWith"

    def hostname(self, value: str):
        return self._add_field(self.__PROPERTY_HOST_NAME, value)

    def http_redirect_code(self, value: str):
        return self._add_field(self.__PROPERTY_HTTP_REDIRECT_CODE, value)

    def protocol(self, value: str):
        return self._add_field(self.__PROPERTY_PROTOCOL, value)

    def replace_key_prefix_with(self, value: str):
        return self._add_field(self.__PROPERTY_REPLACE_KEY_PREFIX_WITH, value)

    def replace_key_with(self, value: str):
        return self._add_field(self.__PROPERTY_REPLACE_KEY_WITH, value)
