from crescent.core import Model, Validator
from .abort_incomplete_multipart_upload import AbortIncompleteMultipartUpload
from .noncurrent_version_transition import NoncurrentVersionTransition
from .tag_filter import TagFilter
from .transition import Transition
from .constants import AllowedValues, ModelRequiredProperties


class Rule(Model):
    @Validator.validate(type=AbortIncompleteMultipartUpload, required_properties=ModelRequiredProperties.ABORT_INCOMPLETE_MULTIPART_UPLOAD)
    def AbortIncompleteMultipartUpload(self, abort_incomplete_multipart_upload: AbortIncompleteMultipartUpload):
        return self._set_field(self.AbortIncompleteMultipartUpload.__name__, abort_incomplete_multipart_upload.__to_dict__())

    @Validator.validate(type=str)
    def ExpirationDate(self, expiration_date: str):
        return self._set_field(self.ExpirationDate.__name__, expiration_date)

    @Validator.validate(type=int)
    def ExpirationInDays(self, expiration_in_days: int):
        return self._set_field(self.ExpirationInDays.__name__, expiration_in_days)

    @Validator.validate(type=str)
    def Id(self, id: str):
        return self._set_field(self.Id.__name__, id)

    @Validator.validate(type=int)
    def NoncurrentVersionExpirationInDays(self, noncurrent_version_expiration_in_days: int):
        return self._set_field(self.NoncurrentVersionExpirationInDays.__name__, noncurrent_version_expiration_in_days)

    @Validator.validate(type=NoncurrentVersionTransition, required_properties=ModelRequiredProperties.NONCURRENT_VERSION_TRANSITION)
    def NoncurrentVersionTransitions(self, *noncurrent_version_transitions: NoncurrentVersionTransition):
        return self._set_field(self.NoncurrentVersionTransitions.__name__, [nvt.__to_dict__() for nvt in list(noncurrent_version_transitions)])

    @Validator.validate(type=NoncurrentVersionTransition, required_properties=ModelRequiredProperties.NONCURRENT_VERSION_TRANSITION)
    def NoncurrentVersionTransition(self, noncurrent_version_transition: NoncurrentVersionTransition):
        return self._set_field(self.NoncurrentVersionTransition.__name__, noncurrent_version_transition.__to_dict__())

    @Validator.validate(type=str)
    def Prefix(self, prefix: str):
        return self._set_field(self.Prefix.__name__, prefix)

    @Validator.validate(type=str, allowed_values=AllowedValues.RULE_STATUS)
    def Status(self, status: str):
        return self._set_field(self.Status.__name__, status)

    @Validator.validate(type=TagFilter, required_properties=ModelRequiredProperties.TAG_FILTER)
    def TagFilters(self, *tag_filters: TagFilter):
        return self._set_field(self.TagFilters.__name__, [tf.__to_dict__() for tf in list(tag_filters)])

    @Validator.validate(type=Transition, required_properties=ModelRequiredProperties.TRANSITION)
    def Transitions(self, *transitions: Transition):
        return self._set_field(self.Transitions.__name__, [t.__to_dict__() for t in list(transitions)])

    @Validator.validate(type=Transition, required_properties=ModelRequiredProperties.TRANSITION)
    def Transition(self, transition: Transition):
        return self._set_field(self.Transition.__name__, transition.__to_dict__())
