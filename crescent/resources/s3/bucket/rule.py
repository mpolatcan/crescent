from crescent.core import Model
from .abort_incomplete_multipart_upload import AbortIncompleteMultipartUpload
from .noncurrent_version_transition import NoncurrentVersionTransition
from .tag_filter import TagFilter
from .transition import Transition
from .constants import AllowedValues, ModelRequiredProperties, Conditions


class Rule(Model):
    def __init__(self):
        super(Rule, self).__init__(
            allowed_values={self.Status.__name__: AllowedValues.RULE_STATUS},
            required_properties=ModelRequiredProperties.RULE,
            conditions={self.Status.__name__: Conditions.RULE_STATUS}
        )

    def AbortIncompleteMultipartUpload(self, abort_incomplete_multipart_upload: AbortIncompleteMultipartUpload):
        return self._set_field(self.AbortIncompleteMultipartUpload.__name__, abort_incomplete_multipart_upload)

    def ExpirationDate(self, expiration_date: str):
        return self._set_field(self.ExpirationDate.__name__, expiration_date)

    def ExpirationInDays(self, expiration_in_days: int):
        return self._set_field(self.ExpirationInDays.__name__, expiration_in_days)

    def Id(self, id: str):
        return self._set_field(self.Id.__name__, id)

    def NoncurrentVersionExpirationInDays(self, noncurrent_version_expiration_in_days: int):
        return self._set_field(self.NoncurrentVersionExpirationInDays.__name__, noncurrent_version_expiration_in_days)

    def NoncurrentVersionTransitions(self, *noncurrent_version_transitions: NoncurrentVersionTransition):
        return self._set_field(self.NoncurrentVersionTransitions.__name__, list(noncurrent_version_transitions))

    def NoncurrentVersionTransition(self, noncurrent_version_transition: NoncurrentVersionTransition):
        return self._set_field(self.NoncurrentVersionTransition.__name__, noncurrent_version_transition)

    def Prefix(self, prefix: str):
        return self._set_field(self.Prefix.__name__, prefix)

    def Status(self, status: str):
        return self._set_field(self.Status.__name__, status)

    def TagFilters(self, *tag_filters: TagFilter):
        return self._set_field(self.TagFilters.__name__, list(tag_filters))

    def Transitions(self, *transitions: Transition):
        return self._set_field(self.Transitions.__name__, list(transitions))

    def Transition(self, transition: Transition):
        return self._set_field(self.Transition.__name__, transition)
