from .typesafe_dict import TypeSafeDict
from .constants import Conditions
from .model import Model

# TODO Cloudformation Init Metadata will be added


class Metadata(TypeSafeDict):
    def __init__(self, **validations):
        super(Metadata, self).__init__(**validations)

    def _set_property(self, property, value):
        return self._update_model({property: value})

    def __rearrange_metadata(self):
        json = self.__get_field__(self.Json.__name__)
        kvs = self.__get_field__(self.KeyValue.__name__)

        if json or kvs:
            for key, value in json.items() if json else kvs.items():
                self._set_property(key, value)

            self._pop_field(self.Json.__name__ if json else self.KeyValue.__name__)

    def __to_dict__(self, **kwargs):
        conversion_success, conversion_result = super().__to_dict__()

        if conversion_success:
            self.__rearrange_metadata()

        return conversion_success, conversion_result

# ---------------------------------------------------------------------


class CfnAuthentication(Metadata):
    __METADATA_TYPE_CFN_AUTHENTICATION = "AWS::CloudFormation::Authentication"

    def __init__(self, id: str):
        super(CfnAuthentication, self).__init__(
            conditions={self.type.__name__: Conditions.CLOUDFORMATION_AUTHENTICATION_TYPE},
            required_properties=[self.type.__name__]
        )
        self.__id = id
        self._set_property(self.__METADATA_TYPE_CFN_AUTHENTICATION, {self.__id: {}})

    def __set_property(self, property, value):
        self.__get_field__(self.__METADATA_TYPE_CFN_AUTHENTICATION)[self.__id][property] = value
        return self

    def accessKeyId(self, access_key_id: str):
        return self.__set_property(self.accessKeyId.__name__, access_key_id)

    def buckets(self, *buckets: str):
        return self.__set_property(self.buckets.__name__, ",".join(list(buckets)))

    def password(self, password: str):
        return self.__set_property(self.password.__name__, password)

    def secretKey(self, secret_key: str):
        return self.__set_property(self.secretKey.__name__, secret_key)

    def type(self, type: str):
        return self.__set_property(self.type.__name__, type)

    def uris(self, *uris: str):
        return self.__set_property(self.uris.__name__, ",".join(list(uris)))

    def username(self, username: str):
        return self.__set_property(self.username.__name__, username)

    def roleName(self, role_name: str):
        return self.__set_property(self.roleName.__name__, role_name)

    def Json(self, kvs: dict = None):
        return self  # These methods doesn't use for this class

    def KeyValue(self, **kvs: dict):
        return self  # These methods doesn't use for this class

# ---------------------------------------------------------------------


class Label(Model):
    def default(self, default: str):
        return self._set_field(self.default.__name__, default)


class ParameterGroup(Model):
    def Label(self, label: Label):
        return self._set_field(self.Label.__name__, label)

    def Parameters(self, *parameters: str):
        return self._set_field(self.Parameters.__name__, list(parameters))


class ParameterLabel(Model):
    def __init__(self, id: str):
        super(ParameterLabel, self).__init__()
        self.__id = id

    def Label(self, label: Label):
        return self._set_field(self.Label.__name__, label)


class CfnInterface(Metadata):
    __METADATA_TYPE_CFN_INTERFACE = "AWS::CloudFormation::Interface"

    def __init__(self, id: str):
        super(CfnInterface, self).__init__()
        self.__id = id
        self._set_property(self.__METADATA_TYPE_CFN_INTERFACE, {self.__id: {}})

    def __set_property(self, property, value):
        self.__get_field__(self.__METADATA_TYPE_CFN_INTERFACE)[self.__id][property] = value
        return self

    def ParameterGroups(self, *parameter_groups: ParameterGroup):
        return self.__set_property(self.ParameterGroups.__name__, list(parameter_groups))

    def ParameterLabels(self, *parameter_labels: ParameterLabel):
        return self.__set_property(self.ParameterLabels.__name__, list(parameter_labels))

    def Json(self, kvs: dict):
        return self  # These methods doesn't use for this class

    def KeyValue(self, **kvs: dict):
        return self  # These methods doesn't use for this class

