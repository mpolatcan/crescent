from resources.shared import BaseModel
from resources.s3.bucket import FilterRule


class S3KeyFilter(BaseModel):
    __PROPERTY_RULES = "Rules"

    def rules(self, *value: FilterRule):
        return self._add_field(self.__PROPERTY_RULES, [
            filter_rule.create() for filter_rule in list(value)
        ])
