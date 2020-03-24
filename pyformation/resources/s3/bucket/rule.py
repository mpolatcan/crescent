from pyformation.core import Model, Validator
from .abort_incomplete_multipart_upload import AbortIncompleteMultipartUpload
from .noncurrent_version_transition import NoncurrentVersionTransition
from .tag_filter import TagFilter
from .transition import Transition
from .constants import AllowedValues, RequiredProperties


class Rule(Model):
    @Validator.validate(type=AbortIncompleteMultipartUpload, required_properties=RequiredProperties.ABORT_INCOMPLETE_MULTIPART_UPLOAD)
    def AbortIncompleteMultipartUpload(self, value: AbortIncompleteMultipartUpload):
        return self._set_field(self.AbortIncompleteMultipartUpload.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def ExpirationDate(self, value: str):
        return self._set_field(self.ExpirationDate.__name__, value)

    @Validator.validate(type=int)
    def ExpirationInDays(self, value: int):
        return self._set_field(self.ExpirationInDays.__name__, value)

    @Validator.validate(type=str)
    def Id(self, value: str):
        return self._set_field(self.Id.__name__, value)

    @Validator.validate(type=int)
    def NoncurrentVersionExpirationInDays(self, value: int):
        return self._set_field(self.NoncurrentVersionExpirationInDays.__name__, value)

    @Validator.validate(type=NoncurrentVersionTransition, required_properties=RequiredProperties.NONCURRENT_VERSION_TRANSITION)
    def NoncurrentVersionTransitions(self, *value: NoncurrentVersionTransition):
        return self._set_field(self.NoncurrentVersionTransitions.__name__, [nvt.__to_dict__() for nvt in list(value)])

    @Validator.validate(type=NoncurrentVersionTransition, required_properties=RequiredProperties.NONCURRENT_VERSION_TRANSITION)
    def NoncurrentVersionTransition(self, value: NoncurrentVersionTransition):
        return self._set_field(self.NoncurrentVersionTransition.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)

    @Validator.validate(type=str, allowed_values=AllowedValues.RULE_STATUS)
    def Status(self, value: str):
        return self._set_field(self.Status.__name__, value)

    @Validator.validate(type=TagFilter, required_properties=RequiredProperties.TAG_FILTER)
    def TagFilters(self, *value: TagFilter):
        return self._set_field(self.TagFilters.__name__, [tf.__to_dict__() for tf in list(value)])

    @Validator.validate(type=Transition, required_properties=RequiredProperties.TRANSITION)
    def Transitions(self, *value: Transition):
        return self._set_field(self.Transitions.__name__, [t.__to_dict__() for t in list(value)])

    @Validator.validate(type=Transition, required_properties=RequiredProperties.TRANSITION)
    def Transition(self, value: Transition):
        return self._set_field(self.Transition.__name__, value.__to_dict__())