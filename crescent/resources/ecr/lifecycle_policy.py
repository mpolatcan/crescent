from crescent.core import Model, Validator


class LifecyclePolicy(Model):
    @Validator.validate(type=str)
    def LifecyclePolicyText(self, lifecycle_policy_text: str):
        return self._set_field(self.LifecyclePolicyText.__name__, lifecycle_policy_text)

    @Validator.validate(type=str, pattern=r"[0-9]{12}")
    def RegistryId(self, registry_id: str):
        return self._set_field(self.RegistryId.__name__, registry_id)
