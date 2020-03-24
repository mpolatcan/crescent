from .resource import Resource
from .exceptions import (
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
    VALIDATION_NOT_SPECIFY_IF_SPECIFIED = "not_specify_if_specified"
    VALIDATION_CONDITIONS = "conditions"
    VALIDATION_MIN_VALUE = "min_value"
    VALIDATION_MAX_VALUE = "max_value"
    VALIDATION_MIN_LENGTH = "min_length"
    VALIDATION_MAX_LENGTH = "max_length"
    VALIDATION_PATTERN = "pattern"
    VALIDATION_ALLOWED_VALUES = "allowed_values"
    VALIDATION_REQUIRED_PROPERTIES = "required_properties"
    VALIDATION_TYPE = "type"

    def __init__(self):
        self.__validations = {
            self.VALIDATION_NOT_SPECIFY_IF_SPECIFIED: self.__not_specify_if_specified,
            self.VALIDATION_CONDITIONS: self.__conditions,
            self.VALIDATION_MIN_VALUE: self.__min_value,
            self.VALIDATION_MAX_VALUE: self.__max_value,
            self.VALIDATION_MIN_LENGTH: self.__min_length,
            self.VALIDATION_MAX_LENGTH: self.__max_length,
            self.VALIDATION_PATTERN: self.__pattern,
            self.VALIDATION_ALLOWED_VALUES: self.__allowed_values,
            self.VALIDATION_REQUIRED_PROPERTIES: self.__required_properties,
            self.VALIDATION_TYPE: self.__type
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

        if not isinstance(value, __type__):
            raise TypeMismatchException("Value \"{value}\"'s type is not \"{correct_type}\"".format(
                value=value, correct_type=__type__
            ))
        else:
            return

    def __required_properties(self, **kwargs):
        parent_property_name = type(kwargs[Validator.KEY_MODEL]).__name__
        sub_property_name = kwargs[Validator.KEY_PROPERTY]
        sub_property_value_name = type(kwargs[Validator.KEY_VALUE]).__name__

        if isinstance(kwargs[Validator.KEY_VALUE], Resource):
            value = kwargs[Validator.KEY_VALUE].__get_properties__()
            validation_value = getattr(kwargs[Validator.KEY_VALIDATION_VALUE], sub_property_value_name, [])
        else:
            value = kwargs[Validator.KEY_VALUE].__to_dict__()
            validation_value = kwargs[Validator.KEY_VALIDATION_VALUE]

        for required_property in validation_value:
            if value.get(required_property, None) is None:
                raise RequiredPropertyException("\"{required_property}\" of \"{sub_property_value}\" must be defined at \"{parent_property}.{sub_property}\"".format(
                    required_property=required_property, sub_property_value=sub_property_value_name, parent_property=parent_property_name, sub_property=sub_property_name
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
            param_keys = condition[0]
            condition_fn = condition[1]

            for param_key in param_keys:
                params.append(model_properties.get(param_key, None))

            result = condition_fn(*params) if condition_fn else None

            if isinstance(result, Exception):
                raise ConditionNotSatisfiedException(str(result))

    def validate(self, *args, **kwargs):
        validations = kwargs

        def __decorator__(fn):
            def __wrapper__(*args, **kwargs):
                __wrapper__.__name__ = fn.__name__

                # Type validation
                for value in list(args[1:]):
                    self.__validations[self.VALIDATION_TYPE](
                        model=args[0],
                        property=fn.__name__,
                        value=value,
                        validation_value=validations[self.VALIDATION_TYPE]
                    )

                fn(*args)

                # Other validations
                for value in list(args[1:]):
                    for validation, arg in validations.items():
                        if validation != self.VALIDATION_TYPE:
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
