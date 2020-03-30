from crescent.core import Model, Validator
from .option_setting import OptionSetting


class OptionConfiguration(Model):
    @Validator.validate(type=str)
    def DBSecurityGroupMemberships(self, *db_security_group_memberships: str):
        return self._set_field(self.DBSecurityGroupMemberships.__name__, list(db_security_group_memberships))

    @Validator.validate(type=str)
    def OptionName(self, option_name: str):
        return self._set_field(self.OptionName.__name__, option_name)

    @Validator.validate(type=OptionSetting)
    def OptionSettings(self, *option_settings: OptionSetting):
        return self._set_field(self.OptionSettings.__name__, [os.__to_dict__() for os in list(option_settings)])

    @Validator.validate(type=str)
    def OptionVersion(self, option_version: str):
        return self._set_field(self.OptionVersion.__name__, option_version)

    @Validator.validate(type=int)
    def Port(self, port: int):
        return self._set_field(self.Port.__name__, port)

    @Validator.validate(type=str)
    def VpcSecurityGroupMemberships(self, *vpc_security_group_memberships: str):
        return self._set_field(self.VpcSecurityGroupMemberships.__name__, list(vpc_security_group_memberships))
