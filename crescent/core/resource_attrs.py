# TODO Validations will be checked and updated
from .model import Model
from .validator import Validator
from .constants import RequiredProperties


class ResourceSignalModel(Model):
    @Validator.validate(type=int)
    def Count(self, value: int):
        return self._set_field(self.Count.__name__, value)

    @Validator.validate(type=str)
    def Timeout(self, value: str):
        return self._set_field(self.Timeout.__name__, value)


class AutoscalingCreationPolicyModel(Model):
    @Validator.validate(type=int, min_value=0, max_value=100)
    def MinSuccessfulInstancesPercent(self, value: int):
        return self._set_field(self.MinSuccessfulInstancesPercent.__name__, value)


class CreationPolicy(Model):
    @Validator.validate(type=AutoscalingCreationPolicyModel)
    def AutoscalingCreationPolicy(self, value: AutoscalingCreationPolicyModel):
        return self._set_field(self.AutoscalingCreationPolicy.__name__, value.__to_dict__())

    @Validator.validate(type=ResourceSignalModel)
    def ResourceSignal(self, value: ResourceSignalModel):
        return self._set_field(self.ResourceSignal.__name__, value.__to_dict__())

# --------------------------------------------------------------------------------------------


class DeletionPolicy:
    DELETE = "Delete"
    RETAIN = "Retain"
    SNAPSHOT = "Snapshot"

# --------------------------------------------------------------------------------------------


class AutoScalingReplacingUpdatePolicy(Model):
    @Validator.validate(type=bool)
    def WillReplace(self, value: bool):
        return self._set_field(self.WillReplace.__name__, value)


class SuspendedProcesses:
    LAUNCH = "Launch"
    TERMINATE = "Terminate"
    HEALTH_CHECK = "HealthCheck"
    REPLACE_UNHEALTHY = "ReplaceUnhealthy"
    AZ_REBALANCE = "AZRebalance"
    ALARM_NOTIFICATION = "AlarmNotification"
    SCHEDULED_ACTIONS = "ScheduledActions"
    ADD_TO_LOAD_BALANCER = "AddToLoadBalancer"


class AutoScalingRollingUpdatePolicy(Model):
    @Validator.validate(type=int)
    def MaxBatchSize(self, value: int):
        return self._set_field(self.MaxBatchSize.__name__, value)

    @Validator.validate(type=int)
    def MinInstancesInService(self, value: int):
        return self._set_field(self.MinInstancesInService.__name__, value)

    @Validator.validate(type=int, min_value=0, max_value=100)
    def MinSuccessfullInstancesPercent(self, value: int):
        return self._set_field(self.MinSuccessfullInstancesPercent.__name__, value)

    @Validator.validate(type=str)
    def PauseTime(self, value: str):
        return self._set_field(self.PauseTime.__name__, value)

    @Validator.validate(type=str, allowed_values=[
        SuspendedProcesses.LAUNCH,
        SuspendedProcesses.TERMINATE,
        SuspendedProcesses.HEALTH_CHECK,
        SuspendedProcesses.REPLACE_UNHEALTHY,
        SuspendedProcesses.AZ_REBALANCE,
        SuspendedProcesses.ALARM_NOTIFICATION,
        SuspendedProcesses.SCHEDULED_ACTIONS,
        SuspendedProcesses.ADD_TO_LOAD_BALANCER
    ])
    def SuspendedProcesses(self, *value: str):
        return self._set_field(self.SuspendedProcesses.__name__, list(value))

    @Validator.validate(type=bool)
    def WaitOnResourceSignals(self, value: bool):
        return self._set_field(self.WaitOnResourceSignals.__name__, value)


class AutoScalingScheduledActionPolicy(Model):
    @Validator.validate(type=bool)
    def IgnoreUnmodifiedGroupSizeProperties(self, value: bool):
        return self._set_field(self.IgnoreUnmodifiedGroupSizeProperties.__name__, value)


class CodeDeployLambdaAliasUpdatePolicy(Model):
    @Validator.validate(type=str)
    def AfterAllowTrafficHook(self, value: str):
        return self._set_field(self.AfterAllowTrafficHook.__name__, value)

    @Validator.validate(type=str)
    def ApplicationName(self, value: str):
        return self._set_field(self.ApplicationName.__name__, value)

    @Validator.validate(type=str)
    def BeforeAllowTrafficHook(self, value: str):
        return self._set_field(self.BeforeAllowTrafficHook.__name__, value)

    @Validator.validate(type=str)
    def DeploymentGroupName(self, value: str):
        return self._set_field(self.DeploymentGroupName.__name__, value)


class UpdatePolicy(Model):
    @Validator.validate(type=AutoScalingReplacingUpdatePolicy)
    def AutoScalingReplacingUpdate(self, value: AutoScalingReplacingUpdatePolicy):
        return self._set_field(self.AutoScalingReplacingUpdate.__name__, value.__to_dict__())

    @Validator.validate(type=AutoScalingRollingUpdatePolicy)
    def AutoScalingRollingUpdate(self, value: AutoScalingRollingUpdatePolicy):
        return self._set_field(self.AutoScalingRollingUpdate.__name__, value.__to_dict__())

    @Validator.validate(type=AutoScalingScheduledActionPolicy)
    def AutoScalingScheduledAction(self, value: AutoScalingScheduledActionPolicy):
        return self._set_field(self.AutoScalingScheduledAction.__name__, value.__to_dict__())

    @Validator.validate(type=bool)
    def UseOnlineResharding(self, value: bool):
        return self._set_field(self.UseOnlineResharding.__name__, value)

    @Validator.validate(type=bool)
    def EnableVersionUpgrade(self, value: bool):
        return self._set_field(self.EnableVersionUpgrade.__name__, value)

    @Validator.validate(type=CodeDeployLambdaAliasUpdatePolicy, required_properties=RequiredProperties.CODE_DEPLOY_LAMBDA_ALIAS_UPDATE_POLICY)
    def CodeDeployLambdaAliasUpdate(self, value: CodeDeployLambdaAliasUpdatePolicy):
        return self._set_field(self.CodeDeployLambdaAliasUpdate.__name__, value.__to_dict__())

# --------------------------------------------------------------------------------------------


class UpdateReplacePolicy:
    DELETE = "Delete"
    RETAIN = "Retain"
    SNAPSHOT = "Snapshot"

