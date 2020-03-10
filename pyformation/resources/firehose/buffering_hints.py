from pyformation.resources.shared import BaseModel


class BufferingHints(BaseModel):
    __PROPERTY_INTERVAL_IN_SECONDS = "IntervalInSeconds"
    __PROPERTY_SIZE_IN_MBS = "SizeInMBs"

    def interval_in_seconds(self, value: int):
        return self._add_field(self.__PROPERTY_INTERVAL_IN_SECONDS, value)

    def size_in_mbs(self, value: int):
        return self._add_field(self.__PROPERTY_SIZE_IN_MBS, value)
