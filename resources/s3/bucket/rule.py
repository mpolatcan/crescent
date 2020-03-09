from resources.shared import BaseModel
from resources.s3.bucket import (
    AbortIncompleteMultipartUpload,
    NoncurrentVersionTransition,
    TagFilter,
    Transition
)


class Rule(BaseModel):
    __PROPERTY_ABORT_INCOMPLETE_MULTIPART_UPLOAD = "AbortIncompleteMultipartUpload"
    __PROPERTY_EXPIRATION_DATE = "ExpirationDate"
    __PROPERTY_EXPIRATION_IN_DAYS = "ExpirationInDays"
    __PROPERTY_ID = "Id"
    __PROPERTY_NONCURRENT_VERSION_EXPIRATION_IN_DAYS = "NoncurrentVersionExpirationInDays"
    __PROPERTY_NONCURRENT_VERSION_TRANSITION = "NoncurrentVersionTransition"
    __PROPERTY_NONCURRENT_VERSION_TRANSITIONS = "NoncurrentVersionTransitions"
    __PROPERTY_PREFIX = "Prefix"
    __PROPERTY_STATUS = "Status"
    __PROPERTY_TAG_FILTERS = "TagFilters"
    __PROPERTY_TRANSITION = "Transition"
    __PROPERTY_TRANSITIONS = "Transitions"

    def abort_incomplete_multipart_upload(self, value: AbortIncompleteMultipartUpload):
        return self._add_field(self.__PROPERTY_ABORT_INCOMPLETE_MULTIPART_UPLOAD, value.create())

    def expiration_date(self, value: str):
        return self._add_field(self.__PROPERTY_EXPIRATION_DATE, value)

    def expiration_in_days(self, value: int):
        return self._add_field(self.__PROPERTY_EXPIRATION_IN_DAYS, value)

    def id(self, value: str):
        return self._add_field(self.__PROPERTY_ID, value)

    def noncurrent_version_expiration_in_days(self, value: int):
        return self._add_field(self.__PROPERTY_NONCURRENT_VERSION_EXPIRATION_IN_DAYS, value)

    def noncurrent_version_transition(self, value: NoncurrentVersionTransition):
        return self._add_field(self.__PROPERTY_NONCURRENT_VERSION_TRANSITION, value.create())

    def noncurrent_version_transitions(self, *value: NoncurrentVersionTransition):
        return self._add_field(self.__PROPERTY_NONCURRENT_VERSION_TRANSITIONS, [
            noncurrent_v_transition.create() for noncurrent_v_transition in list(value)
        ])

    def prefix(self, value: str):
        return self._add_field(self.__PROPERTY_PREFIX, value)

    def status(self, value: str):
        return self._add_field(self.__PROPERTY_STATUS, value)

    def tag_filters(self, *value: TagFilter):
        return self._add_field(self.__PROPERTY_TAG_FILTERS, [
            tag_filter.create() for tag_filter in list(value)
        ])

    def transition(self, value: Transition):
        return self._add_field(self.__PROPERTY_TRANSITION, value.create())

    def transitions(self, *value: Transition):
        return self._add_field(self.__PROPERTY_TRANSITIONS, [
            transition.create() for transition in list(value)
        ])
