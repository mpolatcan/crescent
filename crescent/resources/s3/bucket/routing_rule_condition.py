from crescent.core import Model
from crescent.functions import AnyFn
from .constants import Conditions
from typing import Union


class RoutingRuleCondition(Model):
    def __init__(self):
        super(RoutingRuleCondition, self).__init__(
            conditions={
                self.HttpErrorCodeReturnedEquals.__name__: Conditions.ROUTING_RULE_CONDITION_HTTP_ERROR_CODE_RETURNED_EQUALS,
                self.KeyPrefixEquals.__name__: Conditions.ROUTING_RULE_CONDITION_KEY_PREFIX_EQUALS
            })

    def HttpErrorCodeReturnedEquals(self, http_error_code_returned_equals: Union[str, AnyFn]):
        return self._set_field(self.HttpErrorCodeReturnedEquals.__name__, http_error_code_returned_equals)

    def KeyPrefixEquals(self, key_prefix_equals: Union[str, AnyFn]):
        return self._set_field(self.KeyPrefixEquals.__name__, key_prefix_equals)
