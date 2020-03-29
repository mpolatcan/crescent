from itertools import chain


def get_values(obj):
    ignore_keys = ["__module__", "__dict__", "__doc__", "__weakref__"]
    values = [value for key, value in obj.__dict__.items() if key not in ignore_keys]

    if (
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
    class Efs:
        class MountTarget:
            FILE_SYSTEM_ID = "FileSystemId"
            SECURITY_GROUPS = "SecurityGroups"
            SUBNET_ID = "SubnetId"

    class Iam:
        class AccessKey:
            USERNAME = "Username"

        class InstanceProfile:
            ROLES = "Roles"

        class ManagedPolicy:
            POLICY_DOCUMENT = "PolicyDocument"

        class Policy:
            POLICY_DOCUMENT = "PolicyDocument"
            POLICY_NAME = "PolicyName"

        class Role:
            ASSUME_ROLE_POLICY_DOCUMENT = "AssumeRolePolicyDocument"

        class ServiceLinkedRole:
            AWS_SERVICE_NAME = "AWSServiceName"

        class UserToGroupAddition:
            GROUP_NAME = "GroupName"
            USERS = "Users"

    class Kinesis:
        class Stream:
            SHARD_COUNT = "ShardCount"

        class StreamConsumer:
            CONSUMER_NAME = "ConsumerName"
            STREAM_ARN = "StreamARN"

    class Rds:
        class DBCluster:
            ENGINE = "Engine"

        class DBClusterParameterGroup:
            DESCRIPTION = "Description"
            FAMILY = "Family"
            PARAMETERS = "Parameters"

        class DBInstance:
            DB_INSTANCE_CLASS = "DBInstanceClass"

        class DBParameterGroup:
            DESCRIPTION = "Description"
            FAMILY = "Family"

        class DBSecurityGroup:
            DB_SECURITY_GROUP_INGRESS = "DBSecurityGroupIngress"
            GROUP_DESCRIPTION = "GroupDescription"

        class DBSecurityGroupIngress:
            DB_SECURITY_GROUP_NAME = "DBSecurityGroupName"

        class DBSubnetGroup:
            DB_SUBNET_GROUP_DESCRIPTION = "DBSubnetGroupDescription"
            SUBNET_IDS = "SubnetIds"

        class EventSubscription:
            SNS_TOPIC_ARN = "SnsTopicArn"

        class OptionGroup:
            ENGINE_NAME = "EngineName"
            MAJOR_ENGINE_VERSION = "MajorEngineVersion"
            OPTION_CONFIGURATIONS = "OptionConfigurations"
            OPTION_GROUP_DESCRIPTION = "OptionGroupDescription"

    class S3:
        class AccessPoint:
            BUCKET = "Bucket"

        class BucketPolicy:
            BUCKET = "Bucket"
            POLICY_DOCUMENT = "PolicyDocument"

    class ResourceAttr:
        class CodeDeployLambdaAliasUpdate:
            APPLICATION_NAME = "ApplicationName"
            DEPLOYMENT_GROUP_NAME = "DeploymentGroupName"


# --------------------------------------------------------

class ModelRequiredProperties:
    CODE_DEPLOY_LAMBDA_ALIAS_UPDATE_POLICY = get_values(_RequiredProperties.ResourceAttr.CodeDeployLambdaAliasUpdate)

# --------------------------------------------------------


class ResourcesRequiredProperties:
    # -------------- EFS --------------
    MountTarget = get_values(_RequiredProperties.Efs.MountTarget)

    # -------------- IAM --------------
    AccessKey = get_values(_RequiredProperties.Iam.AccessKey)
    InstanceProfile = get_values(_RequiredProperties.Iam.InstanceProfile)
    ManagedPolicy = get_values(_RequiredProperties.Iam.ManagedPolicy)
    Policy = get_values(_RequiredProperties.Iam.Policy)
    Role = get_values(_RequiredProperties.Iam.Role)
    ServiceLinkedRole = get_values(_RequiredProperties.Iam.ServiceLinkedRole)
    UserToGroupAddition = get_values(_RequiredProperties.Iam.UserToGroupAddition)

    # ------------ KINESIS -------------
    Stream = get_values(_RequiredProperties.Kinesis.Stream)
    StreamConsumer = get_values(_RequiredProperties.Kinesis.StreamConsumer)

    # -------------- RDS --------------
    DBCluster = get_values(_RequiredProperties.Rds.DBCluster)
    DBClusterParameterGroup = get_values(_RequiredProperties.Rds.DBClusterParameterGroup)
    DBInstance = get_values(_RequiredProperties.Rds.DBInstance)
    DBParameterGroup = get_values(_RequiredProperties.Rds.DBParameterGroup)
    DBSecurityGroup = get_values(_RequiredProperties.Rds.DBSecurityGroup)
    DBSecurityGroupIngress = get_values(_RequiredProperties.Rds.DBSecurityGroupIngress)
    DBSubnetGroup = get_values(_RequiredProperties.Rds.DBSubnetGroup)
    EventSubscription = get_values(_RequiredProperties.Rds.EventSubscription)
    OptionGroup = get_values(_RequiredProperties.Rds.OptionGroup)

    # -------------- S3 --------------
    AccessPoint = get_values(_RequiredProperties.S3.AccessPoint)
    BucketPolicy = get_values(_RequiredProperties.S3.BucketPolicy)


# --------------------------------------------------------


class AllowedValues:
    REGION = get_values(Region)
    ZONE = get_values(Zone)
