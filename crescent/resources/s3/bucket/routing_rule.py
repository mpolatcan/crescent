from crescent.core import Model
from .redirect_rule import RedirectRule
from .routing_rule_condition import RoutingRuleCondition
from .constants import ModelRequiredProperties


class RoutingRule(Model):
    def __init__(self):
        super(RoutingRule, self).__init__(required_properties=ModelRequiredProperties.ROUTING_RULE)

    def RedirectRule(self, redirect_rule: RedirectRule):
        return self._set_field(self.RedirectRule.__name__, redirect_rule)

    def RoutingRuleCondition(self, routing_rule_condition: RoutingRuleCondition):
        return self._set_field(self.RoutingRuleCondition.__name__, routing_rule_condition)
