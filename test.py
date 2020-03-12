from pyformation import PyformationFactory as pf

pf.Template("").Resources(
    pf.ecr.Repository(id="EcrTest").RepositoryName("ecr-test").LifecyclePolicy(
        pf.ecr.LifecyclePolicy()
    ),
    pf.firehose.DeliveryStream(id="FirehoseTest").S3DestinationConfiguration(
        pf.firehose.S3DestinationConfiguration()
    )
).YAML("test")
