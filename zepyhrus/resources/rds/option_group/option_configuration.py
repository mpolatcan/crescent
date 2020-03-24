from zepyhrus.core import Model, Validator
from .option_setting import OptionSetting


class OptionConfiguration(Model):
    @Validator.validate(type=str)
    def DBSecurityGroupMemberships(self, *value: str):
        return self._set_field(self.DBSecurityGroupMemberships.__name__, list(value))

    @Validator.validate(type=str)
    def OptionName(self, value: str):
        return self._set_field(self.OptionName.__name__, value)

    @Validator.validate(type=OptionSetting)
    def OptionSettings(self, *value: OptionSetting):
        return self._set_field(self.OptionSettings.__name__, [os.__to_dict__() for os in list(value)])

    @Validator.validate(type=str)
    def OptionVersion(self, value: str):
        return self._set_field(self.OptionVersion.__name__, value)

    @Validator.validate(type=int)
    def Port(self, value: int):
        return self._set_field(self.Port.__name__, value)

    @Validator.validate(type=str)
    def VpcSecurityGroupMemberships(self, *value: str):
        return self._set_field(self.VpcSecurityGroupMemberships.__name__, list(value))
