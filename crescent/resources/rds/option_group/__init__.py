from .option_group import OptionGroup
from .option_configuration import OptionConfiguration
from .option_setting import OptionSetting


class OptionGroupFactory:
    @staticmethod
    def Create(id: str): return OptionGroup(id)

    @staticmethod
    def OptionConfiguration(): return OptionConfiguration()

    @staticmethod
    def OptionSetting(): return OptionSetting()


__all__ = ["OptionGroupFactory"]
