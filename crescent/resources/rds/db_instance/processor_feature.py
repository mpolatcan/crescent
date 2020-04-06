from crescent.core import Model


class ProcessorFeature(Model):
    def Name(self, name: str):
        return self._set_field(self.Name.__name__, name)

    def Value(self, value: str):
        return self._set_field(self.Value.__name__, value)
