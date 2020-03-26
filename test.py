from crescent import (
    CrescentFactory as cf,
    S3 as s3,
    Efs as efs,
    Iam as iam,
    Rds as rds,
    Types as types,
    AwsTypes as aws_types
)

cf.Template().Resources(
    s3.Bucket.Create("TestBucket")
    .BucketName("test")
    .LoggingConfiguration(
        s3.Bucket.LoggingConfiguration()
        .DestinationBucketName("log-test")
        .LogFilePrefix("test-prefix")),
    efs.FileSystem.Create("TestEfs")
        .PerformanceMode(efs.FileSystem.PerformanceMode.GENERAL_PURPOSE)
        .Encrypted(True)
        .ThroughputMode(efs.FileSystem.ThroughtputMode.PROVISIONED),
    efs.MountTarget.Create("TestEfsMountTarget")
        .SubnetId("192.168.0.0/0")
        .FileSystemId("TestEfs")
        .SecurityGroups("sg-1", "sg-2", "sg-3"),
    iam.User("TestEcrUser")
        .UserName("test-ecr-user")
        .Groups("test-ecr-group"),
    iam.User("TestS3User")
        .UserName("test-s3-user")
        .Groups("test-s3-group"),
    rds.DBInstance.Create("test")
    .DBInstanceClass(rds.DBInstance.DBInstanceClass.M5_XL_4_VCPU_16GIB_MEM)
    .Engine(rds.DBInstance.Engines.MARIADB),
    rds.DBCluster.Create("test")
    .Engine(rds.DBCluster.Engine.AURORA)
).Parameters(
    cf.Parameter("test", types.CommaDelimitedList),
    cf.Parameter("aws-type-test", aws_types.Ec2.InstanceId)
).YAML("test")
