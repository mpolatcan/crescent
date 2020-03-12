from pyformation import PyformationModel
from .option_setting import OptionSetting


class OptionConfiguration(PyformationModel):
    def DBSecurityGroupMemberships(self, *value: str):
        return self._set_field(self.DBSecurityGroupMemberships.__name__, list(value))

    def OptionName(self, value: str):
        return self._set_field(self.OptionName.__name__, value)

    def OptionSettings(self, *value: OptionSetting):
        return self._set_field(self.OptionSettings.__name__, [os.__to_dict__() for os in list(value)])

    def OptionVersion(self, value: str):
        return self._set_field(self.OptionVersion.__name__, value)

    def Port(self, value: int):
        return self._set_field(self.Port.__name__, value)

    def VpcSecurityGroupMemberships(self, *value: str):
        return self._set_field(self.VpcSecurityGroupMemberships.__name__, list(value))
