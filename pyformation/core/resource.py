from .model import Model


class Resource(Model):
    __KEY_TYPE = "Type"
    __KEY_PROPERTIES = "Properties"

    def __init__(self, id: str, type: str):
        super(Resource, self).__init__()
        self._data[id] = {
            self.__KEY_TYPE: type,
            self.__KEY_PROPERTIES: {}
        }
        self._properties = self._data[id][self.__KEY_PROPERTIES]

    def _set_property(self, property, value):
        self._properties[property] = value

        return self
