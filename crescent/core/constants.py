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


class Region2AZ:
    def __init__(self, value):
        self.A = "{}a".format(value)
        self.B = "{}b".format(value)


class Region3Az(Region2AZ):
    def __init__(self, value):
        super(Region3Az, self).__init__(value)
        self.C = "{}c".format(value)


class Region4Az(Region3Az):
    def __init__(self, value):
        super(Region4Az, self).__init__(value)
        self.D = "{}d".format(value)


class Region6Az(Region4Az):
    def __init__(self, value):
        super(Region6Az, self).__init__(value)
        self.E = "{}e".format(value)
        self.F = "{}f".format(value)


class Zone:
    N_VIRGINIA_US_EAST_1 = Region6Az(Region.N_VIRGINIA_US_EAST_1)
    OHIO_US_EAST_2 = Region3Az(Region.OHIO_US_EAST_2)
    N_CALIFORNIA_US_WEST_1 = Region2AZ(Region.N_CALIFORNIA_US_WEST_1)
    OREGON_US_WEST_2 = Region4Az(Region.OREGON_US_WEST_2)
    CANADA_CA_CENTRAL_1 = Region2AZ(Region.CANADA_CA_CENTRAL_1)
    HONG_KONG_AP_EAST_1 = Region3Az(Region.HONG_KONG_AP_EAST_1)
    MUMBAI_AP_SOUTH_1 = Region3Az(Region.MUMBAI_AP_SOUTH_1)
    SEOUL_AP_NORTHEAST_1 = Region3Az(Region.SEOUL_AP_NORTHEAST_1)
    SINGAPORE_AP_NORTHEAST_2 = Region3Az(Region.SINGAPORE_AP_NORTHEAST_2)
    SYDNEY_AP_SOUTHEAST_1 = Region3Az(Region.SYDNEY_AP_SOUTHEAST_1)
    TOKYO_AP_SOUTHEAST_2 = Region3Az(Region.TOKYO_AP_SOUTHEAST_2)
    FRANKFURT_EU_CENTRAL_1 = Region3Az(Region.FRANKFURT_EU_CENTRAL_1)
    IRELAND_EU_WEST_1 = Region3Az(Region.IRELAND_EU_WEST_1)
    LONDON_EU_WEST_2 = Region3Az(Region.LONDON_EU_WEST_2)
    PARIS_EU_WEST_3 = Region3Az(Region.PARIS_EU_WEST_3)
    STOCKHOLM_EU_NORTH_1 = Region3Az(Region.STOCKHOLM_EU_NORTH_1)
    SAO_PAULO_SA_EAST_1 = Region3Az(Region.SAO_PAULO_SA_EAST_1)

# --------------------------------------------------------------------------------


class Property:
    EFS_MOUNT_TARGET_FILE_SYSTEM_ID = "FileSystemId"
    EFS_MOUNT_TARGET_SECURITY_GROUPS = "SecurityGroups"
    EFS_MOUNT_TARGET_SUBNET_ID = "SubnetId"
    IAM_ACCESS_KEY_USERNAME = "Username"
    IAM_INSTANCE_PROFILE_ROLES = "Roles"
    IAM_MANAGED_POLICY_POLICY_DOCUMENT = "PolicyDocument"
    IAM_POLICY_POLICY_DOCUMENT = "PolicyDocument"
    IAM_POLICY_POLICY_NAME = "PolicyName"
    IAM_ROLE_ASSUME_ROLE_POLICY_DOCUMENT = "AssumeRolePolicyDocument"
    IAM_SERVICE_LINKED_ROLE_AWS_SERVICE_NAME = "AWSServiceName"
    IAM_USER_TO_GROUP_ADDITION_GROUP_NAME = "GroupName"
    IAM_USER_TO_GROUP_ADDITION_USERS = "Users"
    KINESIS_STREAM_SHARD_COUNT = "ShardCount"
    KINESIS_STREAM_CONSUMER_CONSUMER_NAME = "ConsumerName"
    KINESIS_STREAM_CONSUMER_STREAM_ARN = "StreamARN"
    RDS_DB_CLUSTER_ENGINE = "Engine"
    RDS_DB_CLUSTER_PARAMETER_GROUP_DESCRIPTION = "Description"
    RDS_DB_CLUSTER_PARAMETER_GROUP_FAMILY = "Family"
    RDS_DB_CLUSTER_PARAMETER_GROUP_PARAMETERS = "Parameters"
    RDS_DB_INSTANCE_DB_INSTANCE_CLASS = "DBInstanceClass"
    RDS_DB_PARAMETER_GROUP_DESCRIPTION = "Description"
    RDS_DB_PARAMETER_GROUP_FAMILY = "Family"
    RDS_DB_SECURITY_GROUP_DB_SECURITY_GROUP_INGRESS = "DBSecurityGroupIngress"
    RDS_DB_SECURITY_GROUP_GROUP_DESCRIPTION = "GroupDescription"
    RDS_DB_SECURITY_GROUP_INGRESS_DB_SECURITY_GROUP_NAME = "DBSecurityGroupName"
    RDS_DB_SUBNET_GROUP_DB_SUBNET_GROUP_DESCRIPTION = "DBSubnetGroupDescription"
    RDS_DB_SUBNET_GROUP_SUBNET_IDS = "SubnetIds"
    RDS_EVENT_SUBSCRIPTION_SNS_TOPIC_ARN = "SnsTopicArn"
    RDS_OPTION_GROUP_ENGINE_NAME = "EngineName"
    RDS_OPTION_GROUP_MAJOR_ENGINE_VERSION = "MajorEngineVersion"
    RDS_OPTION_GROUP_OPTION_CONFIGURATIONS = "OptionConfigurations"
    RDS_OPTION_GROUP_OPTION_GROUP_DESCRIPTION = "OptionGroupDescription"
    S3_ACCESS_POINT_BUCKET = "Bucket"
    S3_BUCKET_POLICY_BUCKET = "Bucket"
    S3_BUCKET_POLICY_POLICY_DOCUMENT = "PolicyDocument"
    CODE_DEPLOY_LAMBDA_ALIAS_UPDATE_APPLICATION_NAME = "ApplicationName"
    CODE_DEPLOY_LAMBDA_ALIAS_UPDATE_DEPLOYMENT_GROUP_NAME = "DeploymentGroupNmae"


