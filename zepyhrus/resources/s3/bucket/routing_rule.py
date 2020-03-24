from zepyhrus.core import Model, Validator
from .redirect_rule import RedirectRule
from .routing_rule_condition import RoutingRuleCondition
from .constants import Conditions


class RoutingRule(Model):
    @Validator.validate(type=RedirectRule)
    def RedirectRule(self, value: RedirectRule):
        return self._set_field(self.RedirectRule.__name__, value.__to_dict__())

    @Validator.validate(type=RoutingRuleCondition, conditions=Conditions.ROUTING_RULE_CONDITION)
    def RoutingRuleCondition(self, value: RoutingRuleCondition):
        return self._set_field(self.RoutingRuleCondition.__name__, value.__to_dict__())
