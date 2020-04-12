from .model import Model
from crescent.functions import AnyFn


class Condition(Model):
    def __init__(self, id: str):
        super(Condition, self).__init__()
        self.__id = id

    def Fn(self, fn: AnyFn):
        return self._set_field(self.Fn.__name__, fn)

    def __to_dict__(self, **kwargs):
        conversion_success, conversion_result = super(Condition, self).__to_dict__(id=self.__id)

        if conversion_success:
            self._set_field(self.__id, self.__get_field__(self.Fn.__name__))
            self._pop_field(self.Fn.__name__)

        return conversion_success, conversion_result

