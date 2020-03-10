from pyformation.resources.shared import BaseModel
from pyformation.resources.s3.bucket import RedirectAllRequestTo, RoutingRule


class WebsiteConfiguration(BaseModel):
    __PROPERTY_ERROR_DOCUMENT = "ErrorDocument"
    __PROPERTY_INDEX_DOCUMENT = "IndexDocument"
    __PROPERTY_REDIRECT_ALL_REQUEST_TO = "RedirectAllRequestTo"
    __PROPERTY_ROUTING_RULES = "RoutingRule"

    def error_document(self, value: str):
        return self._add_field(self.__PROPERTY_ERROR_DOCUMENT, value)

    def index_document(self, value: str):
        return self._add_field(self.__PROPERTY_INDEX_DOCUMENT, value)

    def redirect_all_request_to(self, value: RedirectAllRequestTo):
        return self._add_field(self.__PROPERTY_REDIRECT_ALL_REQUEST_TO, value)

    def routing_rules(self, *value: RoutingRule):
        return self._add_field(self.__PROPERTY_ROUTING_RULES, [
            routing_rule for routing_rule in list(value)
        ])
