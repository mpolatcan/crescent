from zepyhrus.core import Model, Validator


class LifecyclePolicy(Model):
    @Validator.validate(type=str)
    def LifecyclePolicyText(self, value: str):
        return self._set_field(self.LifecyclePolicyText.__name__, value)

    @Validator.validate(type=str, pattern=r"[0-9]{12}")
    def RegistryId(self, value: str):
        return self._set_field(self.RegistryId.__name__, value)
