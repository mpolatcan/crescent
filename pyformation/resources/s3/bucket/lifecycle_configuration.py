from pyformation.resources.shared import BaseModel
from pyformation.resources.s3.bucket import Rule


class LifecycleConfiguration(BaseModel):
    __PROPERTY_RULES = "Rules"

    def rules(self, *value: Rule):
        return self._add_field(self.__PROPERTY_RULES, [rule for rule in list(value)])
