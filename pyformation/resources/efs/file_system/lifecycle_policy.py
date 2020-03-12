from pyformation import PyformationModel


class LifecyclePolicy(PyformationModel):
    __PROPERTY_TRANSITION_TO_IA = "TransitionToIA"

    def TransitionToIA(self, value: str):
        return self._set_field(self.TransitionToIA.__name__, value)
