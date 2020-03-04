from typing import List
from resources.shared.base_model import BaseModel
from resources.s3.bucket.filter_rule import FilterRule


class S3KeyFilter(BaseModel):
    __PROPERTY_RULES = "Rules"

    def rules(self, value: List[FilterRule]):
        return self._add_field(self.__PROPERTY_RULES, [
            filter_rule.create() for filter_rule in value
        ])
