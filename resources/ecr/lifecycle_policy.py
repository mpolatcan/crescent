from resources.shared import BaseModel


class LifecyclePolicy(BaseModel):
    __PROPERTY_LIFECYCLE_POLICY_TEXT = "LifecyclePolicyText"
    __PROPERTY_REGISTRY_ID = "RegistryId"

    def lifecycle_policy_texy(self, value: str):
        return self._add_field(self.__PROPERTY_LIFECYCLE_POLICY_TEXT, value)

    def registry_id(self, value):
        return self._add_field(self.__PROPERTY_REGISTRY_ID, value)
