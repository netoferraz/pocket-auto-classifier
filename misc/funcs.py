from pocket import Pocket
from typing import List, Dict


def retrieve_articles_from_tags(api: Pocket, tags: List[str]) -> List[Dict]:
    # initialize a container to holds data
    container = []
    for tag in tags:
        results = api.retrieve(tag=tag)
        if not results["error"]:
            for result in results["list"].values():
                article = {}
                article["item_id"] = result.get("item_id", None)
                article["resolved_id"] = result.get("resolved_id", None)
                article["given_url"] = result.get("given_url", None)
                article["given_title"] = result.get("given_title", None)
                article["resolved_url"] = result.get("resolved_url", None)
                article["resolved_title"] = result.get("resolved_title", None)
                article["is_article"] = result.get("is_article", None)
                article["excerpt"] = result.get("excerpt", None)
                article["word_count"] = result.get("word_count", None)
                article["lang"] = result.get("lang", None)
                domain_metadata = result.get("domain_metadata", None)
                if domain_metadata:
                    article["domain_metadata"] = domain_metadata.get("name", None)
                article["tag"] = tag
                container.append(article)
    return container
