class PropertyNotDefinedException(Exception):
    pass


class BelowMinValueException(Exception):
    pass


class MaxValueExceededException(Exception):
    pass


class MaxLengthExceededException(Exception):
    pass


class BelowMinLengthException(Exception):
    pass


class PatternMismatchException(Exception):
    pass


class TypeMismatchException(Exception):
    pass


class InvalidValueException(Exception):
    pass


class InvalidPropertySpecificationException(Exception):
    pass


class RequiredPropertyException(Exception):
    pass


class ConditionNotSatisfiedException(Exception):
    pass