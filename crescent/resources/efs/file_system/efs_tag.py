from crescent.core import Tag


class ElasticFileSystemTag(Tag):
    def __init__(self, key: str, value: str):
        super(ElasticFileSystemTag, self).__init__(key, value)
