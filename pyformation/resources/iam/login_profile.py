from pyformation.core import Model, Validator


class LoginProfile(Model):
    @Validator.validate(type=str)
    def Password(self, value: str):
        return self._set_field(self.Password.__name__, value)

    @Validator.validate(type=bool)
    def PasswordResetRequired(self, value: bool):
        return self._set_field(self.PasswordResetRequired.__name__, value)
