from .model import Model
from .validator import Validator
from .constants import ModelRequiredProperties


class ResourceSignal(Model):
    @Validator.validate(type=int)
    def Count(self, value: int):
        return self._set_field(self.Count.__name__, value)

    @Validator.validate(type=str)
    def Timeout(self, value: str):
        return self._set_field(self.Timeout.__name__, value)


class AutoscalingCreationPolicy(Model):
    @Validator.validate(type=int, min_value=0, max_value=100)
    def MinSuccessfulInstancesPercent(self, value: int):
        return self._set_field(self.MinSuccessfulInstancesPercent.__name__, value)


class _CreationPolicy(Model):
    @Validator.validate(type=AutoscalingCreationPolicy)
    def AutoscalingCreationPolicy(self, value: AutoscalingCreationPolicy):
        return self._set_field(self.AutoscalingCreationPolicy.__name__, value.__to_dict__())

    @Validator.validate(type=ResourceSignal)
    def ResourceSignal(self, value: ResourceSignal):
        return self._set_field(self.ResourceSignal.__name__, value.__to_dict__())

# --------------------------------------------------------------------------------------------


class AutoScalingReplacingUpdate(Model):
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


class AutoScalingRollingUpdate(Model):
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


class AutoScalingScheduledAction(Model):
    @Validator.validate(type=bool)
    def IgnoreUnmodifiedGroupSizeProperties(self, value: bool):
        return self._set_field(self.IgnoreUnmodifiedGroupSizeProperties.__name__, value)


class CodeDeployLambdaAliasUpdate(Model):
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


class _UpdatePolicy(Model):
    @Validator.validate(type=AutoScalingReplacingUpdate)
    def AutoScalingReplacingUpdate(self, value: AutoScalingReplacingUpdate):
        return self._set_field(self.AutoScalingReplacingUpdate.__name__, value.__to_dict__())

    @Validator.validate(type=AutoScalingRollingUpdate)
    def AutoScalingRollingUpdate(self, value: AutoScalingRollingUpdate):
        return self._set_field(self.AutoScalingRollingUpdate.__name__, value.__to_dict__())

    @Validator.validate(type=AutoScalingScheduledAction)
    def AutoScalingScheduledAction(self, value: AutoScalingScheduledAction):
        return self._set_field(self.AutoScalingScheduledAction.__name__, value.__to_dict__())

    @Validator.validate(type=bool)
    def UseOnlineResharding(self, value: bool):
        return self._set_field(self.UseOnlineResharding.__name__, value)

    @Validator.validate(type=bool)
    def EnableVersionUpgrade(self, value: bool):
        return self._set_field(self.EnableVersionUpgrade.__name__, value)

    @Validator.validate(type=CodeDeployLambdaAliasUpdate, required_properties=ModelRequiredProperties.CODE_DEPLOY_LAMBDA_ALIAS_UPDATE_POLICY)
    def CodeDeployLambdaAliasUpdate(self, value: CodeDeployLambdaAliasUpdate):
        return self._set_field(self.CodeDeployLambdaAliasUpdate.__name__, value.__to_dict__())

# --------------------------------------------------------------------------------------------


class CreationPolicy:
    @staticmethod
    def Create():
        return _CreationPolicy()

    @staticmethod
    def AutoscalingCreationPolicy():
        return AutoscalingCreationPolicy()

    @staticmethod
    def ResourceSignal():
        return ResourceSignal()


class DeletionPolicy:
    DELETE = "Delete"
    RETAIN = "Retain"
    SNAPSHOT = "Snapshot"


class UpdatePolicy:
    SuspendedProcesses = SuspendedProcesses

    @staticmethod
    def Create():
        return _UpdatePolicy()

    @staticmethod
    def AutoScalingReplacingUpdate():
        return AutoScalingReplacingUpdate()

    @staticmethod
    def AutoScalingRollingUpdate():
        return AutoScalingRollingUpdate()

    @staticmethod
    def AutoScalingScheduledAction():
        return AutoScalingScheduledAction()

    @staticmethod
    def CodeDeployLambdaAliasUpdate():
        return CodeDeployLambdaAliasUpdate()


class UpdateReplacePolicy:
    DELETE = "Delete"
    RETAIN = "Retain"
    SNAPSHOT = "Snapshot"
