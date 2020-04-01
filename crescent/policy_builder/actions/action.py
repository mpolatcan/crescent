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
            raise Exception("Required resource \"{}\" must be filled or use \"*\" define policy for all resources of action {}!".format(
                self.__required_resource, self.__action_name)
            )
        else:
            return True

    def _set_resource(self, value):
        self.__resource = value
        return self

    def __get_resource__(self):
        return self.__resource

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
