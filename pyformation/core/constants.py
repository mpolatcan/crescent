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


class RequiredProperties:
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