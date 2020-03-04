from resources.shared.base_model import BaseModel


class RoutingRuleCondition(BaseModel):
    __PROPERTY_HTTP_ERROR_CODE_RETURNED_EQUALS = "HttpErrorCodeReturnedEquals"
    __PROPERTY_KEY_PREFIX_EQUALS = "KeyPrefixEquals"

    def http_error_code_returned_equals(self, value: str):
        return self._add_field(self.__PROPERTY_HTTP_ERROR_CODE_RETURNED_EQUALS, value)

    def key_prefix_equals(self, value: str):
        return self._add_field(self.__PROPERTY_KEY_PREFIX_EQUALS, value)
