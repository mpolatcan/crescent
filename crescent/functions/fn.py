from crescent.core import Model


class Fn(Model):
    def __init__(self, fn_name, **validations):
        super(Fn, self).__init__(**validations)
        self.__fn_name = "Fn::{}".format(fn_name)

    def _set_fn_value(self, value):
        return self._set_field(self.__fn_name, value)

# -------------------------------------


class FnArrayValue(Fn):
    def __init__(self, fn_name, field_order, **validations):
        self.__field_order = field_order

        validations.update({"required_properties": self.__field_order})

        super(FnArrayValue, self).__init__(fn_name=fn_name, **validations)

    def __to_dict__(self, **kwargs):
        conversion_success, conversion_result = super(FnArrayValue, self).__to_dict__()

        if conversion_success:
            self._set_fn_value([self.__get_field__(field) for field in self.__field_order])

            for field in self.__field_order:
                self._pop_field(field)

        return conversion_success, conversion_result

