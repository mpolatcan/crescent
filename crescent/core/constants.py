from itertools import chain


def get_values(obj, raw=True):
    ignore_keys = ["__module__", "__dict__", "__doc__", "__weakref__"]
    values = [value for key, value in obj.__dict__.items() if key not in ignore_keys]

    if (
        raw and
        not isinstance(values[0], str) and
        not isinstance(values[0], int) and
        not isinstance(values[0], float)
    ):
        return list(chain.from_iterable([list(value.__dict__.values()) for value in values]))
    else:
        return values

# --------------------------------------------------------------------------------


class Region:
    N_VIRGINIA_US_EAST_1 = "us-east-1"
    OHIO_US_EAST_2 = "us-east-2"
    N_CALIFORNIA_US_WEST_1 = "us-west-1"
    OREGON_US_WEST_2 = "us-west-2"
    CANADA_CA_CENTRAL_1 = "ca-central-1"
    HONG_KONG_AP_EAST_1 = "ap-east-1"
    MUMBAI_AP_SOUTH_1 = "ap-south-1"
    SEOUL_AP_NORTHEAST_1 = "ap-northeast-1"
    SINGAPORE_AP_NORTHEAST_2 = "ap-northeast-2"
    SYDNEY_AP_SOUTHEAST_1 = "ap-southeast-1"
    TOKYO_AP_SOUTHEAST_2 = "ap-southeast-2"
    FRANKFURT_EU_CENTRAL_1 = "eu-central-1"
    IRELAND_EU_WEST_1 = "eu-west-1"
    LONDON_EU_WEST_2 = "eu-west-2"
    PARIS_EU_WEST_3 = "eu-west-3"
    STOCKHOLM_EU_NORTH_1 = "eu-north-1"
    SAO_PAULO_SA_EAST_1 = "sa-east-1"

# --------------------------------------------------------------------------------


class _Region2AZ:
    def __init__(self, value):
        self.A = "{}a".format(value)
        self.B = "{}b".format(value)


class _Region3Az(_Region2AZ):
    def __init__(self, value):
        super(_Region3Az, self).__init__(value)
        self.C = "{}c".format(value)


class _Region4Az(_Region3Az):
    def __init__(self, value):
        super(_Region4Az, self).__init__(value)
        self.D = "{}d".format(value)


class _Region6Az(_Region4Az):
    def __init__(self, value):
        super(_Region6Az, self).__init__(value)
        self.E = "{}e".format(value)
        self.F = "{}f".format(value)


class Zone:
    N_VIRGINIA_US_EAST_1 = _Region6Az(Region.N_VIRGINIA_US_EAST_1)
    OHIO_US_EAST_2 = _Region3Az(Region.OHIO_US_EAST_2)
    N_CALIFORNIA_US_WEST_1 = _Region2AZ(Region.N_CALIFORNIA_US_WEST_1)
    OREGON_US_WEST_2 = _Region4Az(Region.OREGON_US_WEST_2)
    CANADA_CA_CENTRAL_1 = _Region2AZ(Region.CANADA_CA_CENTRAL_1)
    HONG_KONG_AP_EAST_1 = _Region3Az(Region.HONG_KONG_AP_EAST_1)
    MUMBAI_AP_SOUTH_1 = _Region3Az(Region.MUMBAI_AP_SOUTH_1)
    SEOUL_AP_NORTHEAST_1 = _Region3Az(Region.SEOUL_AP_NORTHEAST_1)
    SINGAPORE_AP_NORTHEAST_2 = _Region3Az(Region.SINGAPORE_AP_NORTHEAST_2)
    SYDNEY_AP_SOUTHEAST_1 = _Region3Az(Region.SYDNEY_AP_SOUTHEAST_1)
    TOKYO_AP_SOUTHEAST_2 = _Region3Az(Region.TOKYO_AP_SOUTHEAST_2)
    FRANKFURT_EU_CENTRAL_1 = _Region3Az(Region.FRANKFURT_EU_CENTRAL_1)
    IRELAND_EU_WEST_1 = _Region3Az(Region.IRELAND_EU_WEST_1)
    LONDON_EU_WEST_2 = _Region3Az(Region.LONDON_EU_WEST_2)
    PARIS_EU_WEST_3 = _Region3Az(Region.PARIS_EU_WEST_3)
    STOCKHOLM_EU_NORTH_1 = _Region3Az(Region.STOCKHOLM_EU_NORTH_1)
    SAO_PAULO_SA_EAST_1 = _Region3Az(Region.SAO_PAULO_SA_EAST_1)

# --------------------------------------------------------------------------------


