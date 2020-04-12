from crescent.core import Resource, Tag
from crescent.functions import AnyFn
from .option_configuration import OptionConfiguration
from .constants import ResourceRequiredProperties
from typing import Union


class OptionGroup(Resource):
    __TYPE = "AWS::RDS::OptionGroup"

    def __init__(self, id: str):
        super(OptionGroup, self).__init__(
            id=id,
            type=self.__TYPE,
            required_properties=ResourceRequiredProperties.OPTION_GROUP
        )

    def EngineName(self, engine_name: Union[str, AnyFn]):
        return self._set_property(self.EngineName.__name__, engine_name)

    def MajorEngineVersion(self, major_engine_version: Union[str, AnyFn]):
        return self._set_property(self.MajorEngineVersion.__name__, major_engine_version)

    def OptionConfigurations(self, *option_configurations: OptionConfiguration):
        return self._set_property(self.OptionConfigurations.__name__, list(option_configurations))

    def OptionGroupDescription(self, option_group_description: Union[str, AnyFn]):
        return self._set_property(self.OptionGroupDescription.__name__, option_group_description)

    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
