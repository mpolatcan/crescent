from pyformation.core import Resource, Tag, Validator


class DBSubnetGroup(Resource):
    __TYPE = "AWS::RDS::DBSubnetGroup"

    def __init__(self, id: str):
        super(DBSubnetGroup, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def DBSubnetGroupDescription(self, value: str):
        return self._set_property(self.DBSubnetGroupDescription.__name__, value)

    @Validator.validate(type=str)
    def DBSubnetGroupName(self, value: str):
        return self._set_property(self.DBSubnetGroupName.__name__, value)

    @Validator.validate(type=str)
    def SubnetIds(self, *value: str):
        return self._set_property(self.SubnetIds.__name__, list(value))

    @Validator.validate(type=Tag)
    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
