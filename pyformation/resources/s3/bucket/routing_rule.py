from pyformation.resources.shared import BaseModel
from pyformation.resources.s3.bucket import RedirectRule, RoutingRuleCondition


class RoutingRule(BaseModel):
    __PROPERTY_REDIRECT_RULE = "RedirectRule"
    __PROPERTY_ROUTING_RULE_CONDITION = "RoutingRuleCondition"

    def redirect_rule(self, value: RedirectRule):
        return self._add_field(self.__PROPERTY_REDIRECT_RULE, value)

    def routing_rule_condition(self, value: RoutingRuleCondition):
        return self._add_field(self.__PROPERTY_ROUTING_RULE_CONDITION, value)
