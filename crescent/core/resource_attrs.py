from crescent.functions import AnyFn
from .model import Model
from .constants import ModelRequiredProperties, get_values
from typing import Union


class ResourceSignal(Model):
    def Count(self, count: Union[int, AnyFn]):
        return self._set_field(self.Count.__name__, count)

    def Timeout(self, timeout: Union[str, AnyFn]):
        return self._set_field(self.Timeout.__name__, timeout)


class AutoscalingCreationPolicy(Model):
    def __init__(self):
        super(AutoscalingCreationPolicy, self).__init__(
            min_value={self.MinSuccessfulInstancesPercent.__name__: 0},
            max_value={self.MinSuccessfulInstancesPercent.__name__: 100}
        )

    def MinSuccessfulInstancesPercent(self, min_succesfull_instances_percent: Union[int, AnyFn]):
        return self._set_field(self.MinSuccessfulInstancesPercent.__name__, min_succesfull_instances_percent)


class CreationPolicy(Model):
    def AutoscalingCreationPolicy(self, autoscaling_creation_policy: AutoscalingCreationPolicy):
        return self._set_field(self.AutoscalingCreationPolicy.__name__, autoscaling_creation_policy)

    def ResourceSignal(self, resource_signal: ResourceSignal):
        return self._set_field(self.ResourceSignal.__name__, resource_signal)

# --------------------------------------------------------------------------------------------


class DeletionPolicy:
    DELETE = "Delete"
    RETAIN = "Retain"
    SNAPSHOT = "Snapshot"


# --------------------------------------------------------------------------------------------


class AutoScalingReplacingUpdate(Model):
    def WillReplace(self, will_replace: Union[bool, AnyFn]):
        return self._set_field(self.WillReplace.__name__, will_replace)


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
    def __init__(self):
        super(AutoScalingRollingUpdate, self).__init__(
            min_value={self.MinSuccessfullInstancesPercent.__name__: 0},
            max_value={self.MinSuccessfullInstancesPercent.__name__: 100},
            allowed_values={self.SuspendedProcesses.__name__: get_values(SuspendedProcesses)}
        )

    def MaxBatchSize(self, max_batch_size: Union[int, AnyFn]):
        return self._set_field(self.MaxBatchSize.__name__, max_batch_size)

    def MinInstancesInService(self, min_instances_in_service: Union[int, AnyFn]):
        return self._set_field(self.MinInstancesInService.__name__, min_instances_in_service)

    def MinSuccessfullInstancesPercent(self, value: Union[int, AnyFn]):
        return self._set_field(self.MinSuccessfullInstancesPercent.__name__, value)

    def PauseTime(self, value: Union[str, AnyFn]):
        return self._set_field(self.PauseTime.__name__, value)

    def SuspendedProcesses(self, *value: Union[str, AnyFn]):
        return self._set_field(self.SuspendedProcesses.__name__, list(value))

    def WaitOnResourceSignals(self, value: Union[bool, AnyFn]):
        return self._set_field(self.WaitOnResourceSignals.__name__, value)


class AutoScalingScheduledAction(Model):
    def IgnoreUnmodifiedGroupSizeProperties(self, value: Union[bool, AnyFn]):
        return self._set_field(self.IgnoreUnmodifiedGroupSizeProperties.__name__, value)


class CodeDeployLambdaAliasUpdate(Model):
    def __init__(self):
        super(CodeDeployLambdaAliasUpdate, self).__init__(required_properties=ModelRequiredProperties.CODE_DEPLOY_LAMBDA_ALIAS_UPDATE_POLICY)

    def AfterAllowTrafficHook(self, value: Union[str, AnyFn]):
        return self._set_field(self.AfterAllowTrafficHook.__name__, value)

    def ApplicationName(self, value: Union[str, AnyFn]):
        return self._set_field(self.ApplicationName.__name__, value)

    def BeforeAllowTrafficHook(self, value: Union[str, AnyFn]):
        return self._set_field(self.BeforeAllowTrafficHook.__name__, value)

    def DeploymentGroupName(self, value: Union[str, AnyFn]):
        return self._set_field(self.DeploymentGroupName.__name__, value)


class UpdatePolicy(Model):
    def __init__(self):
        super(UpdatePolicy, self).__init__(
            required_properties=[self.AutoScalingReplacingUpdate.__name__]
        )

    def AutoScalingReplacingUpdate(self, value: AutoScalingReplacingUpdate):
        return self._set_field(self.AutoScalingReplacingUpdate.__name__, value)

    def AutoScalingRollingUpdate(self, value: AutoScalingRollingUpdate):
        return self._set_field(self.AutoScalingRollingUpdate.__name__, value)

    def AutoScalingScheduledAction(self, value: AutoScalingScheduledAction):
        return self._set_field(self.AutoScalingScheduledAction.__name__, value)

    def UseOnlineResharding(self, value: Union[bool, AnyFn]):
        return self._set_field(self.UseOnlineResharding.__name__, value)

    def EnableVersionUpgrade(self, value: Union[bool, AnyFn]):
        return self._set_field(self.EnableVersionUpgrade.__name__, value)

    def CodeDeployLambdaAliasUpdate(self, value: CodeDeployLambdaAliasUpdate):
        return self._set_field(self.CodeDeployLambdaAliasUpdate.__name__, value)

# --------------------------------------------------------------------------------------------


class UpdateReplacePolicy:
    DELETE = "Delete"
    RETAIN = "Retain"
    SNAPSHOT = "Snapshot"


# --------------------------------------------------------------------------------------------


class ResourceAttributesFactory:
    DeletionPolicy = DeletionPolicy
    UpdateReplacePolicy = UpdateReplacePolicy

    class CreationPolicy:
        @staticmethod
        def Create(): return CreationPolicy()

        @staticmethod
        def AutoscalingCreationPolicy(): return AutoscalingCreationPolicy()

        @staticmethod
        def ResourceSignal(): return ResourceSignal()

    class UpdatePolicy:
        SuspendedProcesses = SuspendedProcesses

        @staticmethod
        def Create(): return UpdatePolicy()

        @staticmethod
        def AutoScalingReplacingUpdate(): return AutoScalingReplacingUpdate()

        @staticmethod
        def AutoScalingRollingUpdate(): return AutoScalingRollingUpdate()

        @staticmethod
        def AutoScalingScheduledAction(): return AutoScalingScheduledAction()

        @staticmethod
        def CodeDeployLambdaAliasUpdate(): return CodeDeployLambdaAliasUpdate()
