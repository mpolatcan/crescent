from .buffering_hints import BufferingHints


class ElasticsearchBufferingHints(BufferingHints):
    def __init__(self):
        super(ElasticsearchBufferingHints, self).__init__()
