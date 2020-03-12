from pyformation import PyformationModel


class LoginProfile(PyformationModel):
    def Password(self, value: str):
        return self._set_field(self.Password.__name__, value)

    def PasswordResetRequired(self, value: bool):
        return self._set_field(self.PasswordResetRequired.__name__, value)
