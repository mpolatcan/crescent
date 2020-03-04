class BaseModel:
    def __init__(self):
        self._data = {}

    def create(self):
        return self._data

    def _add_field(self, key, value):
        self._data[key] = value

        return self

