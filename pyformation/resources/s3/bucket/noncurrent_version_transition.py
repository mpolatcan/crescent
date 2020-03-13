from pyformation.core import Model, Validator


class NoncurrentVersionTransition(Model):
    @Validator.validate(type=str)
    def StorageClass(self, value: str):
        return self._set_field(self.StorageClass.__name__, value)

    @Validator.validate(type=int)
    def TransitionInDays(self, value: int):
        return self._set_field(self.TransitionInDays.__name__, value)
