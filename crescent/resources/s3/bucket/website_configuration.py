from crescent.core import Model
from crescent.functions import AnyFn
from .redirect_all_request_to import RedirectAllRequestTo
from .routing_rule import RoutingRule
from typing import Union


class WebsiteConfiguration(Model):
    def ErrorDocument(self, error_document: Union[str, AnyFn]):
        return self._set_field(self.ErrorDocument.__name__, error_document)

    def IndexDocument(self, index_document: Union[str, AnyFn]):
        return self._set_field(self.IndexDocument.__name__, index_document)

    def RedirectAllRequestTo(self, redirect_all_request_to: RedirectAllRequestTo):
        return self._set_field(self.RedirectAllRequestTo.__name__, redirect_all_request_to)

    def RoutingRules(self, *routing_rules: RoutingRule):
        return self._set_field(self.RoutingRules.__name__, list(routing_rules))
