from crescent.core import Model, Validator
from .redirect_all_request_to import RedirectAllRequestTo
from .routing_rule import RoutingRule
from .constants import ModelRequiredProperties


class WebsiteConfiguration(Model):
    @Validator.validate(type=str)
    def ErrorDocument(self, error_document: str):
        return self._set_field(self.ErrorDocument.__name__, error_document)

    @Validator.validate(type=str)
    def IndexDocument(self, index_document: str):
        return self._set_field(self.IndexDocument.__name__, index_document)

    @Validator.validate(type=RedirectAllRequestTo, required_properties=ModelRequiredProperties.REDIRECT_ALL_REQUEST_TO)
    def RedirectAllRequestTo(self, redirect_all_request_to: RedirectAllRequestTo):
        return self._set_field(self.RedirectAllRequestTo.__name__, redirect_all_request_to.__to_dict__())

    @Validator.validate(type=RoutingRule, required_properties=ModelRequiredProperties.ROUTING_RULE)
    def RoutingRules(self, *routing_rules: RoutingRule):
        return self._set_field(self.RoutingRules.__name__, [rr.__to_dict__() for rr in list(routing_rules)])
