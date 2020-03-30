from crescent.core import Resource, Tag, Validator
from .option_configuration import OptionConfiguration
from .constants import ModelRequiredProperties


class OptionGroup(Resource):
    __TYPE = "AWS::RDS::OptionGroup"

    def __init__(self, id: str):
        super(OptionGroup, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def EngineName(self, engine_name: str):
        return self._set_property(self.EngineName.__name__, engine_name)

    @Validator.validate(type=str)
    def MajorEngineVersion(self, major_engine_version: str):
        return self._set_property(self.MajorEngineVersion.__name__, major_engine_version)

    @Validator.validate(type=OptionConfiguration, required_properties=ModelRequiredProperties.OPTION_CONFIGURATION)
    def OptionConfigurations(self, *option_configurations: OptionConfiguration):
        return self._set_property(self.OptionConfigurations.__name__, [oc.__to_dict__() for oc in list(value)])

    @Validator.validate(type=str)
    def OptionGroupDescription(self, option_group_description: str):
        return self._set_property(self.OptionGroupDescription.__name__, option_group_description)

    @Validator.validate(type=Tag)
    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
