from resources.shared import BaseModel


class BaseCloudFormationResourceModel(BaseModel):
    __KEY_TYPE = "Type"
    __KEY_PROPERTIES = "Properties"

    def __init__(self, type):
        super(BaseCloudFormationResourceModel, self).__init__()
        self._data[self.__KEY_TYPE] = type

    def _add_property_field(self, property, value):
        if self._data.get(self.__KEY_PROPERTIES, None) is None:
            self._data[self.__KEY_PROPERTIES] = {}

        self._data[self.__KEY_PROPERTIES][property] = value

        return self
