from pyformation.resources.shared import BaseModel
from pyformation.resources.s3.bucket import CorsRule


class CorsConfiguration(BaseModel):
    __PROPERTY_CORS_RULES = "CorsRules"

    def cors_rules(self, *value: CorsRule):
        return self._add_field(self.__PROPERTY_CORS_RULES, [
            cors_rule for cors_rule in list(value)
        ])
