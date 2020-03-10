from pyformation.resources.shared import Tag


class ElasticFileSystemTag(Tag):
    def __init__(self, key, value):
        super(ElasticFileSystemTag, self).__init__(key, value)