# --------------------------------------------------------

class AllowedValues:
    REGION = [
        Region.N_VIRGINIA_US_EAST_1,
        Region.OHIO_US_EAST_2,
        Region.N_CALIFORNIA_US_WEST_1,
        Region.OREGON_US_WEST_2,
        Region.CANADA_CA_CENTRAL_1,
        Region.HONG_KONG_AP_EAST_1,
        Region.MUMBAI_AP_SOUTH_1,
        Region.SEOUL_AP_NORTHEAST_1,
        Region.SINGAPORE_AP_NORTHEAST_2,
        Region.SYDNEY_AP_SOUTHEAST_1,
        Region.TOKYO_AP_SOUTHEAST_2,
        Region.FRANKFURT_EU_CENTRAL_1,
        Region.IRELAND_EU_WEST_1,
        Region.LONDON_EU_WEST_2,
        Region.PARIS_EU_WEST_3,
        Region.STOCKHOLM_EU_NORTH_1,
        Region.SAO_PAULO_SA_EAST_1
    ]
    ZONE = [
        Zone.N_VIRGINIA_US_EAST_1.A,
        Zone.N_VIRGINIA_US_EAST_1.B,
        Zone.N_VIRGINIA_US_EAST_1.C,
        Zone.N_VIRGINIA_US_EAST_1.D,
        Zone.N_VIRGINIA_US_EAST_1.E,
        Zone.N_VIRGINIA_US_EAST_1.F,
        Zone.OHIO_US_EAST_2.A,
        Zone.OHIO_US_EAST_2.B,
        Zone.OHIO_US_EAST_2.C,
        Zone.N_CALIFORNIA_US_WEST_1.A,
        Zone.N_CALIFORNIA_US_WEST_1.B,
        Zone.OREGON_US_WEST_2.A,
        Zone.OREGON_US_WEST_2.B,
        Zone.OREGON_US_WEST_2.C,
        Zone.OREGON_US_WEST_2.D,
        Zone.CANADA_CA_CENTRAL_1.A,
        Zone.CANADA_CA_CENTRAL_1.B,
        Zone.HONG_KONG_AP_EAST_1.A,
        Zone.HONG_KONG_AP_EAST_1.B,
        Zone.HONG_KONG_AP_EAST_1.C,
        Zone.MUMBAI_AP_SOUTH_1.A,
        Zone.MUMBAI_AP_SOUTH_1.B,
        Zone.MUMBAI_AP_SOUTH_1.C,
        Zone.SEOUL_AP_NORTHEAST_1.A,
        Zone.SEOUL_AP_NORTHEAST_1.B,
        Zone.SEOUL_AP_NORTHEAST_1.C,
        Zone.SINGAPORE_AP_NORTHEAST_2.A,
        Zone.SINGAPORE_AP_NORTHEAST_2.B,
        Zone.SINGAPORE_AP_NORTHEAST_2.C,
        Zone.SYDNEY_AP_SOUTHEAST_1.A,
        Zone.SYDNEY_AP_SOUTHEAST_1.B,
        Zone.SYDNEY_AP_SOUTHEAST_1.C,
        Zone.TOKYO_AP_SOUTHEAST_2.A,
        Zone.TOKYO_AP_SOUTHEAST_2.B,
        Zone.TOKYO_AP_SOUTHEAST_2.C,
        Zone.FRANKFURT_EU_CENTRAL_1.A,
        Zone.FRANKFURT_EU_CENTRAL_1.B,
        Zone.FRANKFURT_EU_CENTRAL_1.C,
        Zone.IRELAND_EU_WEST_1.A,
        Zone.IRELAND_EU_WEST_1.B,
        Zone.IRELAND_EU_WEST_1.C,
        Zone.LONDON_EU_WEST_2.A,
        Zone.LONDON_EU_WEST_2.B,
        Zone.LONDON_EU_WEST_2.C,
        Zone.PARIS_EU_WEST_3.A,
        Zone.PARIS_EU_WEST_3.B,
        Zone.PARIS_EU_WEST_3.C,
        Zone.STOCKHOLM_EU_NORTH_1.A,
        Zone.STOCKHOLM_EU_NORTH_1.B,
        Zone.STOCKHOLM_EU_NORTH_1.C,
        Zone.SAO_PAULO_SA_EAST_1.A,
        Zone.SAO_PAULO_SA_EAST_1.B,
        Zone.SAO_PAULO_SA_EAST_1.C
    ]
