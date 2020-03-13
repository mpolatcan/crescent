from pyformation.core import Model, Validator


class Transition(Model):
    @Validator.validate(type=str)
    def StorageClass(self, value: str):
        return self._set_field(self.StorageClass.__name__, value)

    @Validator.validate(type=str)
    def TransitionDate(self, value: str):
        return self._set_field(self.TransitionDate.__name__, value)

    @Validator.validate(type=int)
    def TransitionInDays(self, value: int):
        return self._set_field(self.TransitionInDays.__name__, value)
