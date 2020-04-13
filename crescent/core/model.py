"""
    Model is a core component of Crescent, it has self validation methods for validating
    data according to given validation data. These validations and data structures
    are listed below:

    - not_specify_if_specified = {<PROPERTY_NAME>: [<PROPERTY_NAME>, ..., <PROPERTY_NAME>]
    - min_value = {<PROPERTY_NAME>:  <MIN_VALUE>, ...}
    - max_value = {<PROPERTY_NAME>: <MAX_VALUE>, ...}
    - min_length = {<PROPERTY_NAME>: <MIN_LENGTH>, ...}
    - max_length = {<PROPERTY_NAME>: <MAX_LENGTH>, ...}
    - pattern = {<PROPERTY_NAME>: <PATTERN>, ...}
    - allowed_values = {<PROPERTY_NAME>: [<ALLOWED_VALUE>,...,<ALLOWED_VALUE>], ...}
    - required_properties = [<REQUIRED_PROPERTY>,...,<REQUIRED_PROPERTY>],
    - conditions = {
        <PROPERTY_NAME>: [([PARAMETERS], <LAMBDA_FN>), ..., ([PARAMETERS], <LAMBDA_FN>)]
      }
"""
from .constants import ValidationFailureMessages
from typing import get_type_hints
import re


