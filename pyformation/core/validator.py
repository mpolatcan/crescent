import re


class __Validator__:
    def __init__(self):
        self.__validations = {
            "min_length": self.__min_length,
            "max_length": self.__max_length,
            "pattern": self.__pattern,
            "type": self.__type
        }

    def __min_length(self, value, length):
        if len(value) < length:
            raise Exception()  # TODO exception message will be changed

        return

    def __max_length(self, value, length):
        if len(value) > length:
            raise Exception()  # TODO exception message will be changed

        return

    def __pattern(self, value, pattern):
        if not re.match(pattern, value):
            raise Exception()  # TODO Exception message will be handled

        return

    def __type(self, value, __type__):
        # List type checks
        if isinstance(value, list):
            invalid_elems = [elem for elem in value if not isinstance(elem, __type__)]

            if len(invalid_elems) > 0:
                raise Exception("Ex-list")  # TODO Exception message will be handled
        elif not isinstance(value, __type__):
            raise Exception("Ex-std")   # TODO Exception message will be handled
        else:
            return

    def validate(self, *args, **kwargs):
        validations = kwargs

        def __decorator__(fn):
            def __wrapper__(*args, **kwargs):
                __wrapper__.__name__ = fn.__name__

                value = args[1] if len(args[1:]) <= 1 else list(args[1:])

                for validation, arg in validations.items():
                    self.__validations[validation](value, arg)

                fn(*args)

                return args[0]

            return __wrapper__

        return __decorator__


Validator = __Validator__()
