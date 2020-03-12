from pyformation import PyformationResource, Tag


class DBClusterParameterGroup(PyformationResource):
    __TYPE = "AWS::RDS::DBClusterParameterGroup"

    def __init__(self, id: str):
        super(DBClusterParameterGroup, self).__init__(id, self.__TYPE)

    def Description(self, value: str):
        return self._set_property(self.Description.__name__, value)

    def Family(self, value: str):
        return self._set_property(self.Family.__name__, value)

    def Parameters(self, value: dict):
        return self._set_property(self.Parameters.__name__, value)

    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