class _RequiredProperties:
    class ResourceAttr:
        class CodeDeployLambdaAliasUpdate:
            APPLICATION_NAME = "ApplicationName"
            DEPLOYMENT_GROUP_NAME = "DeploymentGroupName"


# --------------------------------------------------------

class ModelRequiredProperties:
    CODE_DEPLOY_LAMBDA_ALIAS_UPDATE_POLICY = get_values(_RequiredProperties.ResourceAttr.CodeDeployLambdaAliasUpdate)

# --------------------------------------------------------


class AllowedValues:
    REGION = get_values(Region)
    ZONE = get_values(Zone)


# --------------------------------------------------------


class _Property:
    class TypeSafeDict:
        KEY_VALUE = "KeyValue"
        JSON = "Json"

    class CloudFormationAuthentication:
        TYPE = "type"
        ACCESS_KEY_ID = "accessKeyId"
        BUCKETS = "buckets"
        PASSWORD = "password"
        SECRET_KEY = "secretKey"
        URIS = "uris"
        USERNAME = "username"
        ROLE_NAME = "roleName"
# --------------------------------------------------------


class Conditions:
    TYPE_SAFE_DICT_KEY_VALUE = [
        (
            [_Property.TypeSafeDict.JSON],
            lambda json:
                dict(is_valid=True) if not json
                else dict(
                    is_valid=True,
                    error="You cannot use KV method when you used Json method of Mapping!"
                )
        )
    ]
    TYPE_SAFE_DICT_JSON = [
        (
            [_Property.TypeSafeDict.KEY_VALUE],
            lambda key_value:
                dict(is_valid=True) if not key_value
                else dict(
                    is_valid=False,
                    error="You cannot use Json method when you used KV method of Mapping!"
                )
        )
    ]
    CLOUDFORMATION_AUTHENTICATION_TYPE = [
        (
            [
                _Property.CloudFormationAuthentication.TYPE,
                _Property.CloudFormationAuthentication.ACCESS_KEY_ID,
                _Property.CloudFormationAuthentication.BUCKETS,
                _Property.CloudFormationAuthentication.PASSWORD,
                _Property.CloudFormationAuthentication.SECRET_KEY,
                _Property.CloudFormationAuthentication.URIS,
                _Property.CloudFormationAuthentication.USERNAME,
                _Property.CloudFormationAuthentication.ROLE_NAME
            ],
            lambda _type, access_key_id, buckets, password, secret_key, uris, username, role_name:
            dict(
                is_valid=False,
                error=("CloudFormationAuthentication's properties accessKeyId, secretKey, buckets "
                       "and roleName can be specified only if the type is \"S3\"")
            ) if _type != "S3" and (access_key_id or secret_key or buckets or role_name)
            else dict(
                is_valid=False,
                error=("CloudFormationAuthentication's properties accessKeyId and secretKey must be"
                       " defined when the type is \"S3\"")
            ) if _type == "S3" and (not access_key_id or not secret_key)
            else dict(
                is_valid=False,
                error=("CloudFormationAuthentication's properties username, password "
                       "must be defined when type is \"basic\"!")
            ) if _type == "basic" and (not username or not password)
            else dict(is_valid=True)
        )
    ]


# --------------------------------------------------------


class ValidationFailureMessages:
    TYPE_VALIDATION = (
        "{owner}'s property {prop_name}'s value \"{prop_value}\" is not "
        "type of {prop_type}"
    )
    NOT_SPECIFY_IF_SPECIFIED_VALIDATION = (
        "{owner}'s property {prop_name} can't be specified when you have specified one "
        "of these properties {specified_properties}"
    )
    MIN_VALUE_VALIDATION = (
        "{owner}'s property {prop_name}'s value \"{prop_value}\" can't be lower"
        " than min value \"{min_value}\""
    )
    MAX_VALUE_VALIDATION = (
        "{owner}'s property {prop_name}'s value \"{prop_value}\" can't be greater"
        " than max value \"{max_value}\""
    )
    MIN_LENGTH_VALIDATION = (
        "{owner}'s property {prop_name}'s value \"{prop_value}\" length must "
        "be \"{min_length}\" at least"
    )
    MAX_LENGTH_VALIDAITON = (
        "{owner}'s property {prop_name}'s value \"{prop_value}\" length must "
        "be \"{max_length}\" at most"
    )
    PATTERN_VALIDATION = (
        "{owner}'s property {prop_name}'s value \"{prop_value}\" is"
        "not matching regex pattern \"{pattern}\""
    )
    REQUIRED_PROPERTIES_VALIDATION = "{owner}'s property {prop_name} must be defined!"
    ALLOWED_VALUES_VALIDATION = (
        "{owner}'s property {prop_name}'s value \"{prop_value}\" is not valid! Valid values "
        "are \"{allowed_values}\"!"
    )
