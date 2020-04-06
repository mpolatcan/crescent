from crescent import CrescentFactory as cf, Rds as rds

cf.Template().Resources(
    rds.DBCluster.Create("TestDBCluster")
    .Engine(rds.DBCluster.Engine.AURORA_MYSQL),
    rds.OptionGroup.Create("TestOptionGroup")
    .EngineName("test-engine")
    .MajorEngineVersion("11.2")
    .OptionConfigurations(
        rds.OptionGroup.OptionConfiguration().OptionName("test")
    )
    .OptionGroupDescription("test-description")
    .DependsOn(
        "test"
    )
    .Metadata(
        Description="Test description for Crescent"
    )
).Parameters(
    cf.Parameter.Create("TestParameter", cf.Parameter.Type.Aws.Ec2.SecurityGroupNameList)
    .AllowedValues(
        "test1",
        "test2",
        "test3"
    )
).Mappings(
   cf.Mapping.Create("test").KV(
       cf.Mapping.KV("a", "b"),
       cf.Mapping.KV("test", "ava")
   )
).Yaml("test")
