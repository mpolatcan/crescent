from typing import List
from resources.shared.base_model import BaseModel
from resources.s3.bucket.cors_rule import CorsRule


class CorsConfiguration(BaseModel):
    __PROPERTY_CORS_RULES = "CorsRules"

    def cors_rules(self, value: List[CorsRule]):
        return self._add_field(self.__PROPERTY_CORS_RULES, [
            cors_rule.create() for cors_rule in value
        ])
