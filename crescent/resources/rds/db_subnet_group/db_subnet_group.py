from crescent.core import Resource, Tag, Validator


class DBSubnetGroup(Resource):
    __TYPE = "AWS::RDS::DBSubnetGroup"

    def __init__(self, id: str):
        super(DBSubnetGroup, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def DBSubnetGroupDescription(self, db_subnet_group_description: str):
        return self._set_property(self.DBSubnetGroupDescription.__name__, db_subnet_group_description)

    @Validator.validate(type=str, max_length=255)
    def DBSubnetGroupName(self, db_subnet_group_name: str):
        return self._set_property(self.DBSubnetGroupName.__name__, db_subnet_group_name)

    @Validator.validate(type=str)
    def SubnetIds(self, *subnet_ids: str):
        return self._set_property(self.SubnetIds.__name__, list(subnet_ids))

    @Validator.validate(type=Tag)
    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
