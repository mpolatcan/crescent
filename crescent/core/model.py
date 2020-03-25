class Model:
    def __init__(self):
        self._data = {}

    def _set_field(self, key, value):
        self._data[key] = value

        return self

    def _get_field(self, key, default=None):
        return self._data.get(key, default)

    def __to_dict__(self):
        return self._data
