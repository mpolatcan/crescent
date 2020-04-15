from crescent.policy_builder import PolicyBuilder, Actions
from crescent import Rds as rds


print(PolicyBuilder("test").AllowActions(
    Actions.Rds.WriteAll()
    .Cluster(rds.Arn.ClusterArn("*", region="*", account_id="*"))
    .DBInstance(rds.Arn.DBArn("*", region="*", account_id="*"))
    .EventSubscription(rds.Arn.EventSubscriptionArn("*", region="*", account_id="*"))
    .ClusterParameterGroup(rds.Arn.ClusterParameterGroupArn("*", region="*", account_id="*"))
    .ClusterSnapshot(rds.Arn.ClusterEndpointArn("*", region="*", account_id="*"))
    .ParameterGroup(rds.Arn.ParameterGroupArn("*", region="*", account_id="*"))
    .Snapshot(rds.Arn.SnapshotArn("*", region="*", account_id="*"))
    .OptionGroup(rds.Arn.OptionGroupArn("test", region="*", account_id="*"))
    .ClusterEndpoint(rds.Arn.ClusterEndpointArn("*", region="*", account_id="*"))
    .Proxy(rds.Arn.ProxyArn("test", region="*", account_id="*"))
    .SecurityGroup(rds.Arn.SecurityGroupArn("*", region="*", account_id="*"))
    .SubnetGroup(rds.Arn.SubnetGroupArn("*", region="*", account_id="*"))
    .TargetGroup(rds.Arn.TargetGroupArn("*", region="*", account_id="*"))
    .ReservedInstance(rds.Arn.ReservedInstanceArn("test", region="*", account_id="*")),
    Actions.Kinesis.WriteAll().AllResources()
).Create())
