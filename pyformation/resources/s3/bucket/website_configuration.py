from pyformation import PyformationModel
from .redirect_all_request_to import RedirectAllRequestTo
from .routing_rule import RoutingRule


class WebsiteConfiguration(PyformationModel):
    def ErrorDocument(self, value: str):
        return self._set_field(self.ErrorDocument.__name__, value)

    def IndexDocument(self, value: str):
        return self._set_field(self.IndexDocument.__name__, value)

    def RedirectAllRequestTo(self, value: RedirectAllRequestTo):
        return self._set_field(self.RedirectAllRequestTo.__name__, value.__to_dict__())

    def RoutingRules(self, *value: RoutingRule):
        return self._set_field(self.RoutingRules.__name__, [rr.__to_dict__() for rr in list(value)])
