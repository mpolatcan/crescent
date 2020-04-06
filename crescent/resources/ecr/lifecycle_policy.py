from crescent.core import Model


class LifecyclePolicy(Model):
    def __init__(self):
        super(LifecyclePolicy, self).__init__(
            pattern={self.RegistryId.__name__: r"[0-9]{12}"}
        )

    def LifecyclePolicyText(self, lifecycle_policy_text: str):
        return self._set_field(self.LifecyclePolicyText.__name__, lifecycle_policy_text)

    def RegistryId(self, registry_id: str):
        return self._set_field(self.RegistryId.__name__, registry_id)
