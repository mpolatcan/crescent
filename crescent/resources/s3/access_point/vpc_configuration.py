from crescent.core import Model, Validator


class VpcConfiguration(Model):
    @Validator.validate(type=str)
    def VpcId(self, value: str):
        return self._set_field(self.VpcId.__name__, value)
