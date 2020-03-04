from typing import List
from resources.shared.base_model import BaseModel
from resources.s3.bucket.replication_rule import ReplicationRule


class ReplicationConfiguration(BaseModel):
    __PROPERTY_ROLE = "Role"
    __PROPERTY_RULES = "Rules"

    def role(self, value: str):
        return self._add_field(self.__PROPERTY_ROLE, value)

    def rules(self, value: List[ReplicationRule]):
        return self._add_field(self.__PROPERTY_RULES, [
            replication_rule.create() for replication_rule in value
        ])
