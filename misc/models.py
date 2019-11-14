class PocketData:
    def __init__(self, **kwargs):
        self.item_id = kwargs.get("item_id", None)
        self.resolved_id = kwargs.get("resolved_id", None)
        self.given_url = kwargs.get("given_url", None)
        self.given_title = kwargs.get("given_title", None)
        self.resolved_url = kwargs.get("resolved_url", None)
        self.resolved_title = kwargs.get("resolved_title", None)
        self.is_article = kwargs.get("is_article", None)
        self.excerpt = kwargs.get("excerpt", None)
        self.word_count = kwargs.get("word_count", None)
        self.lang = kwargs.get("lang", None)
        self.domain_metadata = kwargs.get("domain_metadata", None)
        self.tag = kwargs.get("tag", None)
