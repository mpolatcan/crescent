from crescent.core import Model
from crescent.functions import AnyFn
from .constants import ModelRequiredProperties
from typing import Union


class LoginProfile(Model):
    def __init__(self):
        super(LoginProfile, self).__init__(
            required_properties=ModelRequiredProperties.LOGIN_PROFILE
        )

    def Password(self, password: Union[str, AnyFn]):
        return self._set_field(self.Password.__name__, password)

    def PasswordResetRequired(self, password_reset_required: Union[bool, AnyFn]):
        return self._set_field(self.PasswordResetRequired.__name__, password_reset_required)
