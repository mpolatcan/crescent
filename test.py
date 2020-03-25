from crescent import (
    CrescentFactory as cf,
    s3_bucket,
    efs_file_system,
    efs_mount_target,
    iam,
    rds_instance
)

cf.Template().Resources(
    s3_bucket.Bucket("TestBucket")
    .BucketName("test")
    .LoggingConfiguration(
        s3_bucket.LoggingConfiguration()
        .DestinationBucketName("log-test")
        .LogFilePrefix("test-prefix")
    ),
    efs_file_system.FileSystem("TestEfs")
        .PerformanceMode(efs_file_system.performance_mode.GENERAL_PURPOSE)
        .Encrypted(True)
        .ThroughputMode(efs_file_system.throughput_mode.PROVISIONED),
    efs_mount_target.MountTarget("TestEfsMountTarget")
        .SubnetId("192.168.0.0/0")
        .FileSystemId("TestEfs")
        .SecurityGroups("sg-1", "sg-2", "sg-3"),
    iam.User("TestEcrUser")
        .UserName("test-ecr-user")
        .Groups("test-ecr-group"),
    iam.User("TestS3User")
        .UserName("test-s3-user")
        .Groups("test-s3-group"),
    rds_instance.DBInstance("test")
    .DBInstanceClass(rds_instance.instance_class.M5_2XL_8_VCPU_32GIB_MEM)
).YAML("test")
