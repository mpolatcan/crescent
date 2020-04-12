from crescent.core import Model
from crescent.functions import AnyFn
from .processor import Processor
from typing import Union


class ProcessingConfiguration(Model):
    def Enabled(self, enabled: Union[bool, AnyFn]):
        return self._set_field(self.Enabled.__name__, enabled)

    def Processors(self, *processors: Processor):
        return self._set_field(self.Processors.__name__, list(processors))
