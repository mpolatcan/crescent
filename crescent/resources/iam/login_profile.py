from crescent.core import Model, Validator


class LoginProfile(Model):
    @Validator.validate(type=str)
    def Password(self, password: str):
        return self._set_field(self.Password.__name__, password)

    @Validator.validate(type=bool)
    def PasswordResetRequired(self, password_reset_required: bool):
        return self._set_field(self.PasswordResetRequired.__name__, password_reset_required)
