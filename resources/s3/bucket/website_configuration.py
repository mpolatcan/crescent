from typing import List
from resources.shared.base_model import BaseModel
from resources.s3.bucket.redirect_all_request_to import RedirectAllRequestTo
from resources.s3.bucket.routing_rule import RoutingRule


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
        return self._add_field(self.__PROPERTY_REDIRECT_ALL_REQUEST_TO, value.create())

    def routing_rules(self, value: List[RoutingRule]):
        return self._add_field(self.__PROPERTY_ROUTING_RULES, [
            routing_rule.create() for routing_rule in value
        ])