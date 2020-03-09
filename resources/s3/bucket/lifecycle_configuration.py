from resources.shared import BaseModel
from resources.s3.bucket import Rule


class LifecycleConfiguration(BaseModel):
    __PROPERTY_RULES = "Rules"

    def rules(self, *value: Rule):
        return self._add_field(self.__PROPERTY_RULES, [rule.create() for rule in list(value)])
