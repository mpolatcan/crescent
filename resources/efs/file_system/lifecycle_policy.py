from resources.shared import BaseModel


class LifecyclePolicy(BaseModel):
    __PROPERTY_TRANSITION_TO_IA = "TransitionToIA"

    def transition_to_ia(self, value: str):
        return self._add_field(self.__PROPERTY_TRANSITION_TO_IA, value)
