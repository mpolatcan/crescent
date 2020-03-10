from pyformation.resources.shared import BaseModel
from pyformation.resources.s3.bucket import FilterRule


class S3KeyFilter(BaseModel):
    __PROPERTY_RULES = "Rules"

    def rules(self, *value: FilterRule):
        return self._add_field(self.__PROPERTY_RULES, [
            filter_rule for filter_rule in list(value)
        ])