# --------------------------------------------------------


class RequiredProperties:
    CODE_DEPLOY_LAMBDA_ALIAS_UPDATE_POLICY = [
        Property.CODE_DEPLOY_LAMBDA_ALIAS_UPDATE_APPLICATION_NAME,
        Property.CODE_DEPLOY_LAMBDA_ALIAS_UPDATE_DEPLOYMENT_GROUP_NAME
    ]

# --------------------------------------------------------


class ResourcesRequiredProperties:
    # -------------- EFS --------------
    MountTarget = [
        Property.EFS_MOUNT_TARGET_FILE_SYSTEM_ID,
        Property.EFS_MOUNT_TARGET_SECURITY_GROUPS,
        Property.EFS_MOUNT_TARGET_SUBNET_ID
    ]

    # -------------- IAM --------------
    AccessKey = [
        Property.IAM_ACCESS_KEY_USERNAME
    ]
    InstanceProfile = [
        Property.IAM_INSTANCE_PROFILE_ROLES
    ]
    ManagedPolicy = [
        Property.IAM_MANAGED_POLICY_POLICY_DOCUMENT
    ]
    Policy = [
        Property.IAM_POLICY_POLICY_DOCUMENT,
        Property.IAM_POLICY_POLICY_NAME
    ]
    Role = [
        Property.IAM_ROLE_ASSUME_ROLE_POLICY_DOCUMENT
    ]
    ServiceLinkedRole = [
        Property.IAM_SERVICE_LINKED_ROLE_AWS_SERVICE_NAME
    ]
    UserToGroupAddition = [
        Property.IAM_USER_TO_GROUP_ADDITION_GROUP_NAME,
        Property.IAM_USER_TO_GROUP_ADDITION_USERS
    ]

    # ------------ KINESIS -------------
    Stream = [
        Property.KINESIS_STREAM_SHARD_COUNT
    ]
    StreamConsumer = [
        Property.KINESIS_STREAM_CONSUMER_CONSUMER_NAME,
        Property.KINESIS_STREAM_CONSUMER_STREAM_ARN
    ]

    # -------------- RDS --------------
    DBCluster = [
        Property.RDS_DB_CLUSTER_ENGINE
    ]
    DBClusterParameterGroup = [
        Property.RDS_DB_CLUSTER_PARAMETER_GROUP_DESCRIPTION,
        Property.RDS_DB_CLUSTER_PARAMETER_GROUP_FAMILY,
        Property.RDS_DB_CLUSTER_PARAMETER_GROUP_PARAMETERS
    ]
    DBInstance = [
        Property.RDS_DB_INSTANCE_DB_INSTANCE_CLASS
    ]
    DBParameterGroup = [
        Property.RDS_DB_PARAMETER_GROUP_DESCRIPTION,
        Property.RDS_DB_PARAMETER_GROUP_FAMILY
    ]
    DBSecurityGroup = [
        Property.RDS_DB_SECURITY_GROUP_DB_SECURITY_GROUP_INGRESS,
        Property.RDS_DB_SECURITY_GROUP_GROUP_DESCRIPTION
    ]
    DBSecurityGroupIngress = [
        Property.RDS_DB_SECURITY_GROUP_INGRESS_DB_SECURITY_GROUP_NAME
    ]
    DBSubnetGroup = [
        Property.RDS_DB_SUBNET_GROUP_DB_SUBNET_GROUP_DESCRIPTION,
        Property.RDS_DB_SUBNET_GROUP_SUBNET_IDS
    ]
    EventSubscription = [
        Property.RDS_EVENT_SUBSCRIPTION_SNS_TOPIC_ARN
    ]
    OptionGroup = [
        Property.RDS_OPTION_GROUP_ENGINE_NAME,
        Property.RDS_OPTION_GROUP_MAJOR_ENGINE_VERSION,
        Property.RDS_OPTION_GROUP_OPTION_CONFIGURATIONS,
        Property.RDS_OPTION_GROUP_OPTION_GROUP_DESCRIPTION
    ]

    # -------------- S3 --------------
    AccessPoint = [
        Property.S3_ACCESS_POINT_BUCKET
    ]
    BucketPolicy = [
        Property.S3_BUCKET_POLICY_BUCKET,
        Property.S3_BUCKET_POLICY_POLICY_DOCUMENT
    ]