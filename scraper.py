# scraper.py

import concurrent.futures
from newspaper import Article
from duckduckgo_search import DDGS

def fetch_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return {"url": url, "text": article.text}
    except:
        return None

def fetch_links_and_articles(query, max_results=3):
    results = []
    urls = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            url = r.get("href") or r.get("url")
            if url:
                urls.append(url)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = executor.map(fetch_article, urls)
        for article in futures:
            if article:
                results.append(article)

    return results
