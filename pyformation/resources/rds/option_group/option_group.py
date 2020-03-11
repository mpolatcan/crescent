from pyformation.resources.shared import BaseCloudFormationResourceModel, Tag
from pyformation.resources.rds.option_group import OptionConfiguration


class OptionGroup(BaseCloudFormationResourceModel):
    __TYPE = "AWS::RDS::OptionGroup"
    __PROPERTY_ENGINE_NAME = "EngineName"
    __PROPERTY_MAJOR_ENGINE_VERSION = "MajorEngineVersion"
    __PROPERTY_OPTION_CONFIGURATIONS = "OptionConfigurations"
    __PROPERTY_OPTION_GROUP_DESCRIPTION = "OptionGroupDescription"
    __PROPERTY_TAGS = "Tags"

    def __init__(self):
        super(OptionGroup, self).__init__(type=self.__TYPE)

    def engine_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_ENGINE_NAME, value)

    def major_engine_version(self, value: str):
        return self._add_property_field(self.__PROPERTY_MAJOR_ENGINE_VERSION, value)

    def option_configurations(self, *value: OptionConfiguration):
        return self._add_property_field(self.__PROPERTY_OPTION_CONFIGURATIONS, [
            option_group_conf.create() for option_group_conf in list(value)
        ])

    def option_group_description(self, value: str):
        return self._add_property_field(self.__PROPERTY_OPTION_GROUP_DESCRIPTION, value)

    def tags(self, *value: Tag):
        return self._add_property_field(self.__PROPERTY_TAGS, [
            tag.create() for tag in list(value)
        ])
