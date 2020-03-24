from zepyhrus import ZepyhrusFactory as zf
from zepyhrus import iam, s3_bucket, rds_cluster

zf.Template().Resources(
    iam.User("TestUser")
    .UserName("test-user"),
    s3_bucket.Bucket("test-bucket")
    .PublicAccessBlockConfiguration(
        s3_bucket.PublicAccessBlockConfiguration()
        .BlockPublicAcls(True)
        .BlockPublicPolicy(True)
        .IgnorePublicAcls(True)
    )
    .VersioningConfiguration(
        s3_bucket.VersioningConfiguration().Status(s3_bucket.versioning_configuration_status.ENABLED)
    ),
    rds_cluster.DBCluster("test-cluster")
    .Engine(rds_cluster.engine.AURORA)
    .EngineMode(rds_cluster.engine_mode.PARALLEL_QUERY)
).YAML("test")