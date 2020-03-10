from pyformation.resources.shared import BaseModel


class AbortIncompleteMultipartUpload(BaseModel):
    __PROPERTY_DAYS_AFTER_INITIATION = "DaysAfterInitiation"

    def days_after_initiation(self, value: int):
        return self._add_field(self.__PROPERTY_DAYS_AFTER_INITIATION, value)
