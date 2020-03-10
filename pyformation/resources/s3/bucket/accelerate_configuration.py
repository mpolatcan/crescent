from pyformation.resources.shared import BaseModel


class AccelerateConfiguration(BaseModel):
    __PROPERTY_ACCELERATION_STATUS = "AccelerationStatus"

    def acceleration_status(self, value: str):
        return self._add_field(self.__PROPERTY_ACCELERATION_STATUS, value)
