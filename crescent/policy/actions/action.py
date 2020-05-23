class Action:
    __KEY_REQUIRED = "required"
    __KEY_OPTIONAL = "optional"

    def __init__(self, service, action_name, **definable_resources):
        self.__service = service
        self.__action_name = "{}:{}".format(service, action_name)
        self.__required_resources = definable_resources.get(self.__KEY_REQUIRED, [])
        self.__optional_resources = definable_resources.get(self.__KEY_OPTIONAL, [])

        self.__resources = {}

        self.__all_resources = self.__required_resources + self.__optional_resources

    def AllResources(self):
        self.__resources = "*"
        return self

    def _set_resource(self, resource, value):
        if len(self.__all_resources) == 0:
            self.__resources = "*"

        if isinstance(self.__resources, dict):
            self.__resources[resource] = value

        return self

    def __get_resources__(self):
        return tuple(self.__resources.values()) if isinstance(self.__resources, dict) else self.__resources

    def __validate__(self):
        if self.__resources is None:
            raise Exception(
                (
                    "Required resources \"{required_resources}\" must be filled or use \"*\" "
                    "define policy for all resources of action {action}!"
                ).format(required_resource=",".join(self.__required_resources), action=self.__action_name)
            )
        else:
            if self.__resources != "*":
                for required_resource in self.__required_resources:
                    if required_resource not in self.__resources.keys():
                        raise Exception(
                            (
                                "Required resource \"{required_resource}\" must be filled or use \"*\" "
                                "define policy for all resources of action {action}!"
                            ).format(required_resource=required_resource, action=self.__action_name)
                        )

            return True

    def __get_service__(self):
        return self.__service

    def __str__(self):
        return self.__action_name

    def __repr__(self):
        return self.__action_name


# -------------------------------

__IGNORED_DICT_KEYS__ = ['__module__', '__dict__', '__weakref__', '__doc__']


class AccessLevelAllActions(list):
    def __init__(self, access_level):
        super(AccessLevelAllActions, self).__init__()
        self.extend([
            getattr(access_level, fn)()
            for fn in [fn for fn in access_level.__dict__.keys() if fn not in __IGNORED_DICT_KEYS__]
        ])

    def _set_all_actions_resources(self, resource, *value):
        for action in self:
            getattr(action, resource)(*value)

        return self

    def AllResources(self):
        return self._set_all_actions_resources(self.AllResources.__name__)
