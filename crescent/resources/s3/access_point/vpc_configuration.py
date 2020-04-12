from crescent.core import Model
from crescent.functions import AnyFn
from typing import Union


class VpcConfiguration(Model):
    def VpcId(self, vpc_id: Union[str, AnyFn]):
        return self._set_field(self.VpcId.__name__, vpc_id)
