class BaseModel(dict):
    def __init__(self, parent=None):
        self._parent = parent

    def _add_field(self, key, value):
        self[key] = value

        return self

    def end(self):
        return self._parent
