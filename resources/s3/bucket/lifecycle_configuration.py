from typing import List
from resources.shared.base_model import BaseModel
from resources.s3.bucket.rule import Rule


class LifecycleConfiguration(BaseModel):
    __PROPERTY_RULES = "Rules"

    def rules(self, value: List[Rule]):
        return self._add_field(self.__PROPERTY_RULES, [rule.create() for rule in value])
