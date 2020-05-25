from crescent import (
    CrescentFactory as cf,
    Rds as rds,
    DynamoDB as ddb,
    ApiGatewayV2 as api_gw_v2
)

cf.Template().Resources(
    rds.DBCluster.Create("TestDBCluster")
       .Engine(cf.Fn.Ref("test"))
       .EngineVersion(rds.DBCluster.EngineVersion.AuroraMysql.V_2_04_2)
       .Metadata(
            cf.Metadata.Create().KeyValue(
                cluster_name="test",
                engine="mysql"
            )
       ).DatabaseName("test-database").Condition("test"),
    rds.OptionGroup.Create("TestOptionGroup")
       .EngineName("test-engine")
       .MajorEngineVersion("11.2")
       .OptionConfigurations(
            rds.OptionGroup.OptionConfiguration()
               .OptionName("test")
       ).OptionGroupDescription("test-description")
       .DependsOn("test"),
    ddb.Table.Create("test")
       .KeySchema()
       .BillingMode(ddb.Table.BillingMode.PROVISIONED)
       .LocalSecondaryIndexes(ddb.Table.LocalSecondaryIndex().Projection(
            ddb.Table.Projection().ProjectionType(ddb.Table.ProjectionType.ALL)
       ).IndexName("test").KeySchema(
            ddb.Table.KeySchema().KeyType(ddb.Table.KeyType.HASH)
       )),
    api_gw_v2.Api.Create("test").BasePath(
        api_gw_v2.Api.BasePath.PREPEND
    )
).Parameters(
    cf.Parameter.Create("TestParameter", cf.Parameter.Type.Aws.Ec2.SecurityGroupIdList)
      .AllowedValues("test1", "test2", "test3")
).Mappings(
   cf.Mapping("test")
).Metadata(
    cf.Metadata.Create()
      .Json({
        "MetadataTest": {
            "crescent": "formation"
        }
      }),
    cf.Metadata.CfnAuthentication.Create("CfnAuthenticationTest")
      .type("basic")
      .username("mpolatcan")
      .password("12345"),
    cf.Metadata.CfnInterface.Create("CfnInterfaceTest")
    .ParameterGroups(
        cf.Metadata.CfnInterface.ParameterGroup()
          .Label(
            cf.Metadata.CfnInterface.Label().default("test")
          ).Parameters("a", "b", "c")
    ).ParameterLabels(
        cf.Metadata.CfnInterface.ParameterLabel("test")
          .Label(
            cf.Metadata.CfnInterface.Label().default("test")
          )
    )
).Outputs(
    cf.Output("OutputTest")
      .Description("Output Test Description")
      .Value("Output Test Value"),
    cf.Output("OutputTest")
      .Description("Output Test Description")
      .Value("Output Test Value")
).Conditions(
    cf.Condition("ConditionTest", cf.Fn.Equals(cf.Fn.Ref("RefTest"), "abc"))
).Yaml("test")
