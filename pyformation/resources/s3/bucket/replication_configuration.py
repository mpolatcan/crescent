from pyformation.resources.shared import BaseModel
from pyformation.resources.s3.bucket import ReplicationRule


class ReplicationConfiguration(BaseModel):
    __PROPERTY_ROLE = "Role"
    __PROPERTY_RULES = "Rules"

    def role(self, value: str):
        return self._add_field(self.__PROPERTY_ROLE, value)

    def rules(self, *value: ReplicationRule):
        return self._add_field(self.__PROPERTY_RULES, [
            replication_rule for replication_rule in list(value)
        ])
