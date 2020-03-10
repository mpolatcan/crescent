from pyformation.resources.shared import BaseModel


class VpcConfiguration(BaseModel):
    __PROPERTY_VPC_ID = "VpcId"

    def vpc_id(self, value: str):
        return self._add_field(self.__PROPERTY_VPC_ID, value)
