from typing import List
from resources.shared import BaseModel


class CorsRule(BaseModel):
    __PROPERTY_ALLOWED_HEADERS = "AllowedHeaders"
    __PROPERTY_ALLOWED_METHODS = "AllowedMethods"
    __PROPERTY_ALLOWED_ORIGINS = "AllowedOrigins"
    __PROPERTY_EXPOSED_HEADERS = "ExposedHeaders"
    __PROPERTY_ID = "Id"
    __PROPERTY_MAX_AGE = "MaxAge"

    def allowed_headers(self, value: List[str]):
        return self._add_field(self.__PROPERTY_ALLOWED_HEADERS, value)

    def allowed_methods(self, value: List[str]):
        return self._add_field(self.__PROPERTY_ALLOWED_METHODS, value)

    def allowed_origins(self, value: List[str]):
        return self._add_field(self.__PROPERTY_ALLOWED_ORIGINS, value)

    def exposed_headers(self, value: List[str]):
        return self._add_field(self.__PROPERTY_EXPOSED_HEADERS, value)

    def id(self, value: str):
        return self._add_field(self.__PROPERTY_ID, value)

    def max_age(self, value: int):
        return self._add_field(self.__PROPERTY_MAX_AGE, value)
