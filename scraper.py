import feedparser

FEEDS = {
    "Google News": "https://news.google.com/rss/search?q=deepfakes",
    "The Verge": "https://www.theverge.com/rss/index.xml",
    "BBC News": "http://feeds.bbci.co.uk/news/technology/rss.xml",
}

def fetch_articles():
    articles = []
    for source, url in FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if "deepfake" in (entry.title + entry.get("summary", "")).lower():
                articles.append({
                    "url": entry.link,
                    "title": entry.title,
                    "source": source,
                    "published": entry.get("published", ""),
                    "content": entry.get("summary", "")
                })
    return articles
