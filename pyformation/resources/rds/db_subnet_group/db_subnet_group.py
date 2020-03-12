from pyformation import PyformationResource, Tag


class DBSubnetGroup(PyformationResource):
    __TYPE = "AWS::RDS::DBSubnetGroup"

    def __init__(self, id: str):
        super(DBSubnetGroup, self).__init__(id, self.__TYPE)

    def DBSubnetGroupDescription(self, value: str):
        return self._set_property(self.DBSubnetGroupDescription.__name__, value)

    def DBSubnetGroupName(self, value: str):
        return self._set_property(self.DBSubnetGroupName.__name__, value)

    def SubnetIds(self, *value: str):
        return self._set_property(self.SubnetIds.__name__, list(value))

    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
