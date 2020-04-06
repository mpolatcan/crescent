from crescent.core import Model


class OptionSetting(Model):
    def Name(self, name: str):
        return self._set_field(self.Name.__name__, name)

    def Value(self, value: str):
        return self._set_field(self.Value.__name__, value)
