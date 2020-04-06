class Action:
    def __init__(self, service, action_name, required_resource=None):
        self.__service = service
        self.__action_name = "{}:{}".format(service, action_name)
        self.__required_resource = required_resource
        self.__resource = "*" if required_resource is None else None

    def AllResources(self):
        self.__resource = "*"
        return self

    def __validate__(self):
        if self.__resource is None:
            raise Exception(
                (
                    "Required resource \"{required_resource}\" must be filled or use \"*\" "
                    "define policy for all resources of action {action}!"
                ).format(required_resource=self.__required_resource, action=self.__action_name)
            )
        else:
            return True

    def _set_resource(self, resource_key, value):
        if self.__required_resource is None:
            raise Exception("You can't set resource \"{resource}\" which it is not required for action {action}!".format(
                resource=resource_key, action=self.__action_name)
            )

        if resource_key != self.__required_resource:
            raise Exception(
                (
                    "Expecting required resource \"{required_resource}\" but given \"{given_resource}\" for "
                    "action {action}!"
                ).format(required_resource=self.__required_resource, given_resource=resource_key, action=self.__action_name))

        self.__resource = value

        return self

    def __get_resource__(self):
        return self.__resource

    def __get_required_resource_name__(self):
        return self.__required_resource

    def __get_service__(self):
        return self.__service

    def __str__(self):
        return self.__action_name

    def __repr__(self):
        return self.__action_name


# -------------------------------

__IGNORED_DICT_KEYS__ = ['__module__', '__dict__', '__weakref__', '__doc__']


class AccessLevelAllActions:
    def __init__(self, access_level):
        self._actions = [
            getattr(access_level, fn)()
            for fn in [fn for fn in access_level.__dict__.keys() if fn not in __IGNORED_DICT_KEYS__]
        ]

    def AllResources(self):
        return [action.AllResources() for action in self._actions]