class Model:
    __KEY_VALIDATION_RESULT_IS_VALID = "is_valid"
    __KEY_VALIDATION_RESULT_ERROR = "error"
    __VALIDATION_NOT_SPECIFY_IF_SPECIFIED = "not_specify_if_specified"
    __VALIDATION_CONDITIONS = "conditions"
    __VALIDATION_MIN_VALUE = "min_value"
    __VALIDATION_MAX_VALUE = "max_value"
    __VALIDATION_MIN_LENGTH = "min_length"
    __VALIDATION_MAX_LENGTH = "max_length"
    __VALIDATION_PATTERN = "pattern"
    __VALIDATION_ALLOWED_VALUES = "allowed_values"
    __VALIDATION_REQUIRED_PROPERTIES = "required_properties"

    def __init__(self, **validations):
        self.__data = {}
        self.__not_specify_if_specified_validations = validations.get(self.__VALIDATION_NOT_SPECIFY_IF_SPECIFIED, {})
        self.__conditions_validations = validations.get(self.__VALIDATION_CONDITIONS, {})
        self.__min_value_validations = validations.get(self.__VALIDATION_MIN_VALUE, {})
        self.__max_value_validations = validations.get(self.__VALIDATION_MAX_VALUE, {})
        self.__min_length_validations = validations.get(self.__VALIDATION_MIN_LENGTH, {})
        self.__max_length_validations = validations.get(self.__VALIDATION_MAX_LENGTH, {})
        self.__pattern_validations = validations.get(self.__VALIDATION_PATTERN, {})
        self.__allowed_values_validations = validations.get(self.__VALIDATION_ALLOWED_VALUES, {})
        self.__required_properties_validations = validations.get(self.__VALIDATION_REQUIRED_PROPERTIES, [])
        self.__property_types_validations = {
            property_name:
                list(get_type_hints(property_fn).values())[0].__args__
                if type(list(get_type_hints(property_fn).values())[0]).__name__ == "_Union"
                else list(get_type_hints(property_fn).values())[0]
            for property_name, property_fn in [
                (class_attr, getattr(self, class_attr)) for class_attr in dir(self)
                if hasattr(getattr(self, class_attr), "__call__")
                and not re.match(r"[\s]?_[^\s]*|\s?(.*?)\s+?", class_attr)
                and len(get_type_hints(getattr(self, class_attr))) > 0
            ]
        }

    def _set_field(self, key, value):
        self.__data[key] = value

        return self

    def __get_field__(self, key, default=None):
        return self.__data.get(key, default)

    def _pop_field(self, key):
        return self.__data.pop(key)

    def _update_model(self, value):
        self.__data.update(value)

        return self

    def __validation_failure_msg(self, error_msg_prefix, failure_msg_fmt, **kwargs):
        return dict(
            is_valid=False,
            error="{}{}".format(
                error_msg_prefix,
                failure_msg_fmt.format(owner=type(self).__name__, **kwargs)
            )
        )

    def __validation_success_msg(self):
        return dict(is_valid=True)

    def __type_validation(self, property_name, property_value, error_msg_prefix):
        property_type = self.__property_types_validations.get(property_name, None)

        # If type check failed add return error message
        if (property_type is not None) and (not isinstance(property_value, property_type)):
            return self.__validation_failure_msg(error_msg_prefix,
                                                 ValidationFailureMessages.TYPE_VALIDATION,
                                                 prop_name=property_name,
                                                 prop_value=property_value,
                                                 prop_type=property_type)
        else:
            return self.__validation_success_msg()

    def __not_specify_if_specified_validation(self, properties, property_name, error_msg_prefix):
        property_if_specified_properties = self.__not_specify_if_specified_validations.get(property_name, None)

        if property_if_specified_properties is not None:
            for property_if_specified_property in property_if_specified_properties:
                if property_if_specified_property in properties.keys():
                    return self.__validation_failure_msg(error_msg_prefix,
                                                         ValidationFailureMessages.NOT_SPECIFY_IF_SPECIFIED_VALIDATION,
                                                         prop_name=property_name,
                                                         specified_properties=",".join(property_if_specified_properties))

        return self.__validation_success_msg()

    def __condition_validation(self, properties, property_name, error_msg_prefix):
        errors = []

        conditions = self.__conditions_validations.get(property_name, None)

        if conditions:
            for condition in conditions:
                params = []
                condition_params, condition_fn = condition

                for param in condition_params:
                    params.append(properties.get(param, None))

                condition_status = condition_fn(*params)

                if not condition_status[self.__KEY_VALIDATION_RESULT_IS_VALID]:
                    errors.append("{}{}".format(error_msg_prefix, condition_status[self.__KEY_VALIDATION_RESULT_ERROR]))

        if len(errors) > 0:
            return dict(is_valid=False, error=errors)
        else:
            return self.__validation_success_msg()

    def __min_value_validation(self, property_name, property_value, error_msg_prefix):
        property_min_value = self.__min_value_validations.get(property_name, None)

        if (property_value is not None) and (property_min_value is not None) and (property_value < property_min_value):
            return self.__validation_failure_msg(error_msg_prefix,
                                                 ValidationFailureMessages.MIN_VALUE_VALIDATION,
                                                 prop_name=property_name,
                                                 prop_value=property_value,
                                                 min_value=property_min_value)
        else:
            return self.__validation_success_msg()

    def __max_value_validation(self, property_name, property_value, error_msg_prefix):
        property_max_value = self.__max_value_validations.get(property_name, None)

        if (property_value is not None) and (property_max_value is not None) and (property_value > property_max_value):
            return self.__validation_failure_msg(error_msg_prefix,
                                                 ValidationFailureMessages.MAX_VALUE_VALIDATION,
                                                 prop_name=property_name,
                                                 prop_value=property_value,
                                                 max_value=property_max_value)
        else:
            return self.__validation_success_msg()

    def __min_length_validation(self, property_name, property_value, error_msg_prefix):
        property_min_length = self.__min_length_validations.get(property_name, None)

        if (property_value is not None) and (property_min_length is not None) and (len(property_value) < property_min_length):
            return self.__validation_failure_msg(error_msg_prefix,
                                                 ValidationFailureMessages.MIN_LENGTH_VALIDATION,
                                                 prop_name=property_name,
                                                 prop_value=property_value,
                                                 min_length=property_min_length)
        else:
            return self.__validation_success_msg()

    def __max_length_validation(self, property_name, property_value, error_msg_prefix):
        property_max_length = self.__max_length_validations.get(property_name, None)

        if (property_value is not None) and (property_max_length is not None) and (len(property_value) > property_max_length):
            return self.__validation_failure_msg(error_msg_prefix,
                                                 ValidationFailureMessages.MAX_LENGTH_VALIDAITON,
                                                 prop_name=property_name,
                                                 prop_value=property_value,
                                                 max_length=property_max_length)
        else:
            return self.__validation_success_msg()

    def __pattern_validation(self, property_name, property_value, error_msg_prefix):
        property_pattern = self.__pattern_validations.get(property_name, None)

        if (property_value is not None) and (property_pattern is not None) and (not re.match(property_pattern, property_value)):
            return self.__validation_failure_msg(error_msg_prefix,
                                                 ValidationFailureMessages.PATTERN_VALIDATION,
                                                 prop_name=property_name,
                                                 prop_value=property_value,
                                                 pattern=property_pattern)
        else:
            return dict(is_valid=True)

    def __required_properties_validation(self, properties, error_msg_prefix):
        errors = []

        for required_property_name in self.__required_properties_validations:
            if required_property_name not in properties.keys():
                errors.append("{}{}".format(
                    error_msg_prefix,
                    ValidationFailureMessages.REQUIRED_PROPERTIES_VALIDATION.format(
                        owner=type(self).__name__, prop_name=required_property_name
                    )
                ))

        if len(errors) > 0:
            return dict(is_valid=False, error=errors)
        else:
            return self.__validation_success_msg()

    def __allowed_values_validation(self, property_name, property_value, error_msg_prefix):
        property_allowed_values = self.__allowed_values_validations.get(property_name, None)

        if (property_value is not None) and (property_allowed_values is not None) and (property_value not in property_allowed_values):
            return self.__validation_failure_msg(error_msg_prefix,
                                                 ValidationFailureMessages.ALLOWED_VALUES_VALIDATION,
                                                 prop_name=property_name,
                                                 prop_value=property_value,
                                                 allowed_values=",".join(property_allowed_values))
        else:
            return dict(is_valid=True)

    def __validate_helper(self, properties, container, idx_or_key, property_name, property_value, **kwargs):
        errors = []

        # If model is instance of Resource, kwargs has id value of Resource to specify error message
        _id = kwargs.get("id", None)
        error_msg_prefix = "{owner}(id: {id}) -> ".format(owner=type(self).__name__, id=_id) if _id else ""
        is_type_valid = False

        # Validate property's value according to validations defined for this property
        for validation, params in [
            (self.__type_validation, [property_name, property_value, error_msg_prefix]),
            (self.__allowed_values_validation, [property_name, property_value, error_msg_prefix]),
            (self.__min_value_validation, [property_name, property_value, error_msg_prefix]),
            (self.__max_value_validation, [property_name, property_value, error_msg_prefix]),
            (self.__min_length_validation, [property_name, property_value, error_msg_prefix]),
            (self.__max_length_validation, [property_name, property_value, error_msg_prefix]),
            (self.__pattern_validation, [property_name, property_value, error_msg_prefix]),
            (self.__not_specify_if_specified_validation, [properties, property_name, error_msg_prefix]),
            (self.__condition_validation, [properties, property_name, error_msg_prefix])
        ]:
            validation_res = validation(*params)
            is_valid = validation_res[self.__KEY_VALIDATION_RESULT_IS_VALID]

            if not is_valid:
                error_msg = validation_res[self.__KEY_VALIDATION_RESULT_ERROR]
                errors.extend(error_msg) if isinstance(error_msg, list) else errors.append(error_msg)

            # If type validation failed or property value is intrinsic function pass other validations
            if validation == self.__type_validation:
                if is_valid:
                    is_type_valid = True

                    if re.match("Fn*", type(property_value).__base__.__name__):
                        break
                else:
                    break

        # If value type is valid and it is also Model, convert it dict, if has errors save that errors
        if is_type_valid and isinstance(property_value, Model):
            success, output = property_value.__to_dict__(**kwargs)

            if not success:
                errors.extend(output)
            else:
                container[idx_or_key] = output

        return errors

    def __validate(self, properties, **kwargs):
        errors = []

        # If model is instance of Resource, kwargs has id value of Resource to add to error messages of validations
        _id = kwargs.get("id", None)
        error_msg_prefix = "{owner}(id: {id}) -> ".format(owner=type(self).__name__, id=_id) if _id else ""

        # Validate that required properties has defined
        required_properties_validation_res = self.__required_properties_validation(properties, error_msg_prefix)

        if not required_properties_validation_res[self.__KEY_VALIDATION_RESULT_IS_VALID]:
            errors.extend(required_properties_validation_res[self.__KEY_VALIDATION_RESULT_ERROR])

        for property_name, property_value in properties.items():
            # Valid property for validation phase
            if self.__property_types_validations.get(property_name, None):
                if isinstance(property_value, list):
                    for idx, elem in enumerate(property_value):
                        errors.extend(self.__validate_helper(properties=properties,
                                                             container=property_value,
                                                             idx_or_key=idx,
                                                             property_name=property_name,
                                                             property_value=elem,
                                                             **kwargs))
                else:
                    errors.extend(self.__validate_helper(properties=properties,
                                                         container=properties,
                                                         idx_or_key=property_name,
                                                         property_name=property_name,
                                                         property_value=property_value,
                                                         **kwargs))
            # If not valid property for validation and its type dict, traverse that dict
            # recursively until find valid property
            elif isinstance(property_value, dict):
                errors.clear()
                errors.extend(self.__validate(property_value, **kwargs))

        return errors

    def __to_dict__(self, **kwargs):
        errors = self.__validate(self.__data, **kwargs)

        if len(errors) > 0:
            return False, errors
        else:
            return True, self.__data

