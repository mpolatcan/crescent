from pyformation import PyformationFactory as pf

ds = pf.firehose.delivery_stream

pf.Template().Resources(
    ds.DeliveryStream("test-stream")
        .ExtendedS3DestinationConfiguration(
            ds.ExtendedS3DestinationConfiguration()
            .DataFormatConversionConfiguration(
                ds.DataFormatConversionConfiguration()
                .Enabled(True)
                .InputFormatConfiguration(
                    ds.InputFormatConfiguration()
                    .Deserializer(
                        ds.Deserializer()
                    )
                ).OutputFormatConfiguration(
                    ds.OutputFormatConfiguration()
                    .Serializer(
                        ds.Serializer()
                    )
                ).SchemaConfiguration(
                    ds.SchemaConfiguration()
                    .CatalogId("test-catalog-id")
                    .RoleARN("test-role-arn")
                    .VersionId("test-version-id")
                    .DatabaseName("test-database-name")
                    .Region("test-region")
                    .TableName("test-table-name")
                )
            )
            .BucketARN("arn:aws:bucket-arn")
            .BufferingHints(
                ds.BufferingHints()
                .SizeInMBs(128)
                .IntervalInSeconds(60)
            ).CompressionFormat(
                ds.compression.s3.SNAPPY
            ).RoleARN("arn:aws:role-arn")
        )
).YAML("test")