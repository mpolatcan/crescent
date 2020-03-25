from .model import Model


class Mapping(Model):
    def __init__(self, id: str):
        super(Mapping, self).__init__()
        self._data[id] = {}
        self._properties = self._data[id]

    def _set_property(self, property, value):
        self._properties[property] = value

        return self

    def KeyValue(self, key: str, value):
        return self._set_property(key, value)

    def Submappings(self, *mappings):
        for mapping in list(mappings):
            self._properties.update(mapping.__to_dict__())

        return self
