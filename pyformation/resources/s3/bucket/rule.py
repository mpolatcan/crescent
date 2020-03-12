from pyformation import PyformationModel
from .abort_incomplete_multipart_upload import AbortIncompleteMultipartUpload
from .noncurrent_version_transition import NoncurrentVersionTransition
from .tag_filter import TagFilter
from .transition import Transition


class Rule(PyformationModel):
    def AbortIncompleteMultipartUpload(self, value: AbortIncompleteMultipartUpload):
        return self._set_field(self.AbortIncompleteMultipartUpload.__name__, value.__to_dict__())

    def ExpirationDate(self, value: str):
        return self._set_field(self.ExpirationDate.__name__, value)

    def ExpirationInDays(self, value: int):
        return self._set_field(self.ExpirationInDays.__name__, value)

    def Id(self, value: str):
        return self._set_field(self.Id.__name__, value)

    def NoncurrentVersionExpirationInDays(self, value: int):
        return self._set_field(self.NoncurrentVersionExpirationInDays.__name__, value)

    def NoncurrentVersionTransition(self, value: NoncurrentVersionTransition):
        return self._set_field(self.NoncurrentVersionTransition.__name__, value.__to_dict__())

    def NoncurrentVersionTransitions(self, *value: NoncurrentVersionTransition):
        return self._set_field(self.NoncurrentVersionTransitions.__name__, [nvt.__to_dict__() for nvt in list(value)])

    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)

    def Status(self, value: str):
        return self._set_field(self.Status.__name__, value)

    def TagFilters(self, *value: TagFilter):
        return self._set_field(self.TagFilters.__name__, [tf.__to_dict__() for tf in list(value)])

    def Transition(self, value: Transition):
        return self._set_field(self.Transition.__name__, value.__to_dict__())

    def Transitions(self, *value: Transition):
        return self._set_field(self.Transitions.__name__, [t.__to_dict__() for t in list(value)])
