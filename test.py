from crescent import CrescentFactory as cf, rds

cf.Template().Resources(
    rds.DBCluster().Create("Test1")
    .Engine(rds.DBCluster.Engine.AURORA_MYSQL)
    .EngineMode(rds.DBCluster.EngineMode.SERVERLESS)
    .EngineVersion(rds.DBCluster.EngineVersion.AuroraMysql.V_2_03_3)
    .ScalingConfiguration(rds.DBCluster.ScalingConfiguration().MinCapacity(2).MaxCapacity(2))
    .AssociatedRoles(rds.DBCluster.DBClusterRole().RoleArn("arn:bucket:adadka"))
    .AvailabilityZones(cf.Zone.FRANKFURT_EU_CENTRAL_1.A)
    .UpdatePolicy(
        cf.UpdatePolicy.Create().AutoScalingReplacingUpdate(
            cf.UpdatePolicy.AutoScalingReplacingUpdate().WillReplace(True)
        ).EnableVersionUpgrade(True)
    ).DeletionPolicy(cf.DeletionPolicy.SNAPSHOT).UpdateReplacePolicy(cf.UpdateReplacePolicy.DELETE),
    rds.DBInstance.Create("Test2")
        .Engine(rds.DBInstance.Engine.MYSQL)
        .DBInstanceClass(rds.DBInstance.DBInstanceClass.M5_8XL_32_VCPU_128GIB_MEM)
        .EngineVersion(rds.DBInstance.EngineVersion.Mysql.V_5_5_53),
    rds.DBParameterGroup.Create("Test3")
        .Family(rds.DBParameterGroup.EngineFamily.OracleEe.V_18)
        .Description("test-description"),
    rds.DBClusterParameterGroup.Create("Test4")
        .Family(rds.DBClusterParameterGroup.EngineFamily.AuroraMysql.V_5_7)
        .Description("test-description")
        .Parameters({})
).YAML("test")
