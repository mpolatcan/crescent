from .resource import Resource
from .exceptions import (
    PropertyNotDefinedException,
    InvalidValueException,
    PatternMismatchException,
    TypeMismatchException,
    MaxLengthExceededException,
    BelowMinLengthException,
    MaxValueExceededException,
    BelowMinValueException,
    InvalidPropertySpecificationException,
    RequiredPropertyException,
    ConditionNotSatisfiedException
)
import re


class __Validator__:
    KEY_MODEL = "model"
    KEY_PROPERTY = "property"
    KEY_VALUE = "value"
    KEY_VALIDATION_VALUE = "validation_value"
    KEY_PARAMETERS = "parameters"
    KEY_CONDITION_FUNCTION = "condition_function"

    def __init__(self):
        self.__validations = {
            "not_specify_if_specified": self.__not_specify_if_specified,
            "conditions": self.__conditions,
            "min_value": self.__min_value,
            "max_value": self.__max_value,
            "min_length": self.__min_length,
            "max_length": self.__max_length,
            "pattern": self.__pattern,
            "allowed_values": self.__allowed_values,
            "required_properties": self.__required_properties,
            "type": self.__type
        }

    def __min_value(self, **kwargs):
        value = kwargs[Validator.KEY_VALUE]
        min_value = kwargs[Validator.KEY_VALIDATION_VALUE]

        if value < min_value:
            raise BelowMinValueException("Value \"{value}\" is below minimum value \"{min_value}\"".format(
                value=value, min_value=min_value
            ))

        return

    def __max_value(self, **kwargs):
        value = kwargs[Validator.KEY_VALUE]
        max_value = kwargs[Validator.KEY_VALIDATION_VALUE]

        if value > max_value:
            raise MaxValueExceededException("Max value exceeded for property {property}! (value: {value}, max: {max_value})".format(
                property=kwargs[Validator.KEY_PROPERTY], value=value, max_value=max_value
            ))

        return

    def __allowed_values(self, **kwargs):
        value = kwargs[Validator.KEY_VALUE]
        allowed_values = kwargs[Validator.KEY_VALIDATION_VALUE]

        if value not in allowed_values:
            raise InvalidValueException("{value} is invalid! Valid values are \"{valid_values}\"".format(
                value=value, valid_values="\", \"".join(allowed_values)
            ))

        return

    def __min_length(self, **kwargs):
        value = kwargs[Validator.KEY_VALUE]
        min_length = kwargs[Validator.KEY_VALIDATION_VALUE]

        if len(value) < min_length:
            raise BelowMinLengthException("String value \"{value}\"'s length below minimum length".format(
                value=value, min_length=min_length
            ))

        return

    def __max_length(self, **kwargs):
        value = kwargs[Validator.KEY_VALUE]
        max_length = kwargs[Validator.KEY_VALIDATION_VALUE]

        if len(value) > max_length:
            raise MaxLengthExceededException("Max length \"{max_length}\" exceeded for value \"{value}\"".format(
                max_length=max_length, value=value
            ))

        return

    def __pattern(self, **kwargs):
        value = kwargs[Validator.KEY_VALUE]
        pattern = kwargs[Validator.KEY_VALIDATION_VALUE]

        if value is not None and not re.match(pattern, value):
            raise PatternMismatchException("Value \"{value}\" is not matching regex pattern \"{pattern}\"".format(
                value=value, pattern=pattern
            ))

        return

    def __not_specify_if_specified(self, **kwargs):
        property = kwargs[Validator.KEY_PROPERTY]
        specified_properties = kwargs[Validator.KEY_VALIDATION_VALUE]
        model_properties = list(kwargs[Validator.KEY_MODEL].__get_properties__().keys())

        for specified_property in specified_properties:
            if specified_property in model_properties:
                raise InvalidPropertySpecificationException(
                    "Property \"{property}\" can't be specified because one of these properties already specified (\"{specified_properties}\")!".format(
                        property=property, specified_properties="\",\"".join(specified_properties)
                    )
                )

        return

    def __type(self, **kwargs):
        value = kwargs[Validator.KEY_VALUE]
        __type__ = kwargs[Validator.KEY_VALIDATION_VALUE]

        if value is None:
            return

        # List type checks
        if isinstance(value, list):
            invalid_elems = [(idx, elem) for idx, elem in enumerate(value) if not isinstance(elem, __type__)]

            if len(invalid_elems) > 0:
                raise TypeMismatchException("Value {value}'s type is not \"{correct_type}\" at index {idx}".format(
                    value=invalid_elems[0][1], correct_type=__type__, idx=invalid_elems[0][0]
                ))
        elif not isinstance(value, __type__):
            raise TypeMismatchException("Value \"{value}\"'s type is not \"{correct_type}\"".format(
                value=value, correct_type=__type__
            ))
        else:
            return

    def __required_properties(self, **kwargs):
        parent_property = type(kwargs[Validator.KEY_MODEL]).__name__
        property_name = kwargs[Validator.KEY_PROPERTY]
        property = kwargs[Validator.KEY_VALUE].__to_dict__()

        for required_property in kwargs[Validator.KEY_VALIDATION_VALUE]:
            if property.get(required_property, None) is None:
                raise RequiredPropertyException("\"{required_property}\" of \"{property}\" must be defined at \"{parent_property}\"".format(
                    required_property=required_property, property=property_name, parent_property=parent_property
                ))

        return

    def __conditions(self, **kwargs):
        model = kwargs[Validator.KEY_MODEL]

        if isinstance(model, Resource):
            model_properties = model.__get_properties__()
        else:
            model_properties = model.__to_dict__()

        conditions = kwargs[Validator.KEY_VALIDATION_VALUE]

        for condition in conditions:
            params = []

            for param in list(condition[0]):
                value = model_properties.get(param, None)

                if value is None:
                    raise PropertyNotDefinedException("Property \"{}\" not defined!".format(param))

                params.append(value)

            result = condition[1](*params)

            if isinstance(result, Exception):
                raise ConditionNotSatisfiedException(str(result))

    def validate(self, *args, **kwargs):
        validations = kwargs

        def __decorator__(fn):
            def __wrapper__(*args, **kwargs):
                __wrapper__.__name__ = fn.__name__

                fn(*args)

                value = args[1] if len(args[1:]) <= 1 else list(args[1:])

                for validation, arg in validations.items():
                    self.__validations[validation](
                        model=args[0],
                        property=fn.__name__,
                        value=value,
                        validation_value=arg
                    )

                return args[0]

            return __wrapper__

        return __decorator__


Validator = __Validator__()